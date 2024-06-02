import requests
import execjs

with open('天翼云登录.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

ctx = execjs.compile(js_file).call('get_params', '邮箱', '密码')

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://m.ctyun.cn",
    "Pragma": "no-cache",
    "Referer": "https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-riskdevicesign": "26e076d268467ead6183f8d57b2e008d"
}
url = "https://m.ctyun.cn/account/login"
params = {
    "referrer": "wap",
    "mainVersion": f"{ctx['mainVersion']}",
    "comParam_curTime": f"{ctx['comParam_curTime']}",
    "comParam_seqCode": f"{ctx['comParam_seqCode']}",
    "comParam_signature": f"{ctx['comParam_signature']}",
    "isCheck": "true",
    "locale": "zh-cn"
}
data = {
    "userName": f"{ctx['username']}",
    "password": f"{ctx['password']}",
}
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)
