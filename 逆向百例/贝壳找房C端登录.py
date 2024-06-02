import json

import execjs
import requests

username = '18933333333'
password = 'TestLogin'

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/125.0.0.0 Safari/537.36'})

login_url = 'https://clogin.ke.com/login'
login_params = {
    'service': 'http://m.ke.com/my/checklogin?redirect=https://m.ke.com/my/index',
    'type': '2'
}
session.get(login_url, params=login_params)  # 初始化cookie

with open('贝壳找房C端登录.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

crosSdkDT2019DeviceId = execjs.compile(js_file).call('get_crosSdkDT2019DeviceId')

session.cookies.update({'crosSdkDT2019DeviceId': crosSdkDT2019DeviceId})  # 更新cookie参数

session.get('https://clogin.ke.com/authentication/sdk/init?version=2.0')

# ==================== 获取loginTicketId ====================
get_loginTicketId_url = 'https://clogin.ke.com/authentication/initialize'
get_loginTicketId_headers = {
    "Content-Type": "application/json",
}
get_loginTicketId_data = {
    "service": "http://m.ke.com/my/checklogin?redirect=https://m.ke.com/my/index",
    "context": {
        "deviceId": "default",
        "sign": "default"
    },
    "version": "2.0"
}
get_loginTicketId_data = json.dumps(get_loginTicketId_data, separators=(',', ':'))
get_loginTicketId_respones = session.post(get_loginTicketId_url, data=get_loginTicketId_data,
                                          headers=get_loginTicketId_headers)

loginTicketId_dict = get_loginTicketId_respones.json()
loginTicketId = loginTicketId_dict['loginTicketId']
# ==================== 获取dataId ====================
get_dataId_cookies = session.cookies.get_dict()
get_dataId_cookies = "; ".join(f"{k}={v}" for k, v in get_dataId_cookies.items())
get_dataId_url = 'https://public-digc.ke.com/h5/v2/g'
get_dataId_datas = execjs.compile(js_file).call('get_k_and_d', get_dataId_cookies)
get_dataId_headers = {
    "Content-Type": "application/json",
}
get_dataId_data = {
    "k": get_dataId_datas['k'],
    "d": get_dataId_datas['d'],
    "clientType": "h5"
}
get_dataId_data = json.dumps(get_dataId_data, separators=(',', ':'))
get_dataId_respones = session.post(get_dataId_url, data=get_dataId_data, headers=get_dataId_headers)
get_dataId_respones_dict = get_dataId_respones.json()

dataId = get_dataId_respones_dict['data']
# ==================== 尝试登录 ====================
start_login_url = "https://clogin.ke.com/authentication/authenticate"
password_enc = execjs.compile(js_file).call('password_enc', password)
start_login_data = {
    "mainAuthMethodName": "username-password",
    "credential": {
        "username": username,
        "password": password_enc,
        "ioaRunState": False,
        "ioaMid": "",
        "alertSt": "",
        "ioaStateVersion": 2,
        "encodeVersion": "2"
    },
    "withCaptcha": False,
    "context": {
        "dataId": dataId,
        "msg": "",
        "deviceId": "default",
        "sign": "default"
    },
    "version": "2.0",
    "accountSystem": "customer",
    "service": "http://m.ke.com/my/checklogin?redirect=https://m.ke.com/my/index",
    "loginTicketId": loginTicketId
}
start_login_data = json.dumps(start_login_data, separators=(',', ':'))
start_login_response = session.post(start_login_url, data=start_login_data, headers=get_loginTicketId_headers)

print(start_login_response.text)
