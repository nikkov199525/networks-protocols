FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt update && apt install -y cron
RUN pip install -r requirements.txt
RUN chmod +x certbot.sh
COPY renew.cron /etc/cron.d/renew
RUN chmod 0644 /etc/cron.d/renew

CMD ["/bin/bash", "-c", "crontab /etc/cron.d/renew && cron && python start.py"]
