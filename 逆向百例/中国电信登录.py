import requests
import execjs
from Utils.tools import *

with open('中国电信登录.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

username = '用户名'
passowrd = '服务密码'
session = requests.Session()

# ==================== 模拟登录，初始化cookies ====================
session.get('https://login.189.cn/web/login')
session.get('https://www.189.cn/jt/loginpic/')
# ==================== 访问ajax，获取SM2加密公钥 ====================
pubkey = session.post('https://login.189.cn/web/login/ajax', data={'m': 'getPubKey'})
pubkey = pubkey.text
# ==================== 再次访问ajax，获取provinceId ====================
provinceId_responese = session.post('https://login.189.cn/web/login/ajax', data={'m': 'checkphone', 'phone': username})
provinceId_dict = provinceId_responese.json()
provinceId = provinceId_dict['provinceId']
# ==================== 调用js，生成cookies参数 ====================
js_file = js_file.replace('SM2国密公钥', f'"{pubkey}"')
zhizhendata2015jssdkcross = execjs.compile(js_file).call('get_zhizhendata2015jssdkcross')
session.cookies.update({'zhizhendata2015jssdkcross': zhizhendata2015jssdkcross})
session.cookies.update({'sajssdk_2015_cross_new_user': '1'})
# ==================== 调用js，获取服务密码密文 ====================
uPwd = execjs.compile(js_file).call('sm2Encrypt', passowrd, pubkey, 0)
# ==================== 访问validate，验证密码 ====================
vaildate_url = 'https://login.189.cn/web/pwd/validate'
vaildate_data = {
    "uName": username,
    "uType": "201",
    "uPwd": uPwd,
    "isRandomPwd": "false"
}
vaildate_response = session.post(vaildate_url, data=vaildate_data)
# ==================== 模拟绕过滑块，获取cookies参数 ====================
checkcapcode = 0
while checkcapcode != 1:
    captcha_url = 'https://login.189.cn/web/getPic'
    captcha_response = session.post(captcha_url)
    captcha_dict = captcha_response.json()

    capcode = captcha_dict['capcode']
    slidingImage = base64_to_image(captcha_dict['slidingImage'], 'slidingImage.jpg')
    backImage = base64_to_image(captcha_dict['backImage'], 'backImage.jpg')

    sliding_distance = find_location('./slidingImage.jpg', './backImage.jpg')

    checkcapcode_url = 'https://login.189.cn/web/checkcapcode'
    checkcapcode_data = {
        'xpos': sliding_distance,
        'capcode': capcode,
        'phonekey': username,
        'slidingType': 'login_sliding'
    }
    checkcapcode_response = session.post(checkcapcode_url, data=checkcapcode_data)
    checkcapcode_dict = checkcapcode_response.json()
    checkcapcode = checkcapcode_dict['code']
# ==================== 已获取全部参数，尝试登录 ====================
login_url = 'https://login.189.cn/web/login'
login_data = {
    "Account": username,
    "UType": "201",
    "ProvinceID": provinceId,
    "AreaCode": "",
    "CityNo": "",
    "RandomFlag": "0",
    "Password": uPwd,
    "ZQFromFlag": ""
}
# allow_redirects=False 防止重定向导致Location丢失
login_response = session.post(login_url, data=login_data, allow_redirects=False)

next_jump_url = login_response.headers.get('Location')

while next_jump_url is not None:
    next_jump_response = session.get(next_jump_url, allow_redirects=False)
    next_jump_url = next_jump_response.headers.get('Location')

# 成功输出个人信息，登录成功
print(session.get('https://www.189.cn/login/index.do').text)
