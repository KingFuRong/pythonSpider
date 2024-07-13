import uuid
import execjs

import requests
import json
from Utils.tools import *

session = requests.Session()
session.cookies.clear()
session.headers.clear()
with open('./米游社.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://www.miyoushe.com",
    "pragma": "no-cache",
    "referer": "https://www.miyoushe.com/",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
session.headers.update(headers)

url = "https://h5collector.mihoyo.com/h5/upload"
data = {
    "page_info": {
        "app_id": "510",
        "page_url": "mihoyo-account-sdk",
        "page_name": "mihoyo-account-sdk",
        "page_fullurl": "https://www.miyoushe.com/zzz/",
        "document_referrer": "https://www.miyoushe.com/",
        "extra_info": {
            "is_v2_platform": "1",
            "sdk_version": "2.28.0",
            "environment": "production",
            "app_id": "bll8iq97cem8",
            "app_version": "2.73.1",
            "tokenType": 4,
            "gameBiz": "bbs_cn",
            "theme": "default",
            "business_url": "https://www.miyoushe.com/zzz/",
            "syncLoginStatus": True,
            "autotest": False,
            "lifecycle_id": ""
        }
    },
    "user_info": {
        "lang": "",
        "platform": "unknown",
        "device": "windows",
        "auth_key": "",
        "game_biz": "",
        "account_id": "",
        "game_uid": "",
        "game_region": "",
        "uuid": str(uuid.uuid4()),
        "device_id": ""
    },
    "event_info": {
        "eventCategory": "init",
        "eventAction": "call",
        "eventLabel": "",
        "eventValue": "",
        "timestamp": time_now(),
        "extra_info": {}
    },
    "type": "tool",
    "data_belong": "plat",
    "mia_session_id": "",
    "mia_session_step": "",
    "analysis_version": "v2"
}
params = execjs.compile(js_file).call('get_params', json.dumps(data, separators=(',', ':')))
data = json.dumps(data, separators=(',', ':'))
response = session.post(url, params=params, data=data)

session.headers.clear()
session.headers.update({
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://user.miyoushe.com",
    "Pragma": "no-cache",
    "Referer": "https://user.miyoushe.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-rpc-app_id": "bll8iq97cem8",
    "x-rpc-client_type": "4",
    "x-rpc-device_fp": "",
    "x-rpc-device_id": str(uuid.uuid4()),
    "x-rpc-device_model": "Chrome%20126.0.0.0",
    "x-rpc-device_name": "Chrome",
    "x-rpc-device_os": "Windows%2010%2064-bit",
    "x-rpc-game_biz": "bbs_cn",
    "x-rpc-lifecycle_id": "",
    "x-rpc-mi_referrer": "https://user.miyoushe.com/login-platform/index.html?app_id=bll8iq97cem8&theme=&token_type=4&game_biz=bbs_cn&message_origin=https%253A%252F%252Fwww.miyoushe.com&succ_back_type=message%253Alogin-platform%253Alogin-success&fail_back_type=message%253Alogin-platform%253Alogin-fail&ux_mode=popup&iframe_level=1#/login/password",
    "x-rpc-sdk_version": "2.28.0",
    "x-rpc-source": "v2.webLogin"
})
login_url = "https://passport-api.miyoushe.com/account/ma-cn-passport/web/loginByPassword"
login_data = {
    "account": execjs.compile(js_file).call('RSAEncrypt', '<USERNAME>'),
    "password": execjs.compile(js_file).call('RSAEncrypt', '<PASSWORD>'),
}
login_data = json.dumps(login_data, separators=(',', ':'))
login_response = session.post(login_url, data=login_data)

print(login_response.text)
