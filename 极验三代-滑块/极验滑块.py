import re
import execjs
import requests

from Utils.tools import *

session = requests.Session()
session.headers['User-Agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/124.0.0.0 Safari/537.36')

# ==================== 第一次请求,注册验证码 ====================
regist_url = f'https://www.geetest.com/demo/gt/register-slide?t={time_now()}'
regist_response = session.get(regist_url)
regist_dict = regist_response.json()
challenge = regist_dict['challenge']
gt = regist_dict['gt']

# ==================== 第二次请求,访问gettype ====================
get_type_url = 'https://apiv6.geetest.com/gettype.php'
get_type_params = {
    'gt': gt,
    'callback': f'geetest_{time_now()}'
}
get_type_response = session.get(get_type_url, params=get_type_params)
# ==================== 第三次请求,首次访问get.php ====================
with open('极验滑块_first_w_params.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
first_get_params_dict = execjs.compile(js_file).call('first_get_params', gt, challenge)

first_get_url = 'https://api.geetest.com/get.php'
first_get_params = {
    'gt': first_get_params_dict['gt'],
    'challenge': first_get_params_dict['challenge'],
    'lang': first_get_params_dict['lang'],
    'pt': first_get_params_dict['pt'],
    'client_type': first_get_params_dict['client_type'],
    'w': first_get_params_dict['w'],
    'callback': f'geetest_{time_now()}'
}

aeskey = first_get_params_dict['aeskey']
fingerprint = first_get_params_dict['fingerprint']

first_get_response = session.get(first_get_url, params=first_get_params)

param_s = re.search('"s": "(.*?)",', first_get_response.text).group(1)
# ==================== 第四次请求,访问ajax.php ====================
with open('极验滑块_second_w_params.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
ajax_params_w = execjs.compile(js_file).call('second_get_params', gt, challenge, aeskey, param_s, fingerprint, "''")

ajax_url = 'https://api.geetest.com/ajax.php'
ajax_params_dict = {
    'gt': gt,
    'challenge': challenge,
    'lang': 'zh-cn',
    'pt': '0',
    'client_type': 'web',
    'w': ajax_params_w,
    'callback': f'geetest_{time_now()}'
}

ajax_response = session.get(ajax_url, params=ajax_params_dict)
# ==================== 第五次请求,再次访问get.php ====================
second_get_url = "https://api.geetest.com/get.php"
second_get_params = {
    "is_next": "true",
    "type": "slide3",
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "https": "true",
    "protocol": "https://",
    "offline": "false",
    "product": "popup",
    "api_server": "api.geetest.com",
    "isPC": "true",
    "autoReset": "true",
    "width": "100%",
    "callback": f'geetest_{time_now()}'
}

second_get_response = session.get(first_get_url, params=second_get_params)
second_get_text = second_get_response.text

static_url = 'https://static.geetest.com/'
id = re.search('"id": "(.*?)"', second_get_text).group(1)
background_img = re.search('"bg": "(.*?)"', second_get_text).group(1)
full_background_img = re.search('"fullbg": "(.*?)"', second_get_text).group(1)
slice_img = re.search('"slice": "(.*?)"', second_get_text).group(1)
new_challenge = re.search('"challenge": "(.*?)"', second_get_text).group(1)
new_param_s = re.search('"s": "(.*?)",', second_get_text).group(1)
# ==================== 处理数据,下载并还原滑块图片 ====================
download_img(session, 'bg', static_url + background_img)
download_img(session, 'fullbg', static_url + full_background_img)
download_img(session, 'slice', static_url + slice_img)

revert_img('fullbg.jpg')
revert_img('bg.jpg')
# ==================== 处理数据,计算滑块位置和轨迹 ====================
slice_distance = find_location('./slice.jpg', './new_bg.jpg')
slide_track, slice_time = get_slide_track(slice_distance)
print(slice_distance, slice_time)
print(slide_track)
print(param_s, new_param_s)
# ==================== 第六次请求,再次访问ajax.php ====================
with open('极验滑块_third_w_params.js', 'r', encoding='utf-8') as f:
    js_file = f.read()
second_ajax_paramas_dict = execjs.compile(js_file).call('third_w_params', gt, new_challenge, id, background_img,
                                                        full_background_img, slice_img, new_param_s, slice_distance,
                                                        slide_track, slice_time)

second_ajax_url = 'https://api.geetest.com/ajax.php'
second_ajax_params = second_ajax_paramas_dict
second_ajax_params['callback'] = f'geetest_{time_now()}'

second_ajax_response = session.get(second_ajax_url, params=second_ajax_params)
second_ajax_text = second_ajax_response.text
print(second_ajax_text)
