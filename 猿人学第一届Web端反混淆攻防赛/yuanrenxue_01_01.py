import requests
import execjs

url = "https://match.yuanrenxue.cn/api/match/1"

with open('yuanrenxue_01_01.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

ctx = execjs.compile(js_file).call('request')

count = 0
for page in range(1, 6):
    params = {
        'page': f'{page}',
        'm': f'{ctx}',
    }

    response = requests.get(url, params=params).json()
    data = response['data']
    print(params)
    for value in data:
        count += int(value['value'])
print(count / 50)
