import os, json, requests


def authenticate():
    url = os.environ.get("login_url")
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    payload = json.dumps(
        {
            "client_id": client_id,
            "client_secret": client_secret,
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        if response.status_code == 200:
            token = response.json().get('token')
            return token
    except Exception:
        return False
    return False


def send_data(data=None):
    url = os.environ.get("send_url")
    token = authenticate()
    response = ""
    if token and data:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response = response.json()
        print('response:', response)
        if response.get('code') == 0:
            return 0, response.get("import_id")
    return 2, response