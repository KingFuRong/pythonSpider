import json

import requests
import execjs

with open('./空气质量在线检测分析平台.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.aqistudy.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.aqistudy.cn/html/city_realtime.php?v=2.3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
data = execjs.compile(js_file).call('get_params', "GETDATA", '成都')

encode_data = requests.post('https://www.aqistudy.cn/apinew/aqistudyapi.php', data=data, headers=headers)

decode_date = execjs.compile(js_file).call('decode', encode_data.text)

json_data = json.loads(decode_date)

formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)

# 打印格式化后的 JSON
print(formatted_json)
