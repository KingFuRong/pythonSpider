import re
import execjs

import requests

def login():
    data = {
        'username': 'ScorpioSpider',
        'password': 'UM4Zppk5NmE.m'
    }
    session.post('https://match.yuanrenxue.cn/api/login', data=data)
    session.get('https://match.yuanrenxue.com/api/loginInfo')

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/14",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
session = requests.Session()

login()

count = 0

for page in range(1, 6):
    url_key = "https://match.yuanrenxue.cn/api/match/14/m"
    response_key = session.get(url_key, headers=headers)

    enc_array = re.search("var \$_0x\w{4}=(.*?);", response_key.text).group(1)
    offset = re.search("\(\$_0x\w{4},(.*?)\)", response_key.text).group(1)

    param_key = re.findall("window\[(.*?)';", response_key.text)
    if len(param_key) == 2:
        v14 = "window[" + param_key[0] + "';"
        v142 = "window[" + param_key[1] + "';"
    else:
        param_key = param_key[0].split(";")
        v14 = "window[" + param_key[0] + ";"
        v142 = param_key[-1] + "';"
    old_param = re.search("\$_0x\w{4}", v14)[0]
    v14 = v14.replace(old_param, '$_0x3d67')
    v142 = v142.replace(old_param, '$_0x3d67')

    with open('yuanrenxue_01_14_getKey.js', 'r', encoding='utf-8') as f:
        js_key = f.read()

    get_key = execjs.compile(js_key).call('get_key', enc_array, offset, v14, v142)
    with open('yuanrenxue_01_14.js', 'r', encoding='utf-8') as f:
        js_cookie = f.read()

    get_cookie = execjs.compile(js_cookie).call('sp', get_key['v14'], get_key['v142'], page)

    url_value = "https://match.yuanrenxue.cn/api/match/14"
    cookies = {
        'm': get_cookie['m'],
        'mz': get_cookie['mz'],
    }
    params = {
        "page": f'{page}'
    }

    response_value = session.get(url_value, cookies=cookies, headers=headers, params=params)
    for value in response_value.json()['data']:
        count += value['value']

print(count)
