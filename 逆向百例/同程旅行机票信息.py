import subprocess  # 执行命令行的
from functools import partial  # 固定某个参数的
from urllib.parse import quote

import requests

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import json

# ==================== ⇣ 航班查询相关参数 ⇣ ====================
FlyOffCity = '维捷布斯克机场'
ArriveCity = '虹桥机场'
FlyOffTime = '2024-07-26'  # 格式 2024-07-05
Departure = 'VTB'  # 格式 PEK
Arrival = 'SHA'  # 格式 SHA
FlyOffCityUrlEncode = quote(FlyOffCity).strip()  # 起飞城市url encode
ArriveCityUrlEncode = quote(ArriveCity).strip()  # 目的城市url encode
# ==================== ↑ 航班查询相关参数 ↑ ====================
# ==================== ⇣ 清除自带请求头和cookies ⇣ ====================
session = requests.Session()
session.headers.clear()
session.cookies.clear()
# ==================== ↑ 清除自带请求头和cookies ↑ ====================
# ==================== ⇣ 获取关键加密参数 ⇣ ====================
with open('./同程旅行机票.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

js_file = js_file.replace('起飞城市三字码', Departure)
js_file = js_file.replace('目的城市三字码', Arrival)
js_file = js_file.replace('起飞城市UrlEncode', FlyOffCityUrlEncode)
js_file = js_file.replace('目的城市UrlEncode', ArriveCityUrlEncode)
js_file = js_file.replace('起飞城市', FlyOffCity)
js_file = js_file.replace('目的城市', ArriveCity)
js_file = js_file.replace('航班日期', FlyOffTime)

user_dun = execjs.compile(js_file).call('run')
# print(user_dun['value'])
# ==================== ↑ 获取关键加密参数 ↑ ====================
headers = {
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "tcplat": "1",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "tcuserid": "",
    "content-type": "application/json;charset=UTF-8",
    # "tcversion": "1.1.0",
    # "accept": "application/json, text/plain, */*",
    # "refid": "0",
    "Referer": f"https://www.ly.com/flights/itinerary/oneway/{Departure}-{Arrival}?date={FlyOffTime}&from={FlyOffCityUrlEncode}&to={ArriveCityUrlEncode}&fromairport=&toairport=&p=&childticket=0,0",
    # "tcsectoken": "",
    "user-dun": user_dun['value'],
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.ly.com/flights/api/getflightlist"
data = {
    "Departure": Departure,
    "Arrival": Arrival,
    "GetType": "1",
    "QueryType": "1",
    "fromairport": "",
    "toairport": "",
    "DepartureDate": FlyOffTime,
    "DepartureName": FlyOffCity,
    "ArrivalName": ArriveCity,
    "IsBaby": 0,
    "paging": {
        "dataflag": "all"
    },
    "DepartureFilter": "",
    "ArrivalFilter": "",
    "flat": 1,
    "plat": 1,
    "isFromKylin": 1,
    "refid": "0"
}
data = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
data = data.encode("utf-8")

# Fiddler调试接口
proxies = {
    "http": "http://127.0.0.1:9999",
    "https": "http://127.0.0.1:9999",
}
session.headers.update(headers)
response = session.post(url, data=data)

response_data = response.json()
print(response_data)

# ==================== ⇣ 数据解析 ⇣ ====================
base_info = response_data['body']
FlyOffCity = base_info['FlyOffCity']  # 起飞城市
ArriveCity = base_info['ArriveCity']  # 目的城市
FlyOffTime = base_info['FlyOffTime']  # 起飞日期
week = base_info['week']  # 星期
FlightNum = base_info['FlightNum']  # 航班总数

FlightInfoSimpleList = base_info['FlightInfoSimpleList']
for FlightInfo in FlightInfoSimpleList:
    oapname = FlightInfo['oapname']  # 出发机场
    aapname = FlightInfo['aapname']  # 目的机场
