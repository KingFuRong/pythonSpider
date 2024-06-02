import execjs
import requests

session = requests.Session()

get_id_request = session.get('https://passport.yhd.com/passport/login_input.do')

with open('一号店_captchaToken.js', 'r', encoding='utf-8') as f:
    js_file = f.read()

ctx = execjs.compile(js_file).call('get_captchaToken')

session.cookies.update({'_c_id': ctx['_c_id'], '_s_id': ctx['_s_id'], ctx['_s_id']: '249'})

login_params = {
    'credentials.username': ctx['credentials.username'],
    'credentials.password': ctx['credentials.password'],
    'sig': '',
    'is_jab': 'true',
    'captchaToken': ctx['captchaToken'],
    'jab_st': '1',
    'loginSource': '1',
    'returnUrl': 'http://www.yhd.com',
    'isAutoLogin': '0',
    'slideData': '',
}

login_response = session.post('https://passport.yhd.com/publicPassport/login.do', params=login_params)
print(login_response.text)
print(requests.utils.dict_from_cookiejar(session.cookies))
