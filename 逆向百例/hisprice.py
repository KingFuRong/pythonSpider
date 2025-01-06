import json
import re
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import requests

with open('./hisprice.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
cookies = {
    "UMID": "ABWBDXQKWZISIZAROJV_HN_1736055808",
    "JM_SESSION_X": "1",
}
url = "https://www.hisprice.cn/dm/ptinfo.php"
params = {
    "ud": "ABWBDXQKWZISIZAROJV_HN_1736055808",
    "reqid": "7b6d444d7e7298fede7e40b41ff57ef0",
    "flg": "2",
    "cd": "ada35e4f5d7c1c555faa9732d3e1ea49P2ac9f5",
    "qt": "1736055813410",
    "zw": "da0e4dfa4d52c63b41b99a9dd37ef850",
    "fp": "4eacefb840e49f43f6da2a688b91794e",
    "fo": "d60b9e37d6b4f296a868b8518646b2b4",
    "rec": "600d0bf478353ff0e2a0dfef29b74e20"
}
data = {
    "checkCode": "",
    "con": "http://item.jd.com/100075069796.html"
}


response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
code = response.json()["code"]
print(response.text)
print(response)

url = "https://hs1.21sou.top/vv/dm/his_n.php"
params = {
    "code": code,
    "t": "",
    "ud": "ABWBDXQKWZISIZAROJV_HN_1736055808",
    "reqid": "7b6d444d7e7298fede7e40b41ff57ef0",
    "callback": "jQuery2240654152383865374_1736132256601",
    "_": "1736132256602"
}
response = requests.get(url, headers=headers, params=params)
enc_data = re.search('jQuery.*?\((.*?)\)', response.text).group(1)
enc_json = json.loads(enc_data)
print(enc_json['nd'])

price_data = execjs.compile(js_code).call("get_history_price", enc_json['nd'])
print(price_data)
