from flask import Flask, jsonify, render_template_string, request, send_file, Response
import sqlite3, os, requests
from db import save_entry
from ip_to_asn import get_as_info
from correlate import find_correlated_events
from ripe_stats import download_and_parse_ripe_asns
import matplotlib.pyplot as plt

app = Flask(__name__)
DB = 'dnsmon.db'

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''SELECT asn, asn_desc,
                 SUM(CASE WHEN source='http' THEN 1 ELSE 0 END),
                 SUM(CASE WHEN source='dns' THEN 1 ELSE 0 END),
                 SUM(CASE WHEN source='js' THEN 1 ELSE 0 END),
                 SUM(CASE WHEN source='nsdni' THEN 1 ELSE 0 END)
                 FROM ip_asn
                 GROUP BY asn, asn_desc
                 ORDER BY 3+4+5+6 DESC''')
    rows = c.fetchall()
    conn.close()
    html = """<h1>Статистика</h1>
<h2>Генерация страницы с внедренным скриптом</h2>
<form method="post" action="/inject">
  <label>Введите адрес сайта</label><br>
  <input name="url" type="text" style="width: 400px;">
  <button type="submit">Сгенерировать</button>
</form>

<p><a href='/asn-graph'>График ASN</a> | <a href='/correlation'>Связанные события</a></p>
<table border=1 cellpadding=4>
<tr><th>ASN</th><th>Описание</th><th>HTTP</th><th>DNS</th><th>JS</th><th>NSDNI</th></tr>
{% for asn,desc,h,d,j,n in rows %}
<tr><td>{{asn}}</td><td>{{desc}}</td><td>{{h}}</td><td>{{d}}</td><td>{{j}}</td><td>{{n}}</td></tr>
{% endfor %}
</table>"""
    return render_template_string(html, rows=rows)

@app.route('/submit', methods=['POST'])
def submit():
    ip = request.remote_addr
    info = get_as_info(ip)
    save_entry(info['ip'], info['asn'], info['asn_desc'], 'js')
    return jsonify({'status':'ok'})

@app.route('/api/stats')
def api_stats():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT source, COUNT(*) FROM ip_asn GROUP BY source')
    rows = c.fetchall()
    conn.close()
    return jsonify({s: c for s, c in rows})

@app.route('/asn-graph')
def asn_graph():
    data = download_and_parse_ripe_asns()
    years = list(data.keys())
    vals = list(data.values())
    plt.figure(figsize=(8, 4))
    plt.bar(years, vals)
    plt.title('Регистрация ASN (RU)')
    plt.xlabel('Год')
    plt.ylabel('Кол-во')
    plt.tight_layout()
    path = 'static/asn_graph.png'
    plt.savefig(path)
    plt.close()
    return send_file(path, mimetype='image/png')

@app.route('/correlation')
def correlation():
    data = find_correlated_events()
    html = """<h1>Связанные события</h1>
    <table border=1 cellpadding=4>
    <tr><th>IP</th><th>DNS</th><th>Событие</th><th>Время</th></tr>
    {% for d in data %}
    <tr><td>{{d.ip}}</td><td>{{d.dns_time}}</td><td>{{d.source}}</td><td>{{d.event_time}}</td></tr>
    {% endfor %}
    </table>"""
    return render_template_string(html, data=data)

@app.route("/inject", methods=["POST"])
def inject():
    target_url = request.form.get("url")
    if not target_url:
        return "URL не указан", 400

    try:
        resp = requests.get(target_url, timeout=5)
        html = resp.text
        script_tag = '<script src="/static/client.js"></script>'

        if "</head>" in html:
            html = html.replace("</head>", f"{script_tag}</head>")
        elif "</body>" in html:
            html = html.replace("</body>", f"{script_tag}</body>")
        else:
            html += script_tag

        return Response(html, mimetype="text/html")

    except Exception as e:
        return f"Ошибка запроса: {e}", 500

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=8000)
