import execjs
import requests

with open('yuanrenxue_01_15.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/15",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "y3dfah7nq9eczlicy6ts2pr9j6ure53y",
    "no-alert3": "true"
}
url = "https://match.yuanrenxue.cn/api/match/15"

count = 0
for page in range(1, 6):
    ctx = execjs.compile(js_file).call('get_m')
    params = {
        "m": f"{ctx}",
        "page": f"{page}"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data = response.json()['data']
    for value in data:
        count += value['value']

print(count)
