import requests
import execjs

with open('yuanrenxue_01_18.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

mouses_start = 656  # 页数起始纵坐标位置
interval = 52       # 两个页数按钮之间间隔的距离

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/18",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

cookies = {
    "sessionid": "y3dfah7nq9eczlicy6ts2pr9j6ure53y",
    "qpfccr": "true",
    "no-alert3": "true"
}

url = "https://match.yuanrenxue.cn/match/18data"
count = 0

for page in range(1, 6):
    mouse = str(mouses_start + (page - 1) * interval)
    mouses = str(page) + '|' + mouse + 'm300,' + mouse + 'm300,' + mouse + 'm300,' + mouse + 'd300,' + mouse + 'u300'
    ctx = execjs.compile(js_file).call('get_v', mouses)
    params = {
        "page": f"{page}",
        "t": f"{ctx['t']}",
        "v": f"{ctx['v']}"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data = response.json()['data']
    for value in data:
        count += value['value']
print(count)
