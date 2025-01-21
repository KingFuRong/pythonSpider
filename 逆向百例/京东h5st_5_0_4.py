import base64
import datetime
import hashlib
import json
import random
import re
import string
import struct
import time

from curl_cffi import requests

JD_PARAMS = {
    "fp_key": "qw3pa2mn87",
    "fp_choice": 5,
    "fp_slice": 2,
    "fp_max": 16,
    "first_key": "U=",
    "second_key": "%Io1mj_wq%@S",
    "slice_index": 14,
    "cut_index": 8,
    "salt": "D8<NCk",
    "version": "5.0",
    "v": "h5_file_v5.0.4",
    'dtime_append': '69'
}

PAGE_PARAMS = {
    "url": "https://item.jd.com/10119559349249.html",
    "og": "https://item.jd.com",
}


def process_string(text, slice_index, cut_index=None):
    if cut_index:
        return (''.join([text[i] + text[i + 1] for i in range(0, slice_index, 2)][::-1]) + text[slice_index:])[:cut_index]
    else:
        return ''.join([text[i] + text[i + 1] for i in range(0, slice_index, 2)][::-1]) + text[slice_index:]


def custom_base64_encode(text, new_table="ZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvutsrqponmlkjihgfedcba"):
    reverse_string = text + ''.join(chr(3 - len(text) % 3) for _ in range(3 - len(text) % 3))
    ciphertext_base64_bytes = base64.b64encode(reverse_string.encode('latin1'))
    ciphertext = ciphertext_base64_bytes.decode()
    raw_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    dictionary_decode = str.maketrans(new_table, raw_table)
    dictionary_encode = dict(zip(dictionary_decode.values(), dictionary_decode.keys()))
    new_result_b64 = ciphertext.translate(dictionary_encode)
    return new_result_b64


def get_key_salt(key):
    salt_map = 'dcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvutsrqponmlkjihgfe'
    tk_len = len(key)
    tk_slice = int(tk_len / 6)
    tk_salt = str()
    salt_index = 0

    for index in range(0, 6):
        if index == 5:
            for slice_index in range(0, tk_slice + tk_len % 6):
                if index * tk_slice + slice_index < tk_len:
                    salt_index += ord(key[index * tk_slice + slice_index])
        else:
            for slice_index in range(0, tk_slice):
                if index * tk_slice + slice_index < tk_len:
                    salt_index += ord(key[index * tk_slice + slice_index])
        salt_index *= 25
        salt_index %= 64
        tk_salt += salt_map[salt_index]
        salt_index = 0

    return tk_salt


def get_fingerprint(JD_PARAMS):
    fp_key = JD_PARAMS['fp_key']
    fp_choice = JD_PARAMS['fp_choice']
    fp_slice = JD_PARAMS['fp_slice']
    fp_max = JD_PARAMS['fp_max']

    base36_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    fp_key_len = len(fp_key)
    fp_list = list()
    fp_first = str()
    for index in range(0, fp_key_len):
        if len(fp_list) == fp_choice:
            break
        if (random.random() * (fp_key_len - index)) < fp_choice - len(fp_list):
            fp_list.append(fp_key[index])

    for index in range(0, fp_choice):
        index_key = int(random.random() * (fp_choice - index))
        fp_first += fp_list[index_key]
        fp_list[index_key] = fp_list[fp_choice - index - 1]

    fp_random = random.randint(0, 10)
    fp_second = ''.join(random.choices(''.join(fp_str for fp_str in fp_key if fp_str not in fp_first), k=fp_random))
    fp_third = ''.join(random.choices(''.join(fp_str for fp_str in fp_key if fp_str not in fp_first),
                                      k=fp_max - fp_choice - fp_random - 1))

    fp = list(fp_second + fp_first + fp_third + str(fp_random))

    for fp_index in range(len(fp) - fp_slice - 1, -1, -1):
        fp[fp_index] = base36_digits[35 - int(fp[fp_index], 36)]

    fp = ''.join(fp[:-fp_slice][::-1] + fp[-fp_slice:])
    return fp


def get_token(JD_PARAMS, fp):
    first_key = JD_PARAMS['first_key']
    second_key = JD_PARAMS['second_key']
    salt = JD_PARAMS['salt']

    def int_to_little_endian_bytes(num, length=8):
        return list(struct.pack('<Q', num)[:length])

    def get_expr():
        random_mode_max = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=32))
        choice_num = random.randint(0, 3) + 2
        expr = str()

        for index in range(0, choice_num):
            expr += random.choice(['1', '2', '3'])
            if index < choice_num - 1:
                expr += random.choice(['+', 'x'])

        expr += random_mode_max[0:9 - len(expr)]
        expr = base64.b64encode(expr.encode('latin1')).decode("latin1").replace('+', '-').replace('/', '_').replace("=",
                                                                                                                    "")

        return expr

    def get_cipher():
        timestamp = int(time.time() * 1000)
        endian_timestamp = ''.join(chr(chars) for chars in int_to_little_endian_bytes(timestamp))
        enc_text = hashlib.new('md5', (first_key + second_key + endian_timestamp + fp).encode('latin1')).hexdigest()
        enc_text = process_string(enc_text, 14, 8)
        return custom_base64_encode(enc_text + first_key + second_key + endian_timestamp + fp)[::-1]

    tk_expr = get_expr()
    tk_cipher = get_cipher()
    fake_tk = 'tk04w41l' + tk_expr + tk_cipher
    fake_tk += get_key_salt(fake_tk) + salt
    fake_tk_enc = process_string(hashlib.new('md5', fake_tk.encode('latin1')).hexdigest(), 14, 8)
    real_tk = 'tk04w' + fake_tk_enc + '41l' + tk_expr + tk_cipher

    return real_tk


def get_token_and_algo(JD_PARAMS, PAGE_PARAMS, user_agent, fp):
    w = random.randint(300, 500)
    h = random.randint(600, 900)
    av = user_agent.replace("Mozilla/", "")
    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_params = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=11))
    env = json.dumps({
        "wc": 0,
        "wd": 0,
        "l": "en-US",
        "ls": "en-US",
        "ml": 2,
        "pl": 5,
        "av": av,
        "ua": user_agent,
        "sua": sua,
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 5,
            "wk": 0,
            "bu1": "0.1.9",
            "bu10": 4,
            "bu2": 0,
            "bu3": 102,
            "bu4": 0,
            "bu5": 0,
            "bu6": 31,
            "bu7": 0,
            "bu8": 0
        },
        "pp1": "",
        "bu1": "",
        "w": w,
        "h": h,
        "ow": w,
        "oh": h,
        "url": PAGE_PARAMS['url'],
        "og": PAGE_PARAMS['og'],
        "pf": "Win32",
        "pr": 1.25,
        "re": "https://www.jd.com/",
        "random": random_params,
        "referer": "https://www.jd.com/",
        "v": JD_PARAMS['v'],
        "bu2": "    at https://storage.360buyimg.com/webcontainer/main/js_security_v3_main_0.1.8.js?v=20250120:5:76057",
        "bu3": "function Window() { [native code] }$function toString() { [native code] }",
        "canvas": "3e355732be2913f536614a5e3b47cffe",
        "canvas1": "3e355732be2913f536614a5e3b47cffe",
        "webglFp": "e50b33f5cfee87d5c19654d85be2c1f0",
        "webglFp1": "e50b33f5cfee87d5c19654d85be2c1f0",
        "ccn": 16,
        "ai": PAGE_PARAMS['api_id'],
        "fp": fp,
        "wk": 0
    }, indent=2)
    extend_params = custom_base64_encode(env)[::-1]

    headers = {
        "sec-ch-ua-platform": "\"Windows\"",
        "Referer": "https://item.jd.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "accept": "application/json",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?0"
    }
    url = "https://cactus.jd.com/request_algo"
    data = {
        "version": JD_PARAMS['version'],
        "fp": fp,
        "appId": PAGE_PARAMS['api_id'],
        "timestamp": int(time.time() * 1e3),
        "platform": "web",
        "expandParams": extend_params,
        "fv": JD_PARAMS['v'],
        "localTk": get_token(JD_PARAMS, fp),
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    token = response.json()["data"]["result"]["tk"]
    algo = response.json()["data"]["result"]["algo"]
    return token, algo


def get_h5st(JD_PARAMS, PAGE_PARAMS, user_agent, fp, token, algo, t):
    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_params = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=11))
    env = {
        "sua": sua,
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 5,
            "wk": 0,
            "bu1": "0.1.9",
            "bu10": 4,
            "bu2": -2,
            "bu3": 84,
            "bu4": 0,
            "bu5": 0,
            "bu6": 41,
            "bu7": 0,
            "bu8": 0
        },
        "pf": "Win32",
        "random": random_params,
        "v": JD_PARAMS['v'],
        "canvas": "3e355732be2913f536614a5e3b47cffe",
        "webglFp": "e50b33f5cfee87d5c19654d85be2c1f0",
        "ccn": 16,
        "fp": fp,
        "bu1": "0.1.8"
    }

    date_now = datetime.datetime.now()
    format_date = date_now.strftime("%Y%m%d%H%M%S%f")[:-3]
    timestamp = str(int(datetime.datetime.timestamp(date_now) * 1e3))
    rd = re.search(r"rd=.(.*?).;", algo).group(1)

    key = f'{token}{fp}{format_date}{JD_PARAMS["dtime_append"]}{PAGE_PARAMS["api_id"]}{rd}'
    key += get_key_salt(key) + JD_PARAMS["salt"]
    key = process_string(hashlib.new('md5', key.encode('latin1')).hexdigest(), JD_PARAMS['slice_index'])
    body = json.dumps(PAGE_PARAMS['body'], separators=(",", ":"), ensure_ascii=False)
    body_str = hashlib.new('sha256', body.encode('latin1')).hexdigest()

    first_text = f'{key}appid:{PAGE_PARAMS["appid"]}&body:{body_str}&client:{PAGE_PARAMS["client"]}&clientVersion:{PAGE_PARAMS["client_version"]}&functionId:{PAGE_PARAMS["function_id"]}&t:{t}{key}'
    first_text += get_key_salt(first_text) + JD_PARAMS["salt"]
    first_sign = process_string(hashlib.new('md5', first_text.encode('latin1')).hexdigest(), JD_PARAMS['slice_index'])

    second_text = f'{key}appid:{PAGE_PARAMS["appid"]}&functionId:{PAGE_PARAMS["function_id"]}{key}'
    second_text += get_key_salt(second_text) + JD_PARAMS["salt"]
    second_sign = process_string(hashlib.new('md5', second_text.encode('latin1')).hexdigest(), JD_PARAMS['slice_index'])
    env_info_enc = custom_base64_encode(json.dumps(env, indent=2))[::-1]

    h5st = f'{format_date};{fp};{PAGE_PARAMS["api_id"]};{token};{first_sign};{JD_PARAMS["version"]};{timestamp};{env_info_enc};{second_sign}'
    return h5st

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
PAGE_PARAMS['appid'] = "item-v3"
PAGE_PARAMS['api_id'] = "fb5df"
PAGE_PARAMS['client'] = "pc"
PAGE_PARAMS['client_version'] = "1.0.0"
PAGE_PARAMS['function_id'] = "pc_club_productPageComments"
PAGE_PARAMS['body'] = {"productId":10119559349249,"score":0,"sortType":5,"page":0,"pageSize":10,"isShadowSku":0,"fold":1,"bbtf":"","shield":""}

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=gbk",
    "origin": "https://item.jd.com",
    "user-agent": user_agent,
}
url = "https://api.m.jd.com/"

ctime = int(time.time() * 1000)
fp = get_fingerprint(JD_PARAMS)
token, algo = get_token_and_algo(JD_PARAMS, PAGE_PARAMS, user_agent, fp)

h5st = get_h5st(JD_PARAMS, PAGE_PARAMS, user_agent, fp, token, algo, ctime)
print(h5st)

params = {
    "appid": "item-v3",
    "functionId": "pc_club_productPageComments",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": ctime,
    "body": json.dumps(PAGE_PARAMS['body'], separators=(",", ":")),
    "h5st": h5st,
    "loginType": "3",
}

response = requests.get(url, headers=headers, params=params)
print(response.text)
print(response)
