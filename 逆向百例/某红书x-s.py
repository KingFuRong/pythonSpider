import base64
import hashlib
import json
import random
import time
from wasmtime import Store, Module, Instance


def custom_b64encode(data_to_encode: bytes, custom_alphabet: str) -> str:
    STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    if len(custom_alphabet) != 64:
        raise ValueError("自定义码表必须包含 64 个字符！")
    standard_encoded_str = base64.b64encode(data_to_encode).decode('ascii')
    translator = str.maketrans(STANDARD_ALPHABET, custom_alphabet)
    return standard_encoded_str.translate(translator)


start_time = int(time.time() * 1000)
xhs_api = "xhs-pc-web"
xhs_key = "19883bb7af6ty540qgul4m63u6u5h95fcml39v0aj30000106925"
array = [119, 104, 96, 41]

random_int = int(random.random() * 4294967295)
xor_num = random_int & 255

temp_array = [(random_int >> (i * 8)) & 0xFF for i in range(4)]
array += temp_array

ctime = int(time.time() * 1000)
temp_array = [(ctime >> (i * 8)) & 0xff for i in range(8)]
temp_val = sum(temp_array[1:]) & 0xFF
temp_array = [(temp_val ^ 41)] + [val ^ 41 for val in temp_array[1:]]
array += temp_array

temp_array = [(start_time >> (i * 8)) & 0xFF for i in range(8)]
array += temp_array

access_time = 15 # 访问次数 每次+1
temp_array = [(access_time >> (i * 8)) & 0xFF for i in range(4)]
array += temp_array

window_property = 1292 # Object.getOwnPropertyNames(window) 返回的Array长度
temp_array = [(window_property >> (i * 8)) & 0xFF for i in range(4)]
array += temp_array

api_url = '/api/sec/v1/scripting{"callFrom":"web","callback":"seccallback"}' # 当前接口的url
temp_array = [(len(api_url) >> (i * 8)) & 0xFF for i in range(4)]
array += temp_array

api_url_encode = hashlib.md5(api_url.encode()).hexdigest() # url的md5加密值
decimal_list = [int(api_url_encode[i:i+2], 16) for i in range(0, len(api_url_encode), 2)]
temp_array = [decimal ^ xor_num for decimal in decimal_list]
array += temp_array[0:8]

temp_array = [len(xhs_key)] + list(xhs_key.encode('utf-8'))
array += temp_array
temp_array = [len(xhs_api)] + list(xhs_api.encode('utf-8'))
array += temp_array

xhs_array = [115, 248, 83, 102, 103, 201, 181, 131, 99, 94, 4, 68, 250, 132, 21] # 常量Array
window_ee019d93900dcee2bdafbe5894e6c8a9 = 1 # window._ee019d93900dcee2bdafbe5894e6c8a9的值
window_dssts = 0 # window.dssts的值
temp_array = [
    1,
    xor_num ^ xhs_array[0],
    window_ee019d93900dcee2bdafbe5894e6c8a9 ^ xhs_array[1],
    window_dssts ^ xhs_array[2],
    1 ^ xhs_array[3], # 100
    0 ^ xhs_array[4], # 101
    0 ^ xhs_array[5], # 102
    0 ^ xhs_array[6], # 103
    2 ^ xhs_array[7], # 104
    0 ^ xhs_array[8], # 106
    0 ^ xhs_array[9], # 107
    3 ^ xhs_array[10], # 401
    0 ^ xhs_array[11],
    0 ^ xhs_array[12], # 109
    0 ^ xhs_array[13],
    0 ^ xhs_array[14],
]
array += temp_array
byte_data = bytes(array)

# wasm 载入初始化
store = Store()
module = Module.from_file(store.engine, './000238fa')
instance = Instance(store, module, [])
exports = instance.exports(store)
malloc = exports['malloc']
free = exports['free']
modify_array = exports['xy_18d12b8e541b1fd80b1c3c2eeb63a208']
encrypt_array = exports['xy_daa92688ff9309e1a29d25224fd0164a']
memory = exports['memory']

# 数组偏移
ptr = malloc(store, len(byte_data))
memory.write(store, byte_data, ptr)
print('原始数组: ', list(memory.read(store, ptr, ptr + len(byte_data))))
array_result = modify_array(store, ptr, len(byte_data), 858975407)
modified_byte = memory.read(store, array_result, array_result + len(byte_data))

free(store, array_result)
free(store, ptr)

# 数组加密
ptr = malloc(store, len(modified_byte))
memory.write(store, modified_byte, ptr)
print('偏移数组: ', list(memory.read(store, ptr, ptr + len(byte_data))))
encode_result = encrypt_array(store, ptr, len(modified_byte))
encode_memory = memory.read(store)
encode_str = []
for idx in range(encode_result, len(encode_memory)):
    byte = encode_memory[idx]
    if byte == 0:
        break
    encode_str.append(chr(byte))
encode_str = 'mns0101_' + ''.join(encode_str)
print('加密密文: ', encode_str)

s = {
    "x0": "4.2.5",
    "x1": "xhs-pc-web",
    "x2": "Mac OS",
    "x3": encode_str,
    "x4": "object"
}
print('构造参数: ', json.dumps(s, separators=(',', ':')))
final_result = "XYS_" + custom_b64encode(json.dumps(s, separators=(',', ':')).encode(), 'ZmserbBoHQtNP+wOcza/LpngG8yJq42KWYj0DSfdikx3VT16IlUAFM97hECvuRX5')
print('最终结果: ', final_result)

