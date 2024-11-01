import datetime
import hashlib
import json
import random
import re
import string
import base64
import time

import requests

# 标准 Base64 字符表
STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# 自定义 Base64 字符表
CUSTOM_ALPHABET = b'WVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvutsrqponmlkjihgfedcbaZYX'

# 创建编码和解码的转换表
ENCODE_TRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
DECODE_TRANS = bytes.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)


def custom_b64encode(data):
    """使用自定义字符表进行 Base64 编码"""
    return base64.b64encode(data).translate(ENCODE_TRANS)


def custom_md5encode(data):
    ori_md5 = hashlib.new('md5', data).hexdigest()
    # 取前12个字符并两两颠倒位置
    new_md5 = ''.join([ori_md5[i + 1] + ori_md5[i] for i in range(0, 12, 2)])
    # 颠倒所有组的顺序并拼接剩余部分
    return new_md5[::-1] + ori_md5[12:]


def custom_sha256encode(data):
    ori_sha256 = hashlib.new('sha256', data).hexdigest()
    # 取前12个字符并两两颠倒位置
    new_sha256 = ''.join([ori_sha256[i + 1] + ori_sha256[i] for i in range(0, 12, 2)])
    # 颠倒所有组的顺序并拼接剩余部分
    return new_sha256[::-1] + ori_sha256[12:]


def browser_environment_enc(original_text):
    def reversal_string(original_str):
        increase_length = 3 - len(original_str) % 3

        for i in range(increase_length):
            original_str += chr(increase_length)

        reversal_str = ''
        for i in range(len(original_str), -1, -3):
            reversal_str += original_str[i:i + 3]

        return reversal_str

    def reversal_encode_string(encode_str):
        reversal_enc_str = ''
        for i in range(0, len(encode_str), 4):
            reversal_enc_str += encode_str[i:i + 4][::-1]
        return reversal_enc_str

    reversal_str = reversal_string(original_text)
    enc_str = custom_b64encode(reversal_str.encode()).decode("utf-8")
    reversal_enc_str = reversal_encode_string(enc_str)

    return reversal_enc_str


def to_base36(num):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    while num > 0:
        result = chars[num % 36] + result
        num //= 36
    return result or "0"


def finger_print_4_8_1(key="2mn87xbyof"):
    middle_original_text = ''.join(random.sample(key, 6))
    temp_key = ''.join([char for char in key if char not in middle_original_text])
    random_num = random.randint(0, 9)
    front_original_text = ''.join(random.choice(temp_key) for _ in range(random_num))
    back_original_text = ''.join(random.choice(temp_key) for _ in range(15 - random_num - 6))
    original_text = front_original_text + middle_original_text + back_original_text + str(random_num)

    cipher_text = ''
    for char in original_text[0:14]:
        if char in string.digits:
            decimal_value = int(char)
        else:
            decimal_value = ord(char) - 97 + 10
        # 用35减去10进制值
        new_value = 35 - decimal_value
        # 将结果转化为36进制
        base36_value = to_base36(new_value)
        cipher_text += base36_value
    cipher_text = cipher_text[::-1] + original_text[14:16]
    return cipher_text


def token_4_8_1(fp, first_key="mT", second_key="DbIAgz71j04v", salt="7hh1BN"):
    def random_mode_max():
        return ''.join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(32))

    def str_to_unicode(str):
        return [ord(unicode_num) for unicode_num in str]

    def decimal_to_little_endian(decimal_number):
        # 创建一个长度为 8 的字节数组
        little_endian_array = [0] * 8
        for i in range(8):
            # 将每个字节填充到数组中
            little_endian_array[i] = decimal_number & 0xFF
            decimal_number >>= 8
        return little_endian_array

    part_one = random_mode_max()
    part_two = random.choice(['1', '2', '3']) + ''.join(
        random.choice(['+', 'x']) + random.choice(['1', '2', '3']) for _ in range(random.randint(1, 4)))
    part_three = part_two + part_one[0:9 - len(part_two)]
    enc_part_one = base64.b64encode(part_three.encode()).decode('utf-8')

    part_four = str_to_unicode(first_key)
    part_five = str_to_unicode(second_key)
    part_six = decimal_to_little_endian(int(time.time() * 1000))
    part_seven = str_to_unicode(fp)
    part_eight = part_four + part_five + part_six + part_seven
    part_nine = custom_md5encode(bytes(part_eight))[0:8]
    part_ten = str_to_unicode(part_nine) + part_four + part_five + part_six + part_seven
    part_ten = part_ten + [3 - len(part_ten) % 3 for _ in range(0, 3 - len(part_ten) % 3)]
    enc_part_two = custom_b64encode(bytes(part_ten)).decode()[::-1]

    part_eleven = 'tk04w41l' + enc_part_one + enc_part_two
    enc_part_three = custom_md5encode((part_eleven + salt).encode())[0:8]

    return 'tk04w' + enc_part_three + '41l' + enc_part_one + enc_part_two


def real_token_4_8_1(url,og,api_appid, fp):
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
        "url": url,
        "og": og,
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
    expand_params = browser_environment_enc(json.dumps(environment_dict, indent=2))
    tk = token_4_8_1(fp)

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
        "version": "4.8",
        "fp": fp,
        "appId": api_appid,
        "timestamp": int(time.time() * 1e3),
        "platform": "web",
        "expandParams": expand_params,
        "fv": "h5_file_v4.8.1",
        "localTk": tk
    }
    data = json.dumps(data, separators=(',', ':'))
    result = requests.post(url, headers=headers, data=data).json()['data']['result']

    return result['tk'], result['algo']


def h5st_4_8_1(param_group, body, t, salt='7hh1BN'):
    url = param_group['url']
    og = param_group['og']
    appid = param_group['appid']
    api_appid = param_group['api_appid']
    client = param_group['client']
    client_version = param_group['client_version']
    function_id = param_group['function_id']

    fp = finger_print_4_8_1()
    environment_dict = {
        "sua": "Macintosh; Intel Mac OS X 10_15_7",
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 5,
            "wk": 0,
            "bu1": "0.1.9",
            "bu2": -1,
            "bu3": 81,
            "bu4": 0,
            "bu5": 0,
            "bu6": 43,
            "bu7": "",
            "bu8": 0
        },
        "pf": "MacIntel",
        "random": "u7GcrHMmX1W",
        "v": "h5_file_v4.8.1",
        "canvas": "8ed4464d02c680d9290f4da1d59154b0",
        "webglFp": "63e81c90ebaeb6ef7f30f966f5ad027c",
        "ccn": 8,
        "fp": fp,
        "bu1": "0.1.8"
    }
    date = datetime.datetime.now()
    body = json.dumps(body, ensure_ascii=False, separators=(',', ":"))
    body = hashlib.new('sha256', body.encode()).hexdigest()
    format_date = date.strftime("%Y%m%d%H%M%S%f")[:-3]
    current_time = str(int(datetime.datetime.timestamp(date) * 1e3))
    environment_enc = browser_environment_enc(json.dumps(environment_dict, indent=2))
    tk, algo = real_token_4_8_1(url ,og ,api_appid, fp)

    part_one = tk + fp + format_date + '36' + api_appid + re.search(r"rd=.(.*?).;", algo).group(1) + salt
    enc_part_one = custom_md5encode(part_one.encode())
    part_two = f"{enc_part_one}appid:{appid}&body:{body}&client:{client}&clientVersion:{client_version}&functionId:{function_id}&t:{t}{enc_part_one}{salt}"
    enc_part_two = custom_sha256encode(part_two.encode())
    part_three = f"{enc_part_one}appid:{appid}&functionId:{function_id}{enc_part_one}{salt}"
    enc_part_three = custom_sha256encode(part_three.encode())

    return f"{format_date};{fp};{api_appid};{tk};{enc_part_two};4.8;{current_time};{environment_enc};{enc_part_three}"


param_group = {
    'appid': 'item-v3',
    'api_appid': 'fb5df',
    'client': 'pc',
    'client_version': '1.0.0',
    'function_id': 'pc_club_productPageComments',
    "url": "https://item.jd.com/100105177369.html",
    "og": "https://item.jd.com",
}
body = {"productId":100105177369,"score":0,"sortType":5,"page":0,"pageSize":10,"isShadowSku":0,"fold":1,"bbtf":"","shield":""}

print(h5st_4_8_1(param_group, body, int(time.time()*1000)))
