import requests
import execjs

with open('yuanrenxue_01_02.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

count = 0
for page in range(1, 6):
    ctx = execjs.compile(js_file).call('get_m')

    cookies = {
        'sessionid': 'ltn8jnmvv5tlw00tq1d6i6lyipqh6ffz',
        'm': f'{ctx}',
        'qpfccr': 'true',
        'no-alert3': 'true',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'sessionid=ltn8jnmvv5tlw00tq1d6i6lyipqh6ffz; m=0c8dd9d13e45d116bd52a3644fa910e3|1712566811000; qpfccr=true; no-alert3=true',
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.cn/match/2',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'page': f'{page}',
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/2', params=params, cookies=cookies,
                            headers=headers).json()
    data = response['data']
    for value in data:
        count += int(value['value'])
print(count)
