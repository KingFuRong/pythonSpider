import base64
import datetime
import hashlib
import json
import random
import re
import string
import struct
import time
import requests

MAP = "utsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwv"
ENCRYPT_TYPE = "md5"


def process_string(text, slice_index, cut_index=None):
    if cut_index:
        return (''.join([text[i] + text[i + 1] for i in range(0, slice_index, 2)][::-1]) + text[slice_index:])[
               :cut_index]
    else:
        return ''.join([text[i] + text[i + 1] for i in range(0, slice_index, 2)][::-1]) + text[slice_index:]


def custom_base64_encode(text, new_table=MAP):
    reverse_string = text + ''.join(chr(3 - len(text) % 3) for _ in range(3 - len(text) % 3))
    ciphertext_base64_bytes = base64.b64encode(reverse_string.encode('latin1'))
    ciphertext = ciphertext_base64_bytes.decode()
    raw_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    dictionary_decode = str.maketrans(new_table, raw_table)
    dictionary_encode = dict(zip(dictionary_decode.values(), dictionary_decode.keys()))
    new_result_b64 = ciphertext.translate(dictionary_encode)
    return new_result_b64


MULTIPLIER = 8
SEGMENTS = 11
RESIDUAL = 64
TABLE = "VUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvutsrqponmlkjihgfedcbaZYXW"


def get_key_salt(key):
    salt_map = TABLE
    tk_len = len(key)
    tk_slice = int(tk_len / SEGMENTS)
    tk_salt = str()
    salt_index = 0

    for index in range(0, SEGMENTS):
        if index == SEGMENTS - 1:
            for slice_index in range(0, tk_slice + tk_len % SEGMENTS):
                if index * tk_slice + slice_index < tk_len:
                    salt_index += ord(key[index * tk_slice + slice_index])
        else:
            for slice_index in range(0, tk_slice):
                if index * tk_slice + slice_index < tk_len:
                    salt_index += ord(key[index * tk_slice + slice_index])
        salt_index *= MULTIPLIER
        salt_index %= RESIDUAL
        tk_salt += salt_map[salt_index]
        salt_index = 0

    return tk_salt


FP_KEY = "0jhqw3pa2m"
FP_CHOICE = 3
FP_SLICE = 9
FP_INDEX = 12


def get_fingerprint():
    base36_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    fp_key_len = len(FP_KEY)
    fp_list = list()
    fp_first = str()
    for index in range(0, fp_key_len):
        if len(fp_list) == FP_CHOICE:
            break
        if (random.random() * (fp_key_len - index)) < FP_CHOICE - len(fp_list):
            fp_list.append(FP_KEY[index])

    for index in range(0, FP_CHOICE):
        index_key = int(random.random() * (FP_CHOICE - index))
        fp_first += fp_list[index_key]
        fp_list[index_key] = fp_list[FP_CHOICE - index - 1]

    fp_random = random.randint(0, 10)
    fp_second = ''.join(random.choices(''.join(fp_str for fp_str in FP_KEY if fp_str not in fp_first), k=fp_random))
    fp_third = ''.join(random.choices(''.join(fp_str for fp_str in FP_KEY if fp_str not in fp_first),
                                      k=FP_INDEX - FP_CHOICE - fp_random - 1))

    fp = list(fp_second + fp_first + fp_third + str(fp_random))

    for fp_index in range(len(fp) - FP_SLICE - 1, -1, -1):
        fp[fp_index] = base36_digits[35 - int(fp[fp_index], 36)]

    fp = ''.join(fp[:-FP_SLICE][::-1] + fp[-FP_SLICE:])
    return fp


FIRST_KEY = "74"
SECOND_KEY = "".join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(12))
SALT = 'I,+$,3'
SLICE_INDEX = 6
CUT_INDEX = 8


def get_token(fp):
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
        enc_text = hashlib.new('md5', (FIRST_KEY + SECOND_KEY + endian_timestamp + fp).encode('latin1')).hexdigest()
        enc_text = process_string(enc_text, SLICE_INDEX, CUT_INDEX)
        return custom_base64_encode(enc_text + FIRST_KEY + SECOND_KEY + endian_timestamp + fp)[::-1]

    tk_expr = get_expr()
    tk_cipher = get_cipher()
    fake_tk = 'tk05w41l' + tk_expr + tk_cipher
    fake_tk += get_key_salt(fake_tk) + SALT
    fake_tk_enc = process_string(hashlib.new('md5', fake_tk.encode('latin1')).hexdigest(), SLICE_INDEX, CUT_INDEX)
    real_tk = 'tk05w' + fake_tk_enc + '41l' + tk_expr + tk_cipher

    return real_tk


URL = "https://prodev.m.jd.com/mall/active/31rhHxMvPQ3A3K1ckTXFz1wdrd4f/index.html"
OG = "https://prodev.m.jd.com"
V = "h5_file_v5.1.2"
VERSION = "5.1"
API_APPID = "35fa0"


def get_token_and_algo(fp, user_agent):
    w = random.randint(300, 500)
    h = random.randint(600, 900)
    av = user_agent.replace("Mozilla/", "")
    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_params = "".join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(13))
    random_extend = "".join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(10))
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
            "bu3": 109,
            "bu4": 0,
            "bu5": 0,
            "bu6": 29,
            "bu7": 0,
            "bu8": 0,
            "random": random_extend,
            "bu10": 7,
            "bu11": 1
        },
        "pp1": "",
        "bu1": "",
        "w": w,
        "h": h,
        "ow": w,
        "oh": h,
        "url": URL,
        "og": OG,
        "pf": "MacIntel",
        "pr": 2,
        "re": "https://www.jd.com/",
        "random": random_params,
        "referer": "https://www.jd.com/",
        "v": V,
        "bu2": "    at https://storage.360buyimg.com/webcontainer/main/js_security_v3_main_0.1.8.js?v=20250307:5:78229",
        "bu3": "function Window() { [native code] }$function toString() { [native code] }",
        "bu4": 0,
        "canvas": "8b75695b5b5194d27be029bde91025fc",
        "canvas1": "8b75695b5b5194d27be029bde91025fc",
        "webglFp": "7d6ef74995c683c564146a1d7cf9fa30",
        "webglFp1": "7d6ef74995c683c564146a1d7cf9fa30",
        "ccn": 8,
        "ai": API_APPID,
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
        "version": VERSION,
        "fp": fp,
        "appId": API_APPID,
        "timestamp": int(time.time() * 1e3),
        "platform": "web",
        "expandParams": extend_params,
        "fv": V,
        "localTk": get_token(fp),
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    token = response.json()["data"]["result"]["tk"]
    algo = response.json()["data"]["result"]["algo"]
    return token, algo


APPID = "wh5"
CLIENT = "wh5"
CLIENT_VERSION = "1.0.0"
FUNCTION_ID = "qryBabelFloors4MiniWq"
DTIME_APPEND = '08'
TK_SLICE_INDEX = 0


def h5st(body: dict, user_agent: str, fp=None, token=None, algo=None, t=None):
    today = datetime.datetime.now()
    ctime = str(int(datetime.datetime.timestamp(today) * 1e3))
    dtime = str(today).replace(":", "").replace(".", "").replace("-", "").replace(" ", "")[:-3]
    rd = re.search(r"rd=.(.*?).;", algo).group(1)
    key = f'{token}{fp}{dtime}{DTIME_APPEND}{API_APPID}{rd}'
    key += get_key_salt(key) + SALT
    key = process_string(hashlib.new('md5', key.encode('latin1')).hexdigest(), SLICE_INDEX)

    body = json.dumps(body, separators=(",", ":"), ensure_ascii=False)
    body_string = hashlib.new('sha256', body.encode('latin1')).hexdigest()
    body_data = f"appid:{APPID}&body:{body_string}&client:{CLIENT}&clientVersion:" \
                f"{CLIENT_VERSION}&functionId:{FUNCTION_ID}"
    if t:
        body_data = body_data + f'&t:{t}'
    first_text = get_key_salt(f"{key}{body_data}{key}") + SALT
    second_text = get_key_salt(f"{key}appid:{APPID}&functionId:{FUNCTION_ID}{key}") + SALT
    first_sign = process_string(hashlib.new(ENCRYPT_TYPE, first_text.encode('latin1')).hexdigest(), SLICE_INDEX)
    second_sign = process_string(hashlib.new(ENCRYPT_TYPE, second_text.encode('latin1')).hexdigest(), SLICE_INDEX)

    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_str = "".join(random.choice(string.digits + string.ascii_letters + '_-') for _ in range(9))
    info_json = json.dumps({
        "sua": sua,
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 0,
            "wk": 0,
            "bu1": "0.1.5",
            "bu2": -2,
            "bu3": 33,
            "bu4": 0,
            "bu5": 0,
            "bu6": 32,
            "bu7": "",
            "bu8": 0
        },
        "pf": "MacIntel",
        "random": random_str,
        "v": V,
        "canvas": "fa3fabf83a3dc96ca518dcdec635e8d9",
        "webglFp": "1bfa6f36ccdc1044daf310b6628e7575",
        "ccn": 8,
        "fp": fp
    }, indent=2)
    info_json = info_json + ''.join(chr(3 - len(info_json) % 3) for _ in range(3 - len(info_json) % 3))
    info = custom_base64_encode(text=info_json)[::-1]
    return f"{dtime};{fp};{API_APPID};{token};{first_sign};{VERSION};{ctime};{info};{second_sign}"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
fp = get_fingerprint()
token, algo = get_token_and_algo(fp, user_agent)
h5st = h5st(body={},user_agent=user_agent, fp=fp, token=token, algo=algo)
print(h5st)

