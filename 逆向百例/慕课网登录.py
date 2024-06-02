import requests
import execjs
from Utils.tools import *
import ddddocr

username = '18966666666'
password = '123456'

with open('./慕课网登录.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
ocr = ddddocr.DdddOcr(show_ad=False)
session = requests.Session()
url = 'https://class.imooc.com/'
session.get(url)
session.get('https://coding.imooc.com/passport/static/scripts/ssologin.js?v=2.0')
session.cookies.update({'sensorsdata2015jssdkcross': execjs.compile(js_file).call('get_sensorsdata2015jssdkcross')})

login_url = "https://class.imooc.com/passport/user/login"
login_data = {
    "username": "18933666666",
    "password": execjs.compile(js_file).call('enc_password', password),
    "verify": "",
    "remember": "1",
    "pwencode": "1",
    "browser_key": execjs.compile(js_file).call('get_browser_key'),
    "referer": "https://class.imooc.com"
}

verifycode_url = f"https://class.imooc.com/passport/user/verifycode?t={time_now()}"
session.headers.update({"referer": "https://class.imooc.com/"})

download_img(session, './verifycode', verifycode_url)
verifycode_pic = open("verifycode.jpg", "rb").read()
verifycode_result = ocr.classification(verifycode_pic)

login_data['verify'] = verifycode_result

login_response = session.post(login_url, data=login_data)

print(login_response.text)
print(login_response)
