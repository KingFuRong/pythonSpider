import base64
import datetime
import hashlib
import json
import hmac
import random
import re
import string
import struct
import time

import requests


def custom_base64_encode(string):
    reverse_string = string + ''.join(chr(3 - len(string) % 3) for i in range(3 - len(string) % 3))
    ciphertext_base64_bytes = base64.b64encode(reverse_string.encode('latin1'))
    ciphertext = ciphertext_base64_bytes.decode()
    raw_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    new_table = "rqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvuts"
    dictionary_decode = str.maketrans(new_table, raw_table)  # 创建字符映射关系 用于base64decode
    dictionary_encode = dict(zip(dictionary_decode.values(), dictionary_decode.keys()))
    new_result_b64 = ciphertext.translate(dictionary_encode)
    return new_result_b64[::-1]

def finger_print_4_9_1(key='z4rekl9i1u'):
    def encode_finger_print(string):
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        return ''.join([chars[35 - chars.index(char)] for char in string])

    middle_original_text = ''.join(random.sample(key, 4))
    temp_key = ''.join([char for char in key if char not in middle_original_text])
    random_num = random.randint(0, 9)
    front_original_text = ''.join(random.choice(temp_key) for _ in range(random_num))
    back_original_text = ''.join(random.choice(temp_key) for _ in range(12 - random_num - 1))
    original_text = front_original_text + middle_original_text + back_original_text + str(random_num)

    return encode_finger_print(original_text[0:8][::-1]) + original_text[8:16]

def browser_environment(environment_dict):
    environment_json = json.dumps(environment_dict, indent=2)
    return custom_base64_encode(environment_json)

def real_token_4_9_1(fp, api_appid):
    environment_dict = {
        "wc": 0,
        "wd": 0,
        "l": "zh-CN",
        "ls": "zh-CN",
        "ml": 2,
        "pl": 5,
        "av": "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "sua": "Macintosh; Intel Mac OS X 10_15_7",
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 5,
            "wk": 0,
            "bu1": "0.1.9",
            "bu2": 0,
            "bu3": 75,
            "bu4": 0,
            "bu5": 0,
            "bu6": 31,
            "bu7": "",
            "bu8": 0
        },
        "pp1": "",
        "bu1": "",
        "w": 1440,
        "h": 900,
        "ow": 1440,
        "oh": 808,
        "url": 'https://item.jd.com/100105177369.html',
        "og": 'https://item.jd.com',
        "pf": "MacIntel",
        "pr": 2,
        "re": "https://www.jd.com/",
        "random": ''.join(random.choice(string.ascii_letters + '_-') for _ in range(11)),
        "referer": "https://www.jd.com/",
        "v": "h5_file_v4.8.1",
        "bu2": "    at r (https://h5static.m.jd.com/act/jd-jssdk/latest/jd-jssdk.min.js:1:93837)",
        "canvas": "8ed4464d02c680d9290f4da1d59154b0",
        "canvas1": "8ed4464d02c680d9290f4da1d59154b0",
        "webglFp": "",
        "webglFp1": "63e81c90ebaeb6ef7f30f966f5ad027c",
        "ccn": 8,
        "ai": api_appid,
        "fp": fp
    }
    expand_params = browser_environment(environment_dict=environment_dict)
    tk = token_4_9_1(fp)

    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://item.jd.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://item.jd.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    url = "https://cactus.jd.com/request_algo"
    data = {
        "version": "4.9",
        "fp": fp,
        "appId": api_appid,
        "timestamp": int(time.time() * 1e3),
        "platform": "web",
        "expandParams": expand_params,
        "fv": "h5_file_v4.9.1",
        "localTk": tk
    }
    data = json.dumps(data, separators=(',', ':'))
    result = requests.post(url, headers=headers, data=data).json()['data']['result']

    return result['tk'], result['algo']

def token_4_9_1(fp, first_key="ba", second_key="qodOHbSV1ik2", salt="x38rG0"):
    def random_mode_max():
        return ''.join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(32))

    def int_to_little_endian_bytes(num, length=8):
        return list(struct.pack('<Q', num)[:length])

    part_one = random_mode_max()
    part_two = random.choice(['1', '2', '3']) + ''.join(random.choice(['+', 'x']) + random.choice(['1', '2', '3']) for _ in range(random.randint(1, 4)))
    part_three = part_two + part_one[0:9 - len(part_two)]
    enc_part_one = base64.b64encode(part_three.encode()).decode('utf-8')

    part_four = int_to_little_endian_bytes(int(time.time() * 1000))
    part_five = first_key + second_key + ''.join(chr(chars) for chars in part_four) + fp
    enc_part_two = hashlib.new('md5', part_five.encode('latin1')).hexdigest()
    enc_part_two = ''.join([enc_part_two[i] + enc_part_two[i + 1] for i in range(4, 12, 2)][::-1])

    part_six = enc_part_two + first_key + second_key + ''.join(chr(chars) for chars in part_four) + fp
    enc_part_three = custom_base64_encode(part_six)

    faker_token = 'tk04w41l' + enc_part_one + enc_part_three + salt
    part_seven = hashlib.new('md5', faker_token.encode('latin1')).hexdigest()
    part_seven = ''.join([part_seven[i] + part_seven[i + 1] for i in range(4, 12, 2)][::-1])

    true_token = 'tk04w' + part_seven + '41l' + enc_part_one + enc_part_three
    return true_token

def h5st_4_9_1(param_group, body, request_time, salt="x38rG0"):
    api_appid = param_group['api_appid']
    appid = param_group['appid']
    client = param_group['client']
    client_version = param_group['client_version']
    function_id = param_group['function_id']

    body = json.dumps(body, ensure_ascii=False, separators=(',', ":"))
    body = hashlib.new('sha256', body.encode()).hexdigest()

    fp = finger_print_4_9_1()
    environment_dict = {
        "sua": "Macintosh; Intel Mac OS X 10_15_7",
        "pp": {
            "p2": ""
        },
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 5,
            "wk": 0,
            "bu1": "0.1.9",
            "bu2": -1,
            "bu3": 97,
            "bu4": 0,
            "bu5": 0,
            "bu6": 41,
            "bu7": "",
            "bu8": 0
        },
        "pf": "MacIntel",
        "random": "uP32SPogfmax",
        "v": "h5_file_v4.9.1",
        "canvas": "8ed4464d02c680d9290f4da1d59154b0",
        "webglFp": "63e81c90ebaeb6ef7f30f966f5ad027c",
        "ccn": 8,
        "fp": fp,
        "bu1": "0.1.8"
    }
    environment_enc = browser_environment(environment_dict=environment_dict)
    date = datetime.datetime.now()
    format_date = date.strftime("%Y%m%d%H%M%S%f")[:-3]
    current_time = str(int(datetime.datetime.timestamp(date) * 1e3))
    tk, algo = real_token_4_9_1(fp, api_appid)

    part_one = tk + fp + format_date + '07' + api_appid + re.search(r"rd=.(.*?).;", algo).group(1) + salt
    enc_part_one = hmac.new((''.join(chr(158 - ord(chars)) for chars in tk[0:9][::-1]) + tk[9::]).encode('latin1'), part_one.encode('latin1'), hashlib.md5).hexdigest()
    enc_part_one = ''.join([enc_part_one[i] + enc_part_one[i + 1] for i in range(0, 12, 2)][::-1]) + enc_part_one[12::]

    part_two = f'{enc_part_one}appid:{appid}&body:{body}&client:{client}&clientVersion:{client_version}&functionId:{function_id}&t:{request_time}{enc_part_one}{salt}'
    enc_part_two = hashlib.new('md5', part_two.encode('latin1')).hexdigest()
    enc_part_two = ''.join([enc_part_two[i] + enc_part_two[i + 1] for i in range(0, 12, 2)][::-1]) + enc_part_two[12::]

    part_three = f'{part_two}appid:{appid}&body:{body}&client:{client}&clientVersion:{client_version}&functionId:{function_id}&t:{request_time}{enc_part_two}{salt}'
    enc_part_three = hashlib.new('md5', part_three.encode('latin1')).hexdigest()
    enc_part_three = ''.join([enc_part_three[i] + enc_part_three[i + 1] for i in range(0, 12, 2)][::-1]) + enc_part_three[12::]

    return f'{format_date};{fp};{api_appid};{tk};{enc_part_two};4.9;{current_time};{environment_enc};{enc_part_three}'

param_group = {
    'appid': 'item-v3',
    'api_appid': 'fb5df',
    'client': 'pc',
    'client_version': '1.0.0',
    'function_id': 'pc_club_productPageComments',
    "url": "https://item.jd.com/100105177369.html",
    "og": "https://item.jd.com",
}
body = {"productId":100012529857,"score":0,"sortType":5,"page":2,"pageSize":10,"isShadowSku":0,"rid":0,"fold":1,"bbtf":"","shield":""}
h5st = h5st_4_9_1(param_group, body, int(time.time()*1000))