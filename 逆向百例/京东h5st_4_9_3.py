import base64
import datetime
import hashlib
import hmac
import json
import random
import re
import string
import struct
import time

import requests

JD_H5_RANK_BUILD = {
    "appid": "wh5",
    "api_appid": "35fa0",
    "client": "wh5",
    "version": "4.9",
    "client_version": "1.0.0",
    "v": "h5_file_v4.9.3",
    "function_id": "qryBabelFloors4MiniWq",
    "url": "https://pro.m.jd.com/mini/active/31rhHxMvPQ3A3K1ckTXFz1wdrd4f/index.html",
    "og": "https://pro.m.jd.com",
    'dtime_append': '77',
    'salt': '83qem7',
    'token_slice_index': 14,
    'key_slice_index': 6
}


def process_string(text, slice_index):
    return ''.join([text[i] + text[i + 1] for i in range(0, slice_index, 2)][::-1]) + text[slice_index:]


def custom_base64_encode(text, new_table="rqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvuts"):
    reverse_string = text + ''.join(chr(3 - len(text) % 3) for _ in range(3 - len(text) % 3))
    ciphertext_base64_bytes = base64.b64encode(reverse_string.encode('latin1'))
    ciphertext = ciphertext_base64_bytes.decode()
    raw_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    dictionary_decode = str.maketrans(new_table, raw_table)
    dictionary_encode = dict(zip(dictionary_decode.values(), dictionary_decode.keys()))
    new_result_b64 = ciphertext.translate(dictionary_encode)
    return new_result_b64


def custom_md5_encode(text, slice_index, cut_index):
    ciphertext = hashlib.new('md5', text.encode('latin1')).hexdigest()
    return process_string(ciphertext, slice_index)[0:cut_index]


def finger_print_4_9_3(key='z4rekl9i1u', choice_num=4, size_index=12, slice_index=8):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    middle = ''.join(random.sample(key, k=choice_num))
    temp = ''.join([char for char in key if char not in middle])
    random_num = random.randint(0, 9)
    first = ''.join(random.choices(temp, k=random_num))
    last = ''.join(random.choices(temp, k=size_index - random_num - 1))

    finger_print = first + middle + last + str(random_num)
    final_finger_print = []
    for i in finger_print[0:slice_index][::-1]:
        final_finger_print.append(chars[35 - int(i, 36)])
    final_finger_print.extend(finger_print[slice_index:16])

    return ''.join(final_finger_print)


def token_4_9_3(fp, first_key='R,', second_key='UnHWNe%n]ro/', salt='83qem7', slice_index=6, cut_index=8):
    def get_expr():
        choice_num = 2 + random.randint(0, 3)
        random_mode_max = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=32))
        num_list = ["1", "2", "3"]
        ope_list = ["+", "x"]
        ori_text = ''
        for i in range(choice_num):
            ori_text += random.choice(num_list)
            if choice_num - 1 > i:
                ori_text += random.choice(ope_list)
        ori_text += random_mode_max[0:9 - len(ori_text)]
        return base64.b64encode(ori_text.encode('utf-8')).decode("utf-8").replace('+', '-').replace('/', '_').replace("=", "")

    def get_cipher():
        timestamp = int(time.time() * 1000)
        endian_timestamp = ''.join(chr(chars) for chars in int_to_little_endian_bytes(timestamp))
        enc_text = custom_md5_encode(first_key + second_key + endian_timestamp + fp, slice_index, cut_index)
        return custom_base64_encode(enc_text + first_key + second_key + endian_timestamp + fp, new_table="rqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvuts")[::-1]

    def int_to_little_endian_bytes(num, length=8):
        return list(struct.pack('<Q', num)[:length])

    tk_expr = get_expr()
    tk_cipher = get_cipher()
    fake_tk = 'tk04w41l' + tk_expr + tk_cipher
    real_tk = 'tk04w' + custom_md5_encode(fake_tk + salt, slice_index, cut_index) + '41l' + tk_expr + tk_cipher
    return real_tk


def token_and_algo(user_agent, fp, version, api_appid, url, og, v):
    w = random.randint(300, 500)
    h = random.randint(600, 900)
    av = user_agent.replace("Mozilla/", "")
    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_params = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=11))
    params = json.dumps({
        "wc": 1,
        "wd": 0,
        "l": "zh-CN",
        "ls": "zh-CN,en-US",
        "ml": 0,
        "pl": 0,
        "av": av,
        "ua": user_agent,
        "sua": sua,
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 0,
            "wk": 0,
            "bu1": "lite_0.1.5",
            "bu2": 0,
            "bu3": 58,
            "bu4": 0,
            "bu5": 0,
            "bu6": 3,
            "bu7": "",
            "bu8": 0
        },
        "pp1": "",
        "bu1": "",
        "w": w,
        "h": h,
        "ow": w,
        "oh": h,
        "url": url,
        "og": og,
        "pf": "Linux aarch64",
        "pr": 3,
        "re": "",
        "random": random_params,
        "referer": "",
        "v": v,
        "bu2": "    at n (https://storage.360buyimg.com/babelnode/jd-jssdk/4.5.2/jd-jssdk.js:3:27296)",
        "canvas": "",
        "canvas1": "47e3f66141bae5270127dcb7f721d7f4",
        "webglFp": "",
        "webglFp1": "e8097fb371349c2e989a6f3dc8f1e907",
        "ccn": 8,
        "ai": api_appid,
        "fp": fp
    }, indent=2)
    extend_params = custom_base64_encode(text=params, new_table="rqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvuts")[::-1]

    headers = {
        "authority": "cactus.jd.com",
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://item.m.jd.com",
        "pragma": "no-cache",
        "referer": "https://item.m.jd.com/",
        "user-agent": user_agent
    }
    url = "https://cactus.jd.com/request_algo"
    data = {
        "version": version,
        "fp": fp,
        "appId": api_appid,
        "timestamp": int(time.time() * 1e3),
        "platform": "web",
        "expandParams": extend_params,
        "fv": v,
        "localTk": token_4_9_3(fp)
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    token = response.json()["data"]["result"]["tk"]
    algo = response.json()["data"]["result"]["algo"]
    return token, algo


def h5st_4_9_3(body, user_agent, fp, token, algo, t, build_params):
    def get_key(token, fp, format_date, dtime_append, api_appid, algo, salt, token_slice_index, key_slice_index):
        rd = re.search(r"rd=.(.*?).;", algo).group(1)
        hmac_text = token + fp + format_date + dtime_append + api_appid + rd + salt
        hmac_key = ''.join(chr(158 - ord(chars)) for chars in token[0:token_slice_index][::-1]) + token[token_slice_index::]

        key = hmac.new(hmac_key.encode('latin1'), hmac_text.encode('latin1'), hashlib.md5).hexdigest()
        return process_string(key, key_slice_index)

    appid = build_params["appid"]
    client = build_params["client"]
    version = build_params["version"]
    api_appid = build_params["api_appid"]
    function_id = build_params["function_id"]
    client_version = build_params["client_version"]
    dtime_append = build_params['dtime_append']
    salt = build_params['salt']
    token_slice_index = build_params['token_slice_index']
    key_slice_index = build_params['key_slice_index']

    sua = re.search(r'5\.0 \((.*?)\)', user_agent).group(1)
    random_params = ''.join(random.choices(string.digits + string.ascii_letters + '_-', k=12))
    env_info = json.dumps({
        "sua": sua,
        "pp": {},
        "extend": {
            "wd": 0,
            "l": 0,
            "ls": 0,
            "wk": 0,
            "bu1": "lite_0.1.5",
            "bu2": -2,
            "bu3": 63,
            "bu4": 0,
            "bu5": 0,
            "bu6": 17,
            "bu7": "",
            "bu8": 0
        },
        "pf": "Linux aarch64",
        "random": random_params,
        "v": v,
        "canvas": "47e3f66141bae5270127dcb7f721d7f4",
        "webglFp": "e8097fb371349c2e989a6f3dc8f1e907",
        "ccn": 8,
        "fp": fp
    }, indent=2)

    date_now = datetime.datetime.now()
    format_date = date_now.strftime("%Y%m%d%H%M%S%f")[:-3]
    current_time = str(int(datetime.datetime.timestamp(date_now) * 1e3))

    key = get_key(token, fp, format_date, dtime_append, api_appid, algo, salt, token_slice_index, key_slice_index)
    body = json.dumps(body, separators=(",", ":"), ensure_ascii=False)
    body_str = hashlib.new('sha256', body.encode()).hexdigest()

    text = f"{key}appid:{appid}&body:{body_str}&client:{client}&clientVersion:{client_version}&functionId:{function_id}{key}{salt}"
    sign = process_string(hashlib.new('sha256', text.encode()).hexdigest(), key_slice_index)
    text1 = f"{key}appid:{appid}&functionId:{function_id}{key}{salt}"
    sign1 = process_string(hashlib.new('sha256', text1.encode()).hexdigest(), key_slice_index)
    env_info_enc = custom_base64_encode(env_info, new_table="rqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA-_9876543210zyxwvuts")[::-1]

    return f"{format_date};{fp};{api_appid};{token};{sign};{version};{current_time};{env_info_enc};{sign1}"


url = "https://api.m.jd.com/client.action"
version = JD_H5_RANK_BUILD["version"]
api_appid = JD_H5_RANK_BUILD["api_appid"]
page_url = JD_H5_RANK_BUILD["url"]
og = JD_H5_RANK_BUILD["og"]
v = JD_H5_RANK_BUILD["v"]

headers = {
    "Host": "api.m.jd.com",
    "sec-ch-ua-platform": "\"Android\"",
    "user-agent": "Mozilla/5.0 (Linux; Android 14; 23078RKD5C Build/UP1A.230905.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.102 Mobile Safari/537.36 XWEB/1300073 MMWEBSDK/20231202 MMWEBID/4640 MicroMessenger/8.0.47.2560(0x28002F51) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx91d27dbf599dff74",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "x-referer-page": "https://pro.m.jd.com/mini/active/31rhHxMvPQ3A3K1ckTXFz1wdrd4f/index.html",
    "content-type": "application/x-www-form-urlencoded",
    "x-rp-client": "h5_1.0.0",
    "sec-ch-ua-mobile": "?1",
    "accept": "*/*",
    "origin": "https://pro.m.jd.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://pro.m.jd.com/mini/active/31rhHxMvPQ3A3K1ckTXFz1wdrd4f/index.html?has_native=0&indParam=%7B%22bbtf%22%3A%22%22%2C%22preSrc%22%3A%22xiaochengxupindao%22%2C%22fromName%22%3A%22main_channel%22%2C%22source%22%3A%22main_channel%22%2C%22currSku%22%3A%22%22%2C%22rankId%22%3A%2226541%22%7D&babelChannel=ttt1&hideAd=&transparent=1&commontitle=no&wxAppName=jd&cookie=%7B%22visitkey%22%3A%22undefined%22%2C%22__wga%22%3A%221732074425657.1732074410055.1732011314146.1731987183834.5.3%22%2C%22PPRD_P%22%3A%22EA.17078.49.1-CT.137854.3.30-LOGID.1732074425663.1013037802%22%2C%22__jda%22%3A%22122270672.1731986650139388642925.1731986650.1731986650.1731986650.1%22%2C%22__jdv%22%3A%22122270672%7Cdirect%7Ct_1000578828_xcx_1089_ltkxl%7Cxcx%7C-%7C1732074432598%22%2C%22unpl%22%3A%22undefined%22%2C%22wxapp_type%22%3A1%2C%22cd_eid%22%3A%22jdd01w49ZMQTRBPP5NCR4XFVSDJ7XMFPGEC6CL6UUQUAP75L7XL5INEUORLP7GWDSY5OM5W2CSFRWZO2P4G7UUDA4KP55VY2VCHN2RIPF3ERPPWKGPEQPQJKHHIGOZOCXJFLR63E%22%2C%22pinStatus%22%3A%22undefined%22%2C%22wxapp_openid%22%3A%22oA1P50NgALLs0hjTmoL2shpdA7Ns%22%2C%22wxapp_version%22%3A%229.23.140%22%2C%22appType%22%3A%22%22%2C%22buildtime%22%3A20241114%2C%22md5_pin%22%3A%2270175f64bd4ff37e78018e668853c6b6%22%2C%22degrade_level%22%3A0%7D",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "priority": "u=1, i"
}
body = {"activityId": "4KBFhfFLrhBy2CzDLvYY2efFid3Y",
        "fullUrl": "https://pro.m.jd.com/mini/active/31rhHxMvPQ3A3K1ckTXFz1wdrd4f/index.html?has_native=0&indParam=%7B%22bbtf%22%3A%22%22%2C%22preSrc%22%3A%22xiaochengxupindao%22%2C%22fromName%22%3A%22main_channel%22%2C%22source%22%3A%22main_channel%22%2C%22currSku%22%3A%22%22%2C%22rankId%22%3A%2226541%22%7D&babelChannel=ttt1&hideAd=&transparent=1&commontitle=no&wxAppName=jd&cookie=%7B%22visitkey%22%3A%22undefined%22%2C%22__wga%22%3A%221732074425657.1732074410055.1732011314146.1731987183834.5.3%22%2C%22PPRD_P%22%3A%22EA.17078.49.1-CT.137854.3.30-LOGID.1732074425663.1013037802%22%2C%22__jda%22%3A%22122270672.1731986650139388642925.1731986650.1731986650.1731986650.1%22%2C%22__jdv%22%3A%22122270672%7Cdirect%7Ct_1000578828_xcx_1089_ltkxl%7Cxcx%7C-%7C1732074432598%22%2C%22unpl%22%3A%22undefined%22%2C%22wxapp_type%22%3A1%2C%22cd_eid%22%3A%22jdd01w49ZMQTRBPP5NCR4XFVSDJ7XMFPGEC6CL6UUQUAP75L7XL5INEUORLP7GWDSY5OM5W2CSFRWZO2P4G7UUDA4KP55VY2VCHN2RIPF3ERPPWKGPEQPQJKHHIGOZOCXJFLR63E%22%2C%22pinStatus%22%3A%22undefined%22%2C%22wxapp_openid%22%3A%22oA1P50NgALLs0hjTmoL2shpdA7Ns%22%2C%22wxapp_version%22%3A%229.23.140%22%2C%22appType%22%3A%22%22%2C%22buildtime%22%3A20241114%2C%22md5_pin%22%3A%2270175f64bd4ff37e78018e668853c6b6%22%2C%22degrade_level%22%3A0%7D#wdref=http%3A%2F%2Fwq.jd.com%2Fwxapp%2Fpages%2Fh5%2Findex&wxa_level=5&sens=%7B%22wq_addr%22%3A%224551928385%7C1_72_2819_0%7C%E5%8C%97%E4%BA%AC%E5%B8%82_%E6%9C%9D%E9%98%B3%E5%8C%BA_%E4%B8%89%E7%8E%AF%E8%87%B3%E5%9B%9B%E7%8E%AF%E4%B9%8B%E9%97%B4_%7C%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E4%B8%89%E7%8E%AF%E8%87%B3%E5%9B%9B%E7%8E%AF%E4%B9%8B%E9%97%B4%7C116.444%2C39.9219%22%7D&wxappSeries=%7B%22uuid%22%3A%2217084911309601621112684%22%2C%22std%22%3A%22JA2019_5112348%22%2C%22seq%22%3A5%2C%22vts%22%3A63%2C%22appid%22%3A%22wx91d27dbf599dff74%22%7D",
        "queryFloorsParam": {"type": "2", "floorParams": {
            "198885893": {"queryType": "2", "siteClient": "wh5", "siteClientVersion": "2.0.0", "rankId": "3166629",
                          "currSku": "", "fromName": "main_channel", "pageNum": 1, "preSrc": "xiaochengxupindao",
                          "bbtf": "", "spuId": "", "lng": "", "lat": ""}}}}
user_agent = headers.get('user-agent')

fp = finger_print_4_9_3()
tk, algo = token_and_algo(user_agent, fp, version, api_appid, url, og, v)
t = int(time.time() * 1000)

h5st = h5st_4_9_3(body, user_agent, fp, tk, algo, t, build_params=JD_H5_RANK_BUILD)

data = {
    "screen": "1221*2463",
    "version": "1.0.0",
    "clientVersion": "1.0.0",
    "client": "wh5",
    "appid": "wh5",
    "body": json.dumps(body, separators=(",", ":"), ensure_ascii=False),
    "area": "",
    "uuid": "1732074428005452443300",
    "uemps": "",
    "functionId": "qryBabelFloors4MiniWq",
    "loginType": "1",
    "loginWQBiz": "tttwxapp",
    "h5st": h5st,
    "x-api-eid-token": "jdd033UQTR6JFVUU7YLHYQTSIHDPFCPC2FGAXAFKCFR53KTIJXAEMDIOHMLD2W74S3K2HDF7EFZKMKWP7SXEN2T47QUMJI4AAAAMTI6XF3VYAAAAADSSO34QRIWDAFIX"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)
