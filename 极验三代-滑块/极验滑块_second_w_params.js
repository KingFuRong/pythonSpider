const Crypto = require("crypto");
const CryptoJS = require("crypto-js");

var window = global;
var i = {};
var mouse_time = new Date().getTime();
var mouse_track = [["down", 755, 107, mouse_time, "pointerdown"], ["focus", mouse_time], ["up", 755, 107, mouse_time + Crypto.randomInt(50, 300), "pointerup"]];
var environment_check_time = mouse_time - Crypto.randomInt(200, 1000)

function $_DJS(e) {
    this['$_BAEy'] = e || [];
}

$_DJS['prototype'] = {
    '$_EHQ': function (e) {
        var t = this['$_BAEy'];
        if (t['indexOf']) return t['indexOf'](e);
        for (var n = 0, r = t['length']; n < r; n += 1) if (t[n] === e) return n;
        return -1;
    },
    '$_EBs': function (e) {
        var t = this['$_BAEy'];
        if (t['map'])
            return new $_DJS(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1)
            n[r] = e(t[r], r, this);
        return new $_DJS(n);
    },
}

function De() {
    this['$_BGC'] = this['$_BGHp']();
}

De['prototype'] = {
    "$_BGHp": function () {
        return {};
    },
    '$_BIDy': -1,
    '$_BIHJ': function (e) {
        return void 0 === e;
    },
    '$_BIIC': ['A', 'ARTICLE', 'ASIDE', 'AUDIO', 'BASE', 'BUTTON', 'CANVAS', 'CODE', 'IFRAME', 'IMG', 'INPUT', 'LABEL', 'LINK', 'NAV', 'OBJECT', 'OL', 'PICTURE', 'PRE', 'SECTION', 'SELECT', 'SOURCE', 'SPAN', 'STYLE', 'TABLE', 'TEXTAREA', 'VIDEO'],
    '$_BIJx': ['DIV', 'P', 'UL', 'LI', 'SCRIPT'],
    '$_BJAl': function () {
        return ['textLength', 'HTMLLength', 'documentMode']['concat'](this['$_BIIC'])['concat'](['screenLeft', 'screenTop', 'screenAvailLeft', 'screenAvailTop', 'innerWidth', 'innerHeight', 'outerWidth', 'outerHeight', 'browserLanguage', 'browserLanguages', 'systemLanguage', 'devicePixelRatio', 'colorDepth', 'userAgent', 'cookieEnabled', 'netEnabled', 'screenWidth', 'screenHeight', 'screenAvailWidth', 'screenAvailHeight', 'localStorageEnabled', 'sessionStorageEnabled', 'indexedDBEnabled', 'CPUClass', 'platform', 'doNotTrack', 'timezone', 'canvas2DFP', 'canvas3DFP', 'plugins', 'maxTouchPoints', 'flashEnabled', 'javaEnabled', 'hardwareConcurrency', 'jsFonts', 'timestamp', 'performanceTiming', 'internalip', 'mediaDevices'])['concat'](this['$_BIJx'])['concat'](['touchEvent']);
    }
}

function $_BHJg(e) {
    var t = '', n = 0;
    (e || [])['length'];
    while (!t && e[n]) t = e[n] && e[n][4], n++;
    if (!t) return e;
    for (var r = '', o = ['mouse', 'touch', 'pointer', 'MSPointer'], i = 0, s = o['length']; i < s; i++) 0 === t['indexOf'](o[i]) && (r = o[i]);
    for (var a = e['slice'](), _ = a['length'] - 1; 0 <= _; _--) {
        var c = a[_], l = c[0];
        if (-1 < new $_DJS(['move', 'down', 'up'])['$_EHQ'](l)) 0 !== (c[4] || '')['indexOf'](r) && a['splice'](_, 1);
    }
    return a;
}

function $_BHHL(e) {
    var t = 32767;
    return 'number' != typeof e ? e : (t < e ? e = t : e < -t && (e = -t), Math['round'](e));
}

function $_BHIG(e) {
    var t = 0, n = 0, r = [], o = {}, i = 0; // o['lastTime']
    if (e['length'] <= 0) return [];
    for (var s = null, a = null, _ = $_BHJg(e), c = _['length'], l = c < 300 ? 0 : c - 300; l < c; l += 1) {
        var u = _[l], p = u[0];
        -1 < new $_DJS(['down', 'move', 'up', 'scroll'])['$_EHQ'](p) ? (s || (s = u), a = u, r['push']([p, [u[1] - t, u[2] - n], $_BHHL(i ? u[3] - i : i)]), t = u[1], n = u[2], i = u[3]) : -1 < new $_DJS(['blur', 'focus', 'unload'])['$_EHQ'](p) && (r['push']([p, $_BHHL(i ? u[1] - i : i)]), i = u[1]);
    }
    return o['$_BGBT'] = s, o['$_BGC_'] = a, r;
}

function $_HDz(e) {
    var p = {
        'move': 0, 'down': 1, 'up': 2, 'scroll': 3, 'focus': 4, 'blur': 5, 'unload': 6, 'unknown': 7
    };

    function h(e, t) {
        for (var n = e['toString'](2), r = '', o = n['length'] + 1; o <= t; o += 1) r += '0';
        return n = r + n;
    }

    function f(e) {
        var t = [], n = e['length'], r = 0;
        while (r < n) {
            var o = e[r], i = 0;
            while (1) {
                if (16 <= i) break;
                var s = r + i + 1;
                if (n <= s) break;
                if (e[s] !== o) break;
                i += 1;
            }
            r = r + 1 + i;
            var a = p[o];
            0 != i ? (t['push'](8 | a), t['push'](i - 1)) : t['push'](a);
        }
        for (var _ = h(32768 | n, 16), c = '', l = 0, u = t['length']; l < u; l += 1) c += h(t[l], 4);
        return _ + c;
    }

    function c(e, t) {
        for (var n = [], r = 0, o = e['length']; r < o; r += 1) n['push'](t(e[r]));
        return n;
    }

    function d(e, t) {
        e = function _(e) {
            var t = 32767, n = (e = c(e, function (e) {
                return t < e ? t : e < -t ? -t : e;
            }))['length'], r = 0, o = [];
            while (r < n) {
                var i = 1, s = e[r], a = Math['abs'](s);
                while (1) {
                    if (n <= r + i) break;
                    if (e[r + i] !== s) break;
                    if (127 <= a || 127 <= i) break;
                    i += 1;
                }
                1 < i ? o['push']((s < 0 ? 49152 : 32768) | i << 7 | a) : o['push'](s), r += i;
            }
            return o;
        }(e);
        var n, r = [], o = [];
        c(e, function (e) {
            var t = Math['ceil'](function n(e, t) {
                return 0 === e ? 0 : Math['log'](e) / Math['log'](t);
            }(Math['abs'](e) + 1, 16));
            0 === t && (t = 1), r['push'](h(t - 1, 2)), o['push'](h(Math['abs'](e), 4 * t));
        });
        var i = r['join'](''), s = o['join']('');
        return n = t ? c(function a(e, t) {
            var n = [];
            return c(e, function (e) {
                t(e) && n['push'](e);
            }), n;
        }(e, function (e) {
            return 0 != e && e >> 15 != 1;
        }), function (e) {
            return e < 0 ? '1' : '0';
        })['join']('') : '', h(32768 | e['length'], 16) + i + s + n;
    }

    return function (e) {
        for (var t = [], n = [], r = [], o = [], i = 0, s = e['length']; i < s; i += 1) {
            var a = e[i], _ = a['length'];
            t['push'](a[0]), n['push'](2 === _ ? a[1] : a[2]), 3 === _ && (r['push'](a[1][0]), o['push'](a[1][1]));
        }
        var c = f(t) + d(n, !1) + d(r, !0) + d(o, !0), l = c['length'];
        return l % 6 != 0 && (c += h(0, 6 - l % 6)), function u(e) {
            for (var t = '', n = e['length'] / 6, r = 0; r < n; r += 1) t += '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz~'['charAt'](window['parseInt'](e['slice'](6 * r, 6 * (r + 1)), 2));
            return t;
        }(c);
    }(e);
}

function $_HCN(e, o) {
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

function assignment_i(gt, challenge, aeskey, param_s, fingerprint) {
    function p_$_HDz(e) {
        var t = $_HCN($_GHQ(e));
        return t['res'] + t['end'];
    }

    function $_GHQ(e) {
        for (var t = [], n = 0, r = e['length']; n < r; n += 1)
            t['push'](e['charCodeAt'](n));
        return t;
    }

    function H(e) {
        return Crypto.createHash('md5').update(e).digest('hex')
    }

    i['$_BJJL'] = {}
    i['$_BJCN'] = {}
    i['$_BDHc'] = {}
    i['$_BJJL']['$_BIBv'] = function () {
        var e = mouse_track;
        mouse_track = [];
        return $_HDz($_BHIG(e))
    }
    i['$_BJJL']['$_BICE'] = function () {
        return $_HDz(mouse_track);
    }
    i['$_BJCN']['$_BICE'] = function (e, t) {
        var n = new De()
            , r = n['$_BGC']
            , o = [];
        return new $_DJS(n['$_BJAl']())['$_EBs'](function (e) {
            var t = r[e];
            o['push'](n['$_BIHJ'](t) ? n['$_BIDy'] : t);
        }),
            o['join']('magic data');
    }
    i['$_CEDX'] = {
        "v": "9.1.9-eyz9lh",
        "te": false,
        "$_BBb": true,
        "ven": "Google Inc. (NVIDIA)",
        "ren": "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Laptop GPU (0x00002560) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "fp": mouse_track.slice(0, 1)[0],
        "lp": mouse_track.slice(-1)[0],
        "em": {
            "ph": 0,
            "cp": 0,
            "ek": "11",
            "wd": 1,
            "nt": 0,
            "si": 0,
            "sc": 0
        },
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
        "dnf": "dnf",
        "by": 0
    }

    var e = i['$_BJJL']['$_BIBv']();
    var t = i['$_BJJL']['$_BICE']();
    var n = i['$_BJCN']['$_BICE']();
    var r = 'DIV_0' // i['$_BDHc']['$_BIBv']();
    var o = {
        "$_CAAM": Date.now(),
        "protocol": "https://",
        "gt": gt,
        "challenge": challenge,
        "offline": false,
        "new_captcha": true,
        "product": "popup",
        "width": "300px",
        "https": true,
        "api_server": "api.geetest.com",
        "type": "fullpage",
        "static_servers": [
            "static.geetest.com",
            "static.geevisit.com"
        ],
        "beeline": "/static/js/beeline.1.0.1.js",
        "voice": "/static/js/voice.1.2.4.js",
        "click": "/static/js/click.3.1.0.js",
        "fullpage": "/static/js/fullpage.9.1.9-eyz9lh.js",
        "slide": "/static/js/slide.7.9.2.js",
        "geetest": "/static/js/geetest.6.0.9.js",
        "aspect_radio": {
            "slide": 103,
            "click": 128,
            "voice": 128,
            "beeline": 50
        },
        "cc": 16,
        "supportWorker": true,
        "$_FFq": {
            "pt": 0
        },
        "aeskey": aeskey,
        "theme": "wind",
        "theme_version": "1.5.8",
        "logo": true,
        "feedback": "https://www.geetest.com/contact#report",
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
        "i18n_labels": {
            "copyright": "由极验提供技术支持",
            "error": "网络不给力",
            "error_content": "请点击此处重试",
            "error_title": "网络超时",
            "fullpage": "智能检测中",
            "goto_cancel": "取消",
            "goto_confirm": "前往",
            "goto_homepage": "是否前往验证服务Geetest官网",
            "loading_content": "智能验证检测中",
            "next": "正在加载验证",
            "next_ready": "请完成验证",
            "read_reversed": false,
            "ready": "点击按钮进行验证",
            "refresh_page": "页面出现错误啦！要继续操作，请刷新此页面",
            "reset": "请点击重试",
            "success": "验证成功",
            "success_title": "通过验证"
        }
    };
    var s = Crypto.randomInt(200, 3000);  // $_GC() - rt;
    i['$_CECe'] = '';
    for (var a = [['lang', o['lang'] || 'zh-cn'], ['type', 'fullpage'], ['tt', function (e, t, n) {
        if (!t || !n) return e;
        var r, o = 0, i = e, s = t[0], a = t[2], _ = t[4];
        while (r = n['substr'](o, 2)) {
            o += 2;
            var c = parseInt(r, 16), l = String['fromCharCode'](c), u = (s * c * c + a * c + _) % e['length'];
            i = i['substr'](0, u) + l + i['substr'](u);
        }
        return i;
    }(e, o['c'], o['s']) || -1], ['light', r || -1], ['s', H(p_$_HDz(t))], ['h', H(p_$_HDz(n))], ['hh', H(n)], ['hi', H(fingerprint)], ['vip_order', i['vip_order'] || -1], ['ct', i['ct'] || -1], ['ep', i['$_CEDX'] || -1], ['passtime', s || -1], ['rp', H(o['gt'] + o['challenge'] + s)]], _ = 0; _ < a['length']; _++)
        i['$_CECe'] += '"' + a[_][0] + '":' + JSON['stringify'](a[_][1]) + ',';
}

function $_HED(e) {
    var t = $_HCN(e);
    return t['res'] + t['end'];
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

function second_get_params(gt, challenge, aeskey, param_s, fingerprint, e) {
    assignment_i(gt, challenge, aeskey, param_s, fingerprint)
    var t = ["bbOy"]
    t['push'](e['toString']());
    var r = '';

    var o_toString = "function o(e,t){var $_CFGDg=hZohI.$_CQ,$_CFGCD=['$_CFGGV'].concat($_CFGDg),$_CFGEq=$_CFGCD[1];$_CFGCD.shift();var $_CFGFQ=$_CFGCD[0];function n(e){var $_DDHGA=hZohI.$_Dd()[0][16];for(;$_DDHGA!==hZohI.$_Dd()[9][13];){switch($_DDHGA){case hZohI.$_Dd()[9][16]:var t=5381,n=e[$_CFGEq(81)],r=0;$_DDHGA=hZohI.$_Dd()[3][15];break;case hZohI.$_Dd()[3][15]:while(n--)t=(t<<5)+t+e[$_CFGDg(31)](r++);$_DDHGA=hZohI.$_Dd()[0][14];break;case hZohI.$_Dd()[9][14]:return t&=~(1<<31);break;}}}100<new Date()[$_CFGDg(200)]()-t[$_CFGDg(200)]()&&(e=$_CFGEq(1152)),r=$_CFGEq(766)+i[$_CFGEq(1109)]+$_CFGEq(1188)+n(o[$_CFGEq(47)]()+n(n[$_CFGDg(47)]())+n(e[$_CFGDg(47)]()))+$_CFGEq(1122);}";
    var n_toString = "function n(e){var $_DDHGA=hZohI.$_Dd()[0][16];for(;$_DDHGA!==hZohI.$_Dd()[9][13];){switch($_DDHGA){case hZohI.$_Dd()[9][16]:var t=5381,n=e[$_CFGEq(81)],r=0;$_DDHGA=hZohI.$_Dd()[3][15];break;case hZohI.$_Dd()[3][15]:while(n--)t=(t<<5)+t+e[$_CFGDg(31)](r++);$_DDHGA=hZohI.$_Dd()[0][14];break;case hZohI.$_Dd()[9][14]:return t&=~(1<<31);break;}}}"

    !function o(e, t) {
        function n(e) {
            var t = 5381, n = e['length'], r = 0;
            while (n--) t = (t << 5) + t + e['charCodeAt'](r++);
            return t &= ~(1 << 31);
        }

        100 < new Date()['getTime']() - t['getTime']() && (e = 'qwe');

        r = '{' + i['$_CECe'] + '"captcha_token":"' + n(o_toString + n(n_toString) + n(e['toString']())) + '","sugd":"lyaxkuq4"}';

    }(t['shift'](), new Date())
    return $_HED(encrypt(r, aeskey));
}
