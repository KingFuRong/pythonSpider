window = global;
navigator = {};
navigator.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36';

const JSEncrypt = require('jsencrypt')
const CryptoJS = require('crypto-js')

function i(e) {
    e += "";
    var t = 0
        , n = 0
        , r = 0;
    if (0 === e.length)
        return t.toString(36);
    for (n = 0; n < e.length; n++)
        r = e.charCodeAt(n),
            t = (t << 5) - t + r,
            t |= 0;
    return t.toString(36)
}

/**
 *
 * @returns {string} cookies crosSdkDT2019DeviceId
 */
function get_crosSdkDT2019DeviceId() {
    function e() {
        return Math.floor(65536 * (1 + Math.random())).toString(36).substring(1)
    }

    return i(1 * new Date + "") + "-" + i(navigator.userAgent) + "-" + e() + e() + e() + e() + e() + "-" + e() + e() + e()
}

function get_k_and_d(cookies) {
    var publickey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp/NaqnXzrnkOGi7neRtUKWhMjenaBpHdN0SL0Ro4Pcjhygxkyk4JltLAtqrNPzIBcFL52ecGS4C9VHm+1UrZIdGzDuJwShWSsnQYRQ47v8ixPpDoScGYBVHi0LN1DJg5lGxkWayeXF1C/hUwZ11P26fmE2M5Jec9Z6ClZPQDjxBJdFtegAQLHsV+KEf/VJu+pqpe2SWuY4UrlL4wQH+y5jf89nccFFQ0I9T3vjSEgaOwRzeSGdNvQg0ORI9sefq5W9F0+4iPVbgKdLAvMY/H9oK8TqsSbP1gkGOysUn68Qk/STxTbbO0Y1KMyrRUieGUe0OIx1tJUcstoZP9Uzi+xwIDAQAB"
    var n = {
        "uuid": "",
        "requestData": {
            "app_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "brand_name": -911,
            "client_ip": -911,
            "client_ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "device_type": "pc",
            "is_debug": 0,
            "net": "4g",
            "os_type": "Windows",
            "os_version": "10",
            "ram_total": 4294705152,
            "sdk_version": "0.0.10",
            "app_code_name": "Mozilla",
            "app_name": "Netscape",
            "product": "Gecko",
            "product_sub": "20030107",
            "platform": "Win32",
            "cookies": cookies,
            "is_incognito": 910474987,
            "plugins": [
                {
                    "name": "PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Chrome PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Chromium PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "Microsoft Edge PDF Viewer",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                },
                {
                    "name": "WebKit built-in PDF",
                    "description": "Portable Document Format",
                    "mimeTypes": [
                        {
                            "type": "application/pdf",
                            "suffixes": "pdf"
                        },
                        {
                            "type": "text/pdf",
                            "suffixes": "pdf"
                        }
                    ]
                }
            ],
            "cookies_enabled": true,
            "do_not_track": -911,
            "inner_width": "1536",
            "outer_width": "1536",
            "inner_height": "168",
            "outer_height": "864",
            "indexed_db": true,
            "open_db": false,
            "local_storage": 0,
            "session_storage": 0,
            "mime_types": [
                {
                    "suffixes": "pdf",
                    "description": "Portable Document Format",
                    "type": "application/pdf"
                },
                {
                    "suffixes": "pdf",
                    "description": "Portable Document Format",
                    "type": "text/pdf"
                }
            ],
            "pdf_viewer_enabled": "true",
            "vendor": "Google Inc.",
            "vendor_flavors": [
                "chrome"
            ],
            "is_webdriver": false,
            "language": "zh-CN",
            "browser_language": -911,
            "user_language": -911,
            "system_language": -911,
            "time_zone": "-8",
            "fonts": "Calibri,Century,Century Gothic,Franklin Gothic,Leelawadee,MS Reference Specialty,MS UI Gothic,MT Extra,Marlett,Microsoft Uighur,Monotype Corsiva,Pristina,Segoe UI Light,SimHei",
            "math": {
                "acos": 1.4473588658278522,
                "acosh": 709.889355822726,
                "acoshPf": 355.291251501643,
                "asin": 0.12343746096704435,
                "asinh": 0.881373587019543,
                "asinhPf": 0.8813735870195429,
                "atanh": 0.5493061443340548,
                "atanhPf": 0.5493061443340548,
                "atan": 0.4636476090008061,
                "sin": 0.8178819121159085,
                "sinh": 1.1752011936438014,
                "sinhPf": 2.534342107873324,
                "cos": -0.8390715290095377,
                "cosh": 1.5430806348152437,
                "coshPf": 1.5430806348152437,
                "tan": -1.4214488238747245,
                "tanh": 0.7615941559557649,
                "tanhPf": 0.7615941559557649,
                "exp": 2.718281828459045,
                "expm1": 1.718281828459045,
                "expm1Pf": 1.718281828459045,
                "log1p": 2.3978952727983707,
                "log1pPf": 2.3978952727983707,
                "powPI": 1.9275814160560204e-50
            },
            "avail_height": "864",
            "avail_width": "1536",
            "avail_left": 0,
            "avail_top": 0,
            "height": "864",
            "width": "1536",
            "screen_frame": [
                0,
                0,
                0,
                0
            ],
            "color_depth": "24",
            "pixel_depth": "24",
            "max_touch_points": "0",
            "monochrome": 0,
            "is_hdr": false,
            "hardware_concurrency": "16",
            "cpu_class": -911,
            "gpu_vendor": "Google Inc. (NVIDIA)",
            "gpu_renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Laptop GPU (0x00002560) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "canvas_fingerprint": "c709923694cff34843bd9ff515624a60700a486e3029bad5662e7475e814c470",
            "canvas_pixel": "255,166,14,255,255,166,14,255,255,165,14,255,255,165,14,255,255,164,14,255,255,164,15,255,235,168,13,255,156,189,5,255,148,191,4,255,148,191,4,255,148,191,4,255,187,180,9,255,255,160,15,255,255,160,16,255,255,159,16,255,172,183,7,255,148,190,5,255,148,190,5,255,164,185,6,255,198,175,11,255,149,164,24,255,214,111,56,255,231,97,64,255,154,160,26,255,202,121,50,255,250,81,74,255,250,81,74,255,184,136,41,255,162,155,30,255,239,90,69,255,250,81,74,255,250,81,74,255,184,136,41,255,147,167,22,255,202,121,50,255,250,81,74,255,250,81,74,255,239,90,69,255,162,155,30,255,147,167,22,255,147,167,22,255,170,147,34,255,184,136,41,255,154,160,26,255,231,97,64,255,214,111,56,255,149,164,24,255,147,167,22,255,147,167,22,255,162,155,30,255,239,90,69,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,184,136,41,255,170,147,34,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,231,97,64,255,154,160,26,255,202,121,50,255,231,97,64,255,154,160,26,255,202,121,50,255,250,81,74,255,250,81,74,255,184,136,41,255,162,155,30,255,239,90,69,255,250,81,74,255,202,121,50,255,147,167,22,255,102,171,36,255,118,158,44,255,168,169,11,255,187,160,14,255,255,123,25,255,255,123,25,255,187,158,14,255,148,179,7,255,148,179,7,255,148,179,8,255,187,157,14,255,255,120,26,255,255,119,26,255,187,157,14,255,164,170,11,255,223,122,36,255,40,104,133,255,173,124,54,255,156,172,9,255,172,163,12,255,148,177,8,255,148,177,8,255,255,166,14,255,255,165,14,255,255,165,14,255,255,164,14,255,255,163,14,255,255,163,14,255,255,162,14,255,255,162,15,255,255,161,15,255,255,161,15,255,255,160,15,255,255,160,15,255,255,159,15,255,255,159,16,255,255,158,15,255,255,158,16,255,255,157,16,255,255,157,16,255,255,156,16,255,255,156,16,255,250,82,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,142,90,108,255,73,96,130,255,239,82,78,255,250,81,74,255,204,85,88,255,38,98,141,255,204,85,88,255,172,166,11,255,187,159,14,255,255,122,25,255,255,122,25,255,255,121,25,255,255,121,25,255,255,120,25,255,255,120,26,255,255,119,25,255,255,119,26,255,255,118,26,255,255,118,26,255,255,117,26,255,232,115,38,255,40,104,133,255,173,124,54,255,156,172,9,255,205,143,18,255,255,114,27,255,255,113,27,255,255,166,14,255,255,165,15,255,255,165,14,255,255,164,15,255,255,163,15,255,255,163,15,255,255,162,15,255,255,162,15,255,255,161,15,255,255,161,16,255,255,160,16,255,255,160,16,255,255,159,16,255,255,159,16,255,255,158,16,255,255,158,16,255,255,157,16,255,255,157,17,255,255,156,17,255,255,156,17,255,250,84,72,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,250,81,74,255,239,82,78,255,73,96,130,255,46,147,85,255,61,163,62,255,26,108,137,255,204,85,88,255,214,113,54,255,156,176,9,255,218,143,19,255,255,122,25,255,255,122,26,255,255,121,25,255,255,121,26,255,255,120,26,255,255,120,26,255,255,119,26,255,255,119,26,255,255,118,26,255,255,118,27,255,255,117,27,255,232,115,39,255,40,104,133,255,173,124,54,255,156,172,9,255,205,143,18,255,255,114,27,255,255,113,28,255",
            "webgl_fingerprint": "b98f6ffeaaaf4f10eb90972069aa5d5ddc6e77d0d7a859338a342b64ca729763",
            "audio_context_fingerprint": 124.04347527516074,
            "device_model": -911,
            "request_time": new Date().getTime()
        },
        "eventSceneId": "event1683346057429434",
        "businessType": "uc"
    };
    var e = JSON.stringify(n);
    var u = {
        "default": {
            "_map": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        }
    }

    function get_key() {
        const t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            , n = t.length;
        let i = "";
        for (let e = 0; e < 16; e++)
            i += t.charAt(Math.floor(Math.random() * n));
        return i
    }

    function p(e, t) {
        const n = CryptoJS.enc.Utf8.parse(t)
            , i = CryptoJS.enc.Utf8.parse(e);
        return CryptoJS.AES.encrypt(i, n, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).ciphertext.toString(CryptoJS.enc.Base64)
    }

    var t = get_key();
    var n = new JSEncrypt();
    n.setPublicKey(publickey);
    return {
        k: n.encrypt(t),
        d: p(e, t),
        key: t
    }
}

function password_enc(password) {
    var publickey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCJxBJn2gY+D2OdldUxpsNwIGyKc/QRvqbWWGIdIewE7SxyyGHNcLdT+2bb6E6Ko7jBlEElUBkKJJ93G761dp6pXu7ORTjJ1mta99Bjud7+u/3473mG+QReoH4ux8idsd+E0TW0HWUP6zyfYy42HPSaN3pjetM30sVazdWxpvAH6wIDAQAB"
    var n = new JSEncrypt();
    n.setPublicKey(publickey)
    return n.encrypt(password)
}

