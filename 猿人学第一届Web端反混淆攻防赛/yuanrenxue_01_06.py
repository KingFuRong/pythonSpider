import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import requests

url = 'https://match.yuanrenxue.cn/api/match/6'

with open('yuanrenxue_01_06.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/6",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

cookies = {
    "sessionid": "ltn8jnmvv5tlw00tq1d6i6lyipqh6ffz",
    "no-alert3": "true",
}
result = []
for page in range(1, 6):
    ctx = execjs.compile(js_file).call('run', page)
    params = {
        "page": f"{page}",
        "m": f"{ctx['m']}",
        "q": f"{page}-{ctx['t']}|"
    }
    # 发送GET请求
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.json())
    data = response.json()
    result.extend([i['value'] for i in data.get('data')])
sum_ = sum(result) * 24
print(sum_)
