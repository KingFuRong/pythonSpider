import requests
import execjs

with open('yuanrenxue_01_05.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

url = "https://match.yuanrenxue.cn/api/match/5"
session = requests.session()

for page in range(1, 6):
    ctx = execjs.compile(js_file).call('get_cookie')
    cookies = {
        "sessionid": "ouayegutflgm3pzbcyf839gd2xs2xkzx",
        "no-alert3": "true",
        "m": f"{ctx['m']}",
        "RM4hZBv0dDon443M": f"{ctx['RM4hZBv0dDon443M']}",
    }
    params = {
        "page": page,
        "m": ctx['param_m'],
        "f": ctx['param_f']
    }
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    print(cookies)
    print(response.url)
    print(response)
