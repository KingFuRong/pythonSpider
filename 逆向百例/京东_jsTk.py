import json
import math
import time
import random
from urllib.parse import quote

import requests

JD_H5_BUILD = {
    "bizId": "JDSC-M-SHOP",
    "shopId": "1000104486",
    "o": "shop.m.jd.com/shop/home"
}

def TDEncrypt(param):
    param_json = json.dumps(param, separators=(',', ':'))
    param_url = quote(param_json, safe='()')
    param_length = len(param_url)
    f = 0
    k = ""
    while f < param_length:
        k_str = "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-"
        h = ord(param_url[f])
        f += 1
        d = ord(param_url[f]) if f < param_length else float('nan')
        f += 1
        a = ord(param_url[f]) if f < param_length else float('nan')
        f += 1
        b = h >> 2
        h = (h & 3) << 4 | (d >> 4 if not math.isnan(d) else 0)
        e = (d & 15) << 2 | (a >> 6 if not math.isnan(a) else 0)
        c = a & 63 if not math.isnan(a) else 0
        if math.isnan(d):
            e = c = 64
        elif math.isnan(a):
            c = 64
        k += k_str[b] + k_str[h] + k_str[e] + k_str[c]
    return k + "/"

def get_jsTk(user_agent, biz_id, shop_id, o):
    ctime = int(time.time() * 1000)
    app_version = user_agent.replace("Mozilla/", "")
    d_param = {
        "ts": {
            "deviceTime": ctime,
            "deviceEndTime": ctime + random.randint(50,150)
        },
        "ca": {
            "tdHash": "fa3fabf83a3dc96ca518dcdec635e8d9",
            "contextName": "webgl,experimental-webgl",
            "webglversion": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
            "shadingLV": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
            "vendor": "WebKit",
            "renderer": "WebKit WebGL",
            "extensions": [
                "ANGLE_instanced_arrays",
                "EXT_blend_minmax",
                "EXT_clip_control",
                "EXT_color_buffer_half_float",
                "EXT_depth_clamp",
                "EXT_disjoint_timer_query",
                "EXT_float_blend",
                "EXT_frag_depth",
                "EXT_polygon_offset_clamp",
                "EXT_shader_texture_lod",
                "EXT_texture_compression_bptc",
                "EXT_texture_compression_rgtc",
                "EXT_texture_filter_anisotropic",
                "EXT_texture_mirror_clamp_to_edge",
                "EXT_sRGB",
                "KHR_parallel_shader_compile",
                "OES_element_index_uint",
                "OES_fbo_render_mipmap",
                "OES_standard_derivatives",
                "OES_texture_float",
                "OES_texture_float_linear",
                "OES_texture_half_float",
                "OES_texture_half_float_linear",
                "OES_vertex_array_object",
                "WEBGL_blend_func_extended",
                "WEBGL_color_buffer_float",
                "WEBGL_compressed_texture_astc",
                "WEBGL_compressed_texture_etc",
                "WEBGL_compressed_texture_etc1",
                "WEBGL_compressed_texture_pvrtc",
                "WEBGL_compressed_texture_s3tc",
                "WEBGL_compressed_texture_s3tc_srgb",
                "WEBGL_debug_renderer_info",
                "WEBGL_debug_shaders",
                "WEBGL_depth_texture",
                "WEBGL_draw_buffers",
                "WEBGL_lose_context",
                "WEBGL_multi_draw",
                "WEBGL_polygon_mode"
            ],
            "wuv": "Google Inc. (Apple)",
            "wur": "ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)"
        },
        "m": {
            "compatMode": "CSS1Compat"
        },
        "n": {
            "vendorSub": "",
            "productSub": "20030107",
            "vendor": "Google Inc.",
            "maxTouchPoints": 0,
            "pdfViewerEnabled": False,
            "hardwareConcurrency": 8,
            "cookieEnabled": True,
            "appCodeName": "Mozilla",
            "appName": "Netscape",
            "appVersion": app_version,
            "platform": "MacIntel",
            "product": "Gecko",
            "userAgent": user_agent,
            "language": "zh-CN",
            "onLine": True,
            "webdriver": False,
            "javaEnabled": False,
            "deprecatedRunAdAuctionEnforcesKAnonymity": False,
            "deviceMemory": 8,
            "enumerationOrder": [
                "vendorSub",
                "productSub",
                "vendor",
                "maxTouchPoints",
                "scheduling",
                "userActivation",
                "doNotTrack",
                "geolocation",
                "connection",
                "plugins",
                "mimeTypes",
                "pdfViewerEnabled",
                "webkitTemporaryStorage",
                "webkitPersistentStorage",
                "windowControlsOverlay",
                "hardwareConcurrency",
                "cookieEnabled",
                "appCodeName",
                "appName",
                "appVersion",
                "platform",
                "product",
                "userAgent",
                "language",
                "languages",
                "onLine",
                "webdriver",
                "getGamepads",
                "javaEnabled",
                "sendBeacon",
                "vibrate",
                "deprecatedRunAdAuctionEnforcesKAnonymity",
                "protectedAudience",
                "bluetooth",
                "storageBuckets",
                "clipboard",
                "credentials",
                "keyboard",
                "managed",
                "mediaDevices",
                "storage",
                "serviceWorker",
                "virtualKeyboard",
                "wakeLock",
                "deviceMemory",
                "userAgentData",
                "cookieDeprecationLabel",
                "login",
                "ink",
                "mediaCapabilities",
                "hid",
                "locks",
                "gpu",
                "mediaSession",
                "permissions",
                "presentation",
                "usb",
                "xr",
                "serial",
                "adAuctionComponents",
                "runAdAuction",
                "canLoadAdAuctionFencedFrame",
                "canShare",
                "share",
                "clearAppBadge",
                "getBattery",
                "getUserMedia",
                "requestMIDIAccess",
                "requestMediaKeySystemAccess",
                "setAppBadge",
                "webkitGetUserMedia",
                "clearOriginJoinedAdInterestGroups",
                "createAuctionNonce",
                "joinAdInterestGroup",
                "leaveAdInterestGroup",
                "updateAdInterestGroups",
                "deprecatedReplaceInURN",
                "deprecatedURNToURL",
                "getInstalledRelatedApps",
                "getInterestGroupAdAuctionData",
                "registerProtocolHandler",
                "unregisterProtocolHandler"
            ]
        },
        "p": [],
        "w": {
            "devicePixelRatio": 4,
            "screenTop": 0,
            "screenLeft": 0
        },
        "s": {
            "availHeight": 740,
            "availWidth": 360,
            "colorDepth": 30,
            "height": 740,
            "width": 360,
            "pixelDepth": 30
        },
        "sc": {
            "ActiveBorder": "rgb(0, 0, 0)",
            "ActiveCaption": "rgb(0, 0, 0)",
            "AppWorkspace": "rgb(255, 255, 255)",
            "Background": "rgb(255, 255, 255)",
            "ButtonFace": "rgb(239, 239, 239)",
            "ButtonHighlight": "rgb(239, 239, 239)",
            "ButtonShadow": "rgb(239, 239, 239)",
            "ButtonText": "rgb(0, 0, 0)",
            "CaptionText": "rgb(0, 0, 0)",
            "GrayText": "rgb(128, 128, 128)",
            "Highlight": "rgba(128, 188, 254, 0.6)",
            "HighlightText": "rgb(0, 0, 0)",
            "InactiveBorder": "rgb(0, 0, 0)",
            "InactiveCaption": "rgb(255, 255, 255)",
            "InactiveCaptionText": "rgb(128, 128, 128)",
            "InfoBackground": "rgb(255, 255, 255)",
            "InfoText": "rgb(0, 0, 0)",
            "Menu": "rgb(255, 255, 255)",
            "MenuText": "rgb(0, 0, 0)",
            "Scrollbar": "rgb(255, 255, 255)",
            "ThreeDDarkShadow": "rgb(0, 0, 0)",
            "ThreeDFace": "rgb(239, 239, 239)",
            "ThreeDHighlight": "rgb(0, 0, 0)",
            "ThreeDLightShadow": "rgb(0, 0, 0)",
            "ThreeDShadow": "rgb(0, 0, 0)",
            "Window": "rgb(255, 255, 255)",
            "WindowFrame": "rgb(0, 0, 0)",
            "WindowText": "rgb(0, 0, 0)"
        },
        "ss": {
            "cookie": True,
            "localStorage": True,
            "sessionStorage": True,
            "globalStorage": False,
            "indexedDB": True
        },
        "tz": -480,
        "lil": "",
        "wil": ""
    }
    a_param = {
        "pin": "",
        "oid": "",
        "bizId": biz_id,
        "fc": "",
        "mode": "strict",
        "p": "s",
        "fp": "b5a9ac831fa86d35bfd1205513d063cd",
        "ctype": 1,
        "v": "3.2.1.1",
        "f": "3",
        "o": o,
        "qs": f"shopId={shop_id}",
        "jsTk": "",
        "qi": ""
    }

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://shop.m.jd.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://shop.m.jd.com/",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
    }
    url = "https://jra.jd.com/jsTk.do"
    params = {
        "a": TDEncrypt(a_param),
    }
    data = {
        "d": TDEncrypt(d_param)
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    return response.text


biz_id = JD_H5_BUILD['bizId']
shop_id = JD_H5_BUILD['shopId']
o = JD_H5_BUILD['o']
user_agent = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
print(get_jsTk(user_agent, biz_id, shop_id, o))
