const Crypto = require("crypto");
const JSEncrypt = require("node-jsencrypt");
const CryptoJS = require("crypto-js");
const jsrsasign = require("jsrsasign");

var window = global;

var environment_check_time = Date.now() - 300;

function H(t, e) {
    for (var n = e['slice'](-2), r = [], i = 0; i < n['length']; i++) {
        var o = n['charCodeAt'](i);
        r[i] = 57 < o ? o - 87 : o - 48;
    }
    n = 36 * r[0] + r[1];
    var s, a = Math['round'](t) + n, _ = [[], [], [], [], []], c = {}, u = 0;
    i = 0;

    for (var l = (e = e['slice'](0, -2))['length']; i < l; i++)
        c[s = e['charAt'](i)] || (c[s] = 1,
            _[u]['push'](s),
            u = 5 == ++u ? 0 : u);
    var h, f = a, d = 4, p = '', g = [1, 2, 5, 10, 50];
    while (0 < f)
        0 <= f - g[d] ? (h = parseInt(Math['random']() * _[d]['length'], 10),
            p += _[d][h],
            f -= g[d]) : (_['splice'](d, 1),
            g['splice'](d, 1),
            d -= 1);
    return p;
}

window['_gct'] = function (t) {
    return StJC(t);
}

function StJC(t) {
    if (t['lang'] && t['ep']) {
        t['h9s9'] = '1803797734';
    }

    function Oo() {
        this['lang'] = t['lang'];
        this['ep'] = t['ep'];
    }

    Oo['prototype'] = new Tr_m();

    function Tr_m() {
    }

    Tr_m['prototype']['gg'] = {
        "n": function HLmT() {
        },
        "s": function FQJF() {
        },
        "e": function li() {
        },
        "es": function MkMS(e) {
            var n = 2;
            var r = '-';
            var i = '-';
            var o = '--';
            var e = e;

            function GPlY() {
                try {
                    if (e['random']['length']) {
                        e['VXMP']({
                            "position": n,
                            "inner": r,
                            "middle": i,
                            "outside": o
                        });
                    }
                } catch (t) {
                }
            }

            return {
                "cc": GPlY
            };
        },
        "en": function IDrp(e) {
            var n = 4;
            var r = '-';
            var i = '-';
            var o = '-';
            var e = e;

            function GPlY() {
                try {
                    if (e['random']['length']) {
                        e['VXMP']({
                            "position": n,
                            "inner": r,
                            "middle": i,
                            "outside": o
                        });
                    }
                } catch (t) {
                }
            }

            return {
                "cc": GPlY
            };
        },
        "w": function KJrn(e) {
            var n = 7;
            var r = '--';
            var i = '-';
            var o = '--';
            var e = e;

            function GPlY() {

                try {
                    if (e['random']['length']) {
                        e['VXMP']({
                            "position": n,
                            "inner": r,
                            "middle": i,
                            "outside": o
                        });
                    }
                } catch (t) {
                }

            }

            return {
                "cc": GPlY
            };
        },
        "wn": function LEZA() {
        },
        "ws": function JVPR() {
        },
        "f": function QKBQ(t, e) {
            try {
                this['query'] = Object['create'](t);
                this['error'] = [];
                this['random'] = this['query'][e] ? this['query'][e]['toString']()['split']('') : '';
                this['addition'] = '-';
                this['multiplication'] = '--';
            } catch (n) {
            }
        }
    };
    return new Oo();
}

function ct(t) {
    this['$_BCAO'] = t || [];
}

ct['prototype'] = {
    '$_CAE': function (t) {
        var e = this['$_BCAO'];
        if (e['map'])
            return new ct(e['map'](t));
        for (var n = [], r = 0, i = e['length']; r < i; r += 1)
            n[r] = t(e[r], r, this);
        return new ct(n);
    }
}

function calculate_l(slide_track, s) {
    var n = {};
    n['$_CICO'] = {
        // 轨迹
        "$_HCb": slide_track,
        '$_BBED': function (t, e, n) {
            if (!e || !n)
                return t;
            var r, i = 0, o = t, s = e[0], a = e[2], _ = e[4];
            while (r = n['substr'](i, 2)) {
                i += 2;
                var c = parseInt(r, 16)
                    , u = String['fromCharCode'](c)
                    , l = (s * c * c + a * c + _) % t['length'];
                o = o['substr'](0, l) + u + o['substr'](l);
            }
            return o;
        },
        '$_FD_': function () {
            function n(t) {
                var e = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
                    , n = e['length']
                    , r = ''
                    , i = Math['abs'](t)
                    , o = parseInt(i / n);
                n <= o && (o = n - 1),
                o && (r = e['charAt'](o));
                var s = '';
                return t < 0 && (s += '!'),
                r && (s += '$'),
                s + r + e['charAt'](i %= n);
            }

            var t = function (t) {
                for (var e, n, r, i = [], o = 0, s = 0, a = t['length'] - 1; s < a; s++)
                    e = Math['round'](t[s + 1][0] - t[s][0]),
                        n = Math['round'](t[s + 1][1] - t[s][1]),
                        r = Math['round'](t[s + 1][2] - t[s][2]),
                    0 == e && 0 == n && 0 == r || (0 == e && 0 == n ? o += r : (i['push']([e, n, r + o]),
                        o = 0));
                return 0 !== o && i['push']([e, n, o]),
                    i;
            }(this['$_HCb'])
                , r = []
                , i = []
                , o = [];
            return new ct(t)['$_CAE'](function (t) {
                var e = function (t) {
                    for (var e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], n = 0, r = e['length']; n < r; n++)
                        if (t[0] == e[n][0] && t[1] == e[n][1])
                            return 'stuvwxyz~'[n];
                    return 0;
                }(t);
                e ? i['push'](e) : (r['push'](n(t[0])),
                    i['push'](n(t[1]))),
                    o['push'](n(t[2]));
            }),
            r['join']('') + '!!' + i['join']('') + '!!' + o['join']('');
        },
    };
    n['$_CJk'] = {};
    n['$_CJk']['c'] = [12, 58, 98, 36, 43, 95, 62, 15, 12];
    n['$_CJk']['s'] = s;
    return n['$_CICO']['$_BBED'](n['$_CICO']['$_FD_'](), n['$_CJk']['c'], n['$_CJk']['s']);
}

function X(e) {
    return Crypto.createHash('md5').update(e).digest('hex')
}

function t() {
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function rt() {
    return t() + t() + t() + t();
}

var Ot = rt()

function $_CCEc(t) {
    return Ot;
}

function $_CCDm(e) {
    var RSA = new JSEncrypt();
    RSA.setPublicKey(get_publickey());
    var t = Buffer.from(RSA['encrypt']($_CCEc(e)), 'base64').toString('hex');
    while (!t || 256 !== t['length']) t = Buffer.from(RSA['encrypt']($_CCEc(e)), 'base64').toString('hex');
    return t;
}

function $_FCD(e, o) {
    var i = this;
    o || (o = i);
    for (var t = function (e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            //   i['$_HBX']                    i['$_HBX']
            1 === $_FBm(t, r) && (n = (n << 1) + $_FBm(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var _;
        if (a + 2 < s) _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2], //  i['$_GJr']
            n += $_EJu(t(_, 7274496)) + $_EJu(t(_, 9483264)) + $_EJu(t(_, 19220)) + $_EJu(t(_, 235)); else {
            var c = s % 3;
            2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8), n += $_EJu(t(_, 7274496)) + $_EJu(t(_, 9483264)) + $_EJu(t(_, 19220)), r = '.') : 1 == c && (_ = e[a] << 16, n += $_EJu(t(_, 7274496)) + $_EJu(t(_, 9483264)), r = '.' + '.');
        }
    }
    return {
        'res': n, 'end': r
    };
}

function $_FBm(e, t) {
    return e >> t & 1;
}

function $_EJu(e) {
    var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()";
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}

function $_FEX(t) {
    var e = $_FCD(t);
    return e['res'] + e['end'];
}

function third_w_params(gt, challenge, id, bg, fullbg, slice, param_s, slice_distance, slide_track, slice_time) {
    // 原始应该传入的参数
    var t = slice_distance; // 滑动距离
    var e = calculate_l(slide_track, param_s); // 轨迹
    var n = slice_time; // 滑动时间


    var r = {};
    var i = {
        "$_GIF": Date.now(),
        "protocol": "https://",
        "is_next": true,
        "type": "multilink",
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "https": true,
        "offline": false,
        "product": "popup",
        "api_server": "https://api.geetest.com",
        "static_servers": [
            "static.geetest.com/",
            "static.geevisit.com/"
        ],
        "isPC": true,
        "autoReset": true,
        "width": "100%",
        "$_DHX": {
            "$_BCN": 0
        },
        "id": id,
        "bg": bg,
        "fullbg": fullbg,
        "link": "",
        "ypos": 54,
        "xpos": 0,
        "height": 160,
        "slice": slice,
        "mobile": true,
        "theme": "ant",
        "theme_version": "1.2.6",
        "template": "",
        "logo": true,
        "clean": false,
        "fullpage": false,
        "feedback": "https://www.geetest.com/contact#report",
        "show_delay": 250,
        "hide_delay": 800,
        "benchmark": false,
        "version": "6.0.9",
        "show_voice": true,
        "c": [
            12,
            58,
            98,
            36,
            43,
            95,
            62,
            15,
            12
        ],
        "s": param_s,
        "so": 0,
        "i18n_labels": {
            "cancel": "取消",
            "close": "关闭验证",
            "error": "请重试",
            "fail": "请正确拼合图像",
            "feedback": "帮助反馈",
            "forbidden": "怪物吃了拼图，请重试",
            "loading": "加载中...",
            "logo": "由极验提供技术支持",
            "read_reversed": false,
            "refresh": "刷新验证",
            "slide": "拖动滑块完成拼图",
            "success": "sec 秒的速度超过 score% 的用户",
            "tip": "请完成下方验证",
            "voice": "视觉障碍"
        },
        "gct_path": "/static/js/gct.b71a9027509bc6bcfef9fc6a196424f5.js"
    };
    var o = {
        "lang": 'zh-cn',
        "userresponse": H(t, i['challenge']),
        "passtime": n,
        "imgload": Crypto.randomInt(100, 300),
        "aa": e,
        "ep": {
            "v": "7.9.2",
            "$_BIE": false,
            "me": true,
            "tm": {
                "a": environment_check_time,
                "b": environment_check_time + 200,
                "c": environment_check_time + 200,
                "d": 0,
                "e": 0,
                "f": environment_check_time + 1,
                "g": environment_check_time + 1,
                "h": environment_check_time + 1,
                "i": environment_check_time + 1,
                "j": environment_check_time + 1,
                "k": 0,
                "l": environment_check_time + 5,
                "m": environment_check_time + 180,
                "n": environment_check_time + 185,
                "o": environment_check_time + 190,
                "p": environment_check_time + 400,
                "q": environment_check_time + 400,
                "r": environment_check_time + 400,
                "s": environment_check_time + 420,
                "t": environment_check_time + 420,
                "u": environment_check_time + 420
            },
            "td": -1
        }
    };

    // if (window['_gct']) {
    //     var s = {
    //         "lang": o['lang'],
    //         "ep": o['ep']
    //     }
    //         , a = window['_gct'](s);
    //     if (a['lang']) {
    //         var _ = function d(t) {
    //             for (var e in t)
    //                 if ('ep' !== e && 'lang' !== e)
    //                     return e;
    //         }(s)
    //         var c = function p(t, e, n) {
    //             var r = new t[('gg')][('f')](e, n);
    //             var i = ['n', 's', 'e', 'es', 'en', 'w', 'wn', 'ws'];
    //             var o = i['length'] - 2;
    //             for (var s = 0; s < n['length']; s++) {
    //                 var a, _ = Math['abs'](n[s]['charCodeAt']() - 70)['toString']()[1];
    //                 a = o < _ ? t['gg'][i[1 + o]](r) : t['gg'][i[_]](r);
    //                 for (var c = Math['abs'](n[s]['charCodeAt']() - 70)['toString']()[0], u = 0; u < c; u++)
    //                     a['cc']();
    //             }
    //             return r['random']['join']('')['slice'](0, 10);
    //         }(a, s, _);
    //         s[_] = c;
    //     }
    //     !function g(t) {
    //         if ('function' == typeof Object['assign'])
    //             return Object['assign']['apply'](Object, arguments);
    //         if (null == t)
    //             throw new Error('Cannot convert undefined or null to object');
    //         t = Object(t);
    //         for (var e = 1; e < arguments['length']; e++) {
    //             var n = arguments[e];
    //             if (null !== n)
    //                 for (var r in n)
    //                     Object['prototype']['hasOwnProperty']['call'](n, r) && (t[r] = n[r]);
    //         }
    //         return t;
    //     }(o, s);
    // }
    //
    // i['offline'] && (o['x'] = t),
    o['rp'] = X(i['gt'] + i['challenge']['slice'](0, 32) + o['passtime']);
    o['h9s9'] = "1816378497";
    var u = $_CCDm()
        , l = encrypt(JSON['stringify'](o), $_CCEc())
        , h = $_FEX(l)
        , f = {
        "gt": i['gt'],
        "challenge": i['challenge'],
        "lang": o['lang'],
        "$_BCN": 0,
        "client_type": 'web',
        "w": h + u
    };
    return f;
}

function encrypt(e, t, n) {
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

function get_publickey() {
    let n = '00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81'; // 模数
    let e = '10001'; // 指数

    let publicKey = new jsrsasign.RSAKey();
    publicKey.setPublic(n, e);
    // 将公钥转换为PEM格式
    return jsrsasign.KEYUTIL.getPEM(publicKey, 'PKCS8PUB');
}

