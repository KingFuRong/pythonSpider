import requests
import execjs
import re

with open('udc.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/9",
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

first_url = "https://match.yuanrenxue.cn/match/9"
url = "https://match.yuanrenxue.cn/api/match/9"
param = session.get(first_url)
time = re.search("\(decrypt,'(.*?)'\)", param.text).group(1)
ctx = execjs.compile(js_file).call('get_cookie', time)
cookies = {
    "m": f"{ctx}"
}
print(cookies)
response = session.get(url, headers=headers, cookies=cookies)
print(response.text)
print(response)
