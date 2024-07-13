import json
import re
from io import BytesIO

import requests

from Utils.tools import *

session = requests.Session()
session.cookies.clear()
session.headers.clear()
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
session.headers.update(headers)


def split_captcha(response):
    image = Image.open(BytesIO(response.content))

    bg_image = image.crop((0, 0, 240, 150))
    bg_image.save('./bg.png')
    slide_image = image.crop((0, 150, 240, 300))
    slide_image.save('./slide.png')


def cut_slide(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        image = image[y:y + h, x:x + w]

    cv2.imwrite('./slide.png', image)


def pass_captcha():
    captcha_url = "https://laowang.vip/captcha/tncode.php"
    captcha_params = {
        "t": "0.0923756200765189"
    }
    captcha_response = session.get(captcha_url, params=captcha_params)

    split_captcha(captcha_response)
    cut_slide("./slide.png")
    sliding_distance = find_location('./slide.png', './bg.png')

    check_url = "https://laowang.vip/captcha/check.php"
    check_params = {
        "tn_r": sliding_distance
    }
    check_response = session.get(check_url, params=check_params)
    if check_response.text.find('ok') != -1:
        return check_response.text
    else:
        return pass_captcha()


def login():
    session.cookies.clear()
    session.get('https://laowang.vip/forum.php')

    login_response = session.get('https://laowang.vip/member.php?mod=logging&action=login').text
    login_hash = re.search(r'loginhash=(.*?)"', login_response).group(1)
    form_hash = re.search(r'name="formhash" value="(.*?)"', login_response).group(1)

    clicaptcha_submit_info = pass_captcha()
    login_url = "https://laowang.vip/member.php"
    login_params = {
        "mod": "logging",
        "action": "login",
        "loginsubmit": "yes",
        "loginhash": login_hash,
        "inajax": "1"
    }
    login_data = {
        "formhash": form_hash,
        "referer": "https://laowang.vip/forum.php",
        "username": "ScorpioSR",
        "password": "61dd9902e2a0692566c87006d2d682ee",
        "questionid": "0",
        "answer": "",
        "cookietime": "2592000",
        "clicaptcha-submit-info": clicaptcha_submit_info
    }

    session.post(login_url, params=login_params, data=login_data)
    with open('./cookies/laowang.json', 'w') as f:
        f.write(json.dumps(session.cookies.get_dict()))


def check_login_status():
    with open('./cookies/laowang.json', 'r') as f:
        cookies = json.loads(f.read())
    session.cookies.update(cookies)
    login_status = session.get('https://laowang.vip/forum.php').text
    if login_status.find('ScorpioSR') != -1:
        pass
    else:
        login()


check_login_status()
sign_response = session.get('https://laowang.vip/sign.php').text
form_hash = re.search(r'formhash=(.*?)"', sign_response).group(1)
session.get('https://laowang.vip/plugin.php',
            params={"id": "k_misign:sign", "operation": "list", "inajax": "1", "ajaxtarget": "ranklist"})

session.get('https://laowang.vip/plugin.php',
            params={"id": "k_misign:sign", "operation": "qiandao", "formhash": form_hash, "format": "empty"})
clicaptcha_submit_info = pass_captcha()
temp = session.post('https://laowang.vip/plugin.php',
                    params={"id": "k_misign:sign", "operation": "qiandao", "formhash": form_hash, "format": "empty"},
                    data={"clicaptcha-submit-info": clicaptcha_submit_info}, allow_redirects=False)
print(temp.headers)
