const jsrsasign = require('jsrsasign');
const JSEncrypt = require('node-jsencrypt');
const CryptoJS = require('crypto-js');

var t = {}

function first_get_params(gt, challenge) {
    t = {
        $_EIi: {
            "$_CAAj": Date.now(),
            "protocol": "https://",
            "gt": gt,
            "challenge": challenge,
            "offline": false,
            "new_captcha": true,
            "product": "popup",
            "width": "300px",
            "https": true,
            "api_server": "apiv6.geetest.com",
            "type": "fullpage",
            "static_servers": ["static.geetest.com/", "static.geevisit.com/"],
            "beeline": "/static/js/beeline.1.0.1.js",
            "voice": "/static/js/voice.1.2.4.js",
            "click": "/static/js/click.3.1.0.js",
            "fullpage": "/static/js/fullpage.9.1.9-glhvqm.js",
            "slide": "/static/js/slide.7.9.2.js",
            "geetest": "/static/js/geetest.6.0.9.js",
            "aspect_radio": {
                "slide": 103, "click": 128, "voice": 128, "beeline": 50
            },
            "cc": 16,
            "supportWorker": true,
            "$_FFG": {
                "pt": 0
            }
        }, $_EJY: {
            "gt": gt,
            "challenge": challenge,
            "offline": false,
            "new_captcha": true,
            "product": "popup",
            "width": "300px",
            "https": true,
            "api_server": "apiv6.geetest.com",
            "protocol": "https://",
            "type": "fullpage",
            "static_servers": ["static.geetest.com/", "static.geevisit.com/"],
            "beeline": "/static/js/beeline.1.0.1.js",
            "voice": "/static/js/voice.1.2.4.js",
            "click": "/static/js/click.3.1.0.js",
            "fullpage": "/static/js/fullpage.9.1.9-glhvqm.js",
            "slide": "/static/js/slide.7.9.2.js",
            "geetest": "/static/js/geetest.6.0.9.js",
            "aspect_radio": {
                "slide": 103, "click": 128, "voice": 128, "beeline": 50
            }
        }, $_BJGj: 0, $_BJHj: "web"
    }
    var n = t['$_EIi'];

    var e = $_BIBF(); // t['$_BJCx']['$_BIBF']()
    t['$_CCFN'] = e, t['$_EJY']['cc'] = n['cc'], t['$_EJY']['ww'] = n['supportWorker'], t['$_EJY']['i'] = e;
    //t['$_CCGH']
    var r = $_CCGH()
        // $_BFD()['encrypt1']                             t['$_CCHI']
        , o = encrypt1(JSON['stringify'](t['$_EJY']), $_CCHI())
        //   p['$_HEv']
        , i = $_HEv(o), s = {
            'gt': t['$_EJY']['gt'],
            'challenge': t['$_EJY']['challenge'],
            'lang': "zh-cn",
            'pt': t['$_BJGj'],
            'client_type': t['$_BJHj'],
            'w': i + r,
            'aeskey': t['$_EIi']['aeskey'],
            'fingerprint': e,
        }
    return s;
}

// ====================获取e的值====================
function $_BIBF() {
    var n = this, r = {} //n['$_BGu']
        , o = [],
        $_BJAc = ["textLength", "HTMLLength", "documentMode", "A", "ARTICLE", "ASIDE", "AUDIO", "BASE", "BUTTON", "CANVAS", "CODE", "IFRAME", "IMG", "INPUT", "LABEL", "LINK", "NAV", "OBJECT", "OL", "PICTURE", "PRE", "SECTION", "SELECT", "SOURCE", "SPAN", "STYLE", "TABLE", "TEXTAREA", "VIDEO", "screenLeft", "screenTop", "screenAvailLeft", "screenAvailTop", "innerWidth", "innerHeight", "outerWidth", "outerHeight", "browserLanguage", "browserLanguages", "systemLanguage", "devicePixelRatio", "colorDepth", "userAgent", "cookieEnabled", "netEnabled", "screenWidth", "screenHeight", "screenAvailWidth", "screenAvailHeight", "localStorageEnabled", "sessionStorageEnabled", "indexedDBEnabled", "CPUClass", "platform", "doNotTrack", "timezone", "canvas2DFP", "canvas3DFP", "plugins", "maxTouchPoints", "flashEnabled", "javaEnabled", "hardwareConcurrency", "jsFonts", "timestamp", "performanceTiming", "internalip", "mediaDevices", "DIV", "P", "UL", "LI", "SCRIPT", "touchEvent"]
    //n['$_BJAc']()
    return new $_DJw($_BJAc)['$_EBL'](function (e) {
        var t = r[e];
        o['push']((void 0 === t) ? -1 : t);
    }), o['join']('!!');

}

function $_DJw(e) {
    this['$_BAEp'] = e || [];
}

$_DJw['prototype'] = {
    '$_EBL': function (e) {
        var t = this['$_BAEp'];
        if (t['map']) return new $_DJw(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1) n[r] = e(t[r], r, this);
        return new $_DJw(n);
    }
}

// ====================获取r的值====================
function $_CCGH(e) {
    var RSA = new JSEncrypt();
    RSA.setPublicKey(get_publickey());
    //this['$_CCHI']
    var t = Buffer.from(RSA['encrypt']($_CCHI(e)), 'base64').toString('hex');
    while (!t || 256 !== t['length']) t = Buffer.from(RSA['encrypt']($_CCHI(e)), 'base64').toString('hex');
    return t;
}

function $_CCHI(e) {
    return t['$_EIi']['aeskey'] && !e || (t['$_EIi']['aeskey'] = te()), t['$_EIi']['aeskey'];
}

function te() {
    return e() + e() + e() + e();
}

function e() {
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function get_publickey() {
    let n = '00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81'; // 模数
    let e = '10001'; // 指数

    let publicKey = new jsrsasign.RSAKey();
    publicKey.setPublic(n, e);
    // 将公钥转换为PEM格式
    return jsrsasign.KEYUTIL.getPEM(publicKey, 'PKCS8PUB');
}

// ====================获取o的值====================
function encrypt1(e, t, n) {
    var data = e;
    var key = CryptoJS.enc.Utf8.parse(t)
    var iv = CryptoJS.enc.Utf8.parse('0000000000000000')
    var r = CryptoJS.AES.encrypt(data, key, {
        'iv': iv, 'mode': CryptoJS.mode.CBC
    })
    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var s = [];
    for (var a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
}

// ====================获取i的值====================
function $_HEv(e) {
    //                     this['$_HCR']
    var t = $_HCR(e);
    return t['res'] + t['end'];
}

function $_HCR(e, o) {
    var i = this;
    o || (o = i);
    for (var t = function (e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            //   i['$_HBX']                    i['$_HBX']
            1 === $_HBX(t, r) && (n = (n << 1) + $_HBX(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var _;
        if (a + 2 < s) _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2], //  i['$_GJr']
            n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)) + $_GJr(t(_, 19220)) + $_GJr(t(_, 235)); else {
            var c = s % 3;
            2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8), n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)) + $_GJr(t(_, 19220)), r = '.') : 1 == c && (_ = e[a] << 16, n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)), r = '.' + '.');
        }
    }
    return {
        'res': n, 'end': r
    };
}

function $_HBX(e, t) {
    return e >> t & 1;
}

function $_GJr(e) {
    var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()";
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}
