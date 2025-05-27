import requests
import json
import time
VK_TOKEN = 'vk1.a.UkVnuPPdpP9-cpep5eEbKQ9GtslTUp0gfTCOz4vWo7fiWvCzkIIXaeMlbEM_CLAmYq5siMKL6VQGXyZ1Y8kRpWY_00y_BhmQIoMYK8LaPU5P_jlwyUnjfeVToZr4vTzkVraCh0vmSzR8jJEMB8SLeBJpdd30AEcJ9DXL18Y6WCTbWvcqe6ubKbLkRcEoVJzYPFTE8svay_tvMkRPkNCdSQ'
owner_id = '188340531'
VK_API_VERSION = '5.199'
def create_post():
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': owner_id,
        'message': 'Создаем надпись на стене через вк апи',
        'access_token': VK_TOKEN,
        'v': VK_API_VERSION
    }
    r = requests.get(url, params=params)
    safe_params = dict(params)
    if 'access_token' in safe_params:
        safe_params['access_token'] = '***'
    with open('create_post.json', 'w', encoding='utf-8') as f:
        log = {
            "method": "GET",
            "url": url,
            "params": safe_params,
            "response": r.json()
        }
        json.dump(log, f, ensure_ascii=False, indent=2)
    post_id = r.json().get('response', {}).get('post_id')
    if post_id:
        input("Запись на стене успешно создана. Можете проверить результат.")
        url_check = 'https://api.vk.com/method/wall.getById'
        params_check = {
            'posts': f"{owner_id}_{post_id}",
            'access_token': VK_TOKEN,
            'v': VK_API_VERSION
        }
        r_check = requests.get(url_check, params=params_check)
        safe_params_check = dict(params_check)
        if 'access_token' in safe_params_check:
            safe_params_check['access_token'] = '***'
        with open('get_post.json', 'w', encoding='utf-8') as f_check:
            log_check = {
                "method": "GET",
                "url": url_check,
                "params": safe_params_check,
                "response": r_check.json()
            }
            json.dump(log_check, f_check, ensure_ascii=False, indent=2)
        print("Ответ на get-запрос к созданному посту находится в файле get_post.json")
    else:
        print("Ошибка при создании поста")
    return post_id
def edit_post(post_id):
    url = 'https://api.vk.com/method/wall.edit'
    new_message = 'Редактируем запись на стене через вк апи'
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'message': new_message,
        'access_token': VK_TOKEN,
        'v': VK_API_VERSION
    }
    r = requests.get(url, params=params)
    safe_params = dict(params)
    if 'access_token' in safe_params:
        safe_params['access_token'] = '***'
    with open('edit_post.json', 'w', encoding='utf-8') as f:
        log = {
            "method": "GET",
            "url": url,
            "params": safe_params,
            "response": r.json()
        }
        json.dump(log, f, ensure_ascii=False, indent=2)

    time.sleep(2)

    url_check = 'https://api.vk.com/method/wall.getById'
    params_check = {
        'posts': f"{owner_id}_{post_id}",
        'access_token': VK_TOKEN,
        'v': VK_API_VERSION
    }
    r_check = requests.get(url_check, params=params_check)
    safe_params_check = dict(params_check)
    if 'access_token' in safe_params_check:
        safe_params_check['access_token'] = '***'
    with open('get_edit_post.json', 'w', encoding='utf-8') as f_check:
        log_check = {
            "method": "GET",
            "url": url_check,
            "params": safe_params_check,
            "response": r_check.json()
        }
        json.dump(log_check, f_check, ensure_ascii=False, indent=2)
    input("Ответ на get-запрос к отредактированной записи сохранён в файле get_edit_post.json")


def delete_post(post_id):
    url = 'https://api.vk.com/method/wall.delete'
    params = {
        'owner_id': owner_id,
        'post_id': post_id,
        'access_token': VK_TOKEN,
        'v': VK_API_VERSION
    }
    r = requests.get(url, params=params)
    safe_params = dict(params)
    if 'access_token' in safe_params:
        safe_params['access_token'] = '***'
    with open('delete_post.json', 'w', encoding='utf-8') as f:
        log = {
            "method": "GET",
            "url": url,
            "params": safe_params,
            "response": r.json()
        }
        json.dump(log, f, ensure_ascii=False, indent=2)
    if r.json().get('response') == 1:
        print("Запись на стене успешно удалена.")
    else:
        print("Ошибка при удалении записи")
url_wall = 'https://api.vk.com/method/wall.get'
params_wall = {
    'owner_id': owner_id,
    'access_token': VK_TOKEN,
    'v': VK_API_VERSION,
    'count': 1
}
r_wall = requests.get(url_wall, params=params_wall)
count_before = r_wall.json().get('response', {}).get('count')
print("Количество записей на стене:", count_before)
post_id = create_post()
r_wall = requests.get(url_wall, params=params_wall)
count_after = r_wall.json().get('response', {}).get('count')
print("Количество записей на стене:", count_after)
if post_id:
    edit_post(post_id)
    r_wall = requests.get(url_wall, params=params_wall)
    count_before_del = r_wall.json().get('response', {}).get('count')
    print("Количество записей на стене:", count_before_del)
    delete_post(post_id)
    r_wall = requests.get(url_wall, params=params_wall)
    count_after_del = r_wall.json().get('response', {}).get('count')
    print("Количество записей на стене:", count_after_del)
else:
    print("Не удалось создать пост. Убедитесь в том, что ваш токен еще действует и нет ошибки в owner_id.")


