const CryptoJS = require('crypto-js');

function wf(e) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
    if (e && "string" === typeof e) {
        var t = n.text || "0"
            , r = n.length || 24;
        if (e.length < r)
            for (var a = e.length; a < r; a++)
                e += t;
        else
            e = e.substring(0, r);
        return e
    }
}

function wc(e) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
        , r = t.enc
        , a = void 0 === r ? "Utf8" : r
        , o = t.mode
        , i = void 0 === o ? "ECB" : o
        , c = t.padding
        , u = void 0 === c ? "Pkcs7" : c
        , d = CryptoJS.enc[a].parse(n)
        , s = {
        mode: CryptoJS.mode[i],
        padding: CryptoJS.pad[u]
    }
        , l = CryptoJS.TripleDES.encrypt(e, d, s);
    return l.toString()
}

function uk() {
    var e, n, t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 32,
        r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 16,
        a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), o = [];
    if (r = r || a.length,
        t)
        for (e = 0; e < t; e++)
            o[e] = a[0 | Math.random() * r];
    else
        for (o[8] = o[13] = o[18] = o[23] = "-",
                 o[14] = "4",
                 e = 0; e < 36; e++)
            o[e] || (n = 0 | 16 * Math.random(),
                o[e] = a[19 === e ? 3 & n | 8 : n]);
    return o.join("")
}


function i(t, e) {
    var n = (65535 & t) + (65535 & e)
        , r = (t >> 16) + (e >> 16) + (n >> 16);
    return r << 16 | 65535 & n
}

function a(t, e) {
    return t << e | t >>> 32 - e
}

function c(t, e, n, r, o, c) {
    return i(a(i(i(e, t), i(r, c)), o), n)
}

function u(t, e, n, r, o, i, a) {
    return c(e & n | ~e & r, t, e, o, i, a)
}

function s(t, e, n, r, o, i, a) {
    return c(e & r | n & ~r, t, e, o, i, a)
}

function f(t, e, n, r, o, i, a) {
    return c(e ^ n ^ r, t, e, o, i, a)
}

function l(t, e, n, r, o, i, a) {
    return c(n ^ (e | ~r), t, e, o, i, a)
}

function p(t, e) {
    var n, r, o, a, c;
    t[e >> 5] |= 128 << e % 32,
        t[14 + (e + 64 >>> 9 << 4)] = e;
    var p = 1732584193
        , h = -271733879
        , d = -1732584194
        , v = 271733878;
    for (n = 0; n < t.length; n += 16)
        r = p,
            o = h,
            a = d,
            c = v,
            p = u(p, h, d, v, t[n], 7, -680876936),
            v = u(v, p, h, d, t[n + 1], 12, -389564586),
            d = u(d, v, p, h, t[n + 2], 17, 606105819),
            h = u(h, d, v, p, t[n + 3], 22, -1044525330),
            p = u(p, h, d, v, t[n + 4], 7, -176418897),
            v = u(v, p, h, d, t[n + 5], 12, 1200080426),
            d = u(d, v, p, h, t[n + 6], 17, -1473231341),
            h = u(h, d, v, p, t[n + 7], 22, -45705983),
            p = u(p, h, d, v, t[n + 8], 7, 1770035416),
            v = u(v, p, h, d, t[n + 9], 12, -1958414417),
            d = u(d, v, p, h, t[n + 10], 17, -42063),
            h = u(h, d, v, p, t[n + 11], 22, -1990404162),
            p = u(p, h, d, v, t[n + 12], 7, 1804603682),
            v = u(v, p, h, d, t[n + 13], 12, -40341101),
            d = u(d, v, p, h, t[n + 14], 17, -1502002290),
            h = u(h, d, v, p, t[n + 15], 22, 1236535329),
            p = s(p, h, d, v, t[n + 1], 5, -165796510),
            v = s(v, p, h, d, t[n + 6], 9, -1069501632),
            d = s(d, v, p, h, t[n + 11], 14, 643717713),
            h = s(h, d, v, p, t[n], 20, -373897302),
            p = s(p, h, d, v, t[n + 5], 5, -701558691),
            v = s(v, p, h, d, t[n + 10], 9, 38016083),
            d = s(d, v, p, h, t[n + 15], 14, -660478335),
            h = s(h, d, v, p, t[n + 4], 20, -405537848),
            p = s(p, h, d, v, t[n + 9], 5, 568446438),
            v = s(v, p, h, d, t[n + 14], 9, -1019803690),
            d = s(d, v, p, h, t[n + 3], 14, -187363961),
            h = s(h, d, v, p, t[n + 8], 20, 1163531501),
            p = s(p, h, d, v, t[n + 13], 5, -1444681467),
            v = s(v, p, h, d, t[n + 2], 9, -51403784),
            d = s(d, v, p, h, t[n + 7], 14, 1735328473),
            h = s(h, d, v, p, t[n + 12], 20, -1926607734),
            p = f(p, h, d, v, t[n + 5], 4, -378558),
            v = f(v, p, h, d, t[n + 8], 11, -2022574463),
            d = f(d, v, p, h, t[n + 11], 16, 1839030562),
            h = f(h, d, v, p, t[n + 14], 23, -35309556),
            p = f(p, h, d, v, t[n + 1], 4, -1530992060),
            v = f(v, p, h, d, t[n + 4], 11, 1272893353),
            d = f(d, v, p, h, t[n + 7], 16, -155497632),
            h = f(h, d, v, p, t[n + 10], 23, -1094730640),
            p = f(p, h, d, v, t[n + 13], 4, 681279174),
            v = f(v, p, h, d, t[n], 11, -358537222),
            d = f(d, v, p, h, t[n + 3], 16, -722521979),
            h = f(h, d, v, p, t[n + 6], 23, 76029189),
            p = f(p, h, d, v, t[n + 9], 4, -640364487),
            v = f(v, p, h, d, t[n + 12], 11, -421815835),
            d = f(d, v, p, h, t[n + 15], 16, 530742520),
            h = f(h, d, v, p, t[n + 2], 23, -995338651),
            p = l(p, h, d, v, t[n], 6, -198630844),
            v = l(v, p, h, d, t[n + 7], 10, 1126891415),
            d = l(d, v, p, h, t[n + 14], 15, -1416354905),
            h = l(h, d, v, p, t[n + 5], 21, -57434055),
            p = l(p, h, d, v, t[n + 12], 6, 1700485571),
            v = l(v, p, h, d, t[n + 3], 10, -1894986606),
            d = l(d, v, p, h, t[n + 10], 15, -1051523),
            h = l(h, d, v, p, t[n + 1], 21, -2054922799),
            p = l(p, h, d, v, t[n + 8], 6, 1873313359),
            v = l(v, p, h, d, t[n + 15], 10, -30611744),
            d = l(d, v, p, h, t[n + 6], 15, -1560198380),
            h = l(h, d, v, p, t[n + 13], 21, 1309151649),
            p = l(p, h, d, v, t[n + 4], 6, -145523070),
            v = l(v, p, h, d, t[n + 11], 10, -1120210379),
            d = l(d, v, p, h, t[n + 2], 15, 718787259),
            h = l(h, d, v, p, t[n + 9], 21, -343485551),
            p = i(p, r),
            h = i(h, o),
            d = i(d, a),
            v = i(v, c);
    return [p, h, d, v]
}

function h(t) {
    var e, n = "", r = 32 * t.length;
    for (e = 0; e < r; e += 8)
        n += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
    return n
}

function d(t) {
    var e, n = [];
    for (n[(t.length >> 2) - 1] = void 0,
             e = 0; e < n.length; e += 1)
        n[e] = 0;
    var r = 8 * t.length;
    for (e = 0; e < r; e += 8)
        n[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
    return n
}

function g(t) {
    var e, n, r = "0123456789abcdef", o = "";
    for (n = 0; n < t.length; n += 1)
        e = t.charCodeAt(n),
            o += r.charAt(e >>> 4 & 15) + r.charAt(15 & e);
    return o
}

function v(t) {
    return h(p(d(t), 8 * t.length))
}

function m(t) {
    return v(unescape(encodeURIComponent(t)))
}

function _(t) {
    return g(m(t))
}

function S(t, e, n) {
    return _(t)
}


function get_params(username, password) {
    var n = (new Date).getTime() - '2712';
    var t = "s54zv9bm1vd5czfujy6nnuxj1l4g2ny6";
    var r = uk();
    var a = S(n + r + S(r + t + n));
    return {
        'username': username,
        'password': encodeURI(wc(password, wf(username))),
        'mainVersion': 300031500,
        'comParam_curTime': n,
        'comParam_seqCode': r,
        'comParam_signature': a,
        'isCheck': true,
        'locale': "zh-cn"


    }
}

// console.log(get_params('18935066921@163.com', '123'))