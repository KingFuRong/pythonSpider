const JSEncrypt = require("node-jsencrypt");


var e, r;
e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
r = {
    rotl: function (t, n) {
        return t << n | t >>> 32 - n
    },
    endian: function (t) {
        if (t.constructor == Number)
            return 16711935 & r.rotl(t, 8) | 4278255360 & r.rotl(t, 24);
        for (var n = 0; n < t.length; n++)
            t[n] = r.endian(t[n]);
        return t
    },
    bytesToWords: function (t) {
        for (var n = [], e = 0, r = 0; e < t.length; e++,
            r += 8)
            n[r >>> 5] |= t[e] << 24 - r % 32;
        return n
    },
    wordsToBytes: function (t) {
        for (var n = [], e = 0; e < 32 * t.length; e += 8)
            n.push(t[e >>> 5] >>> 24 - e % 32 & 255);
        return n
    },
    bytesToHex: function (t) {
        for (var n = [], e = 0; e < t.length; e++)
            n.push((t[e] >>> 4).toString(16)),
                n.push((15 & t[e]).toString(16));
        return n.join("")
    }
}


var f = {};
var c = {};
f.default = function (t, n) {
    var e = {
        utf8: {
            stringToBytes: function (t) {
                return e.bin.stringToBytes(unescape(encodeURIComponent(t)))
            },
            bytesToString: function (t) {
                return decodeURIComponent(escape(e.bin.bytesToString(t)))
            }
        },
        bin: {
            stringToBytes: function (t) {
                for (var n = [], e = 0; e < t.length; e++)
                    n.push(255 & t.charCodeAt(e));
                return n
            },
            bytesToString: function (t) {
                for (var n = [], e = 0; e < t.length; e++)
                    n.push(String.fromCharCode(t[e]));
                return n.join("")
            }
        }
    }
    var i = e.utf8
    var u = e.bin
    var a = function (t, n) {
        t.constructor == String ? t = n && "binary" === n.encoding ? u.stringToBytes(t) : i.stringToBytes(t) : o(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || t.constructor === Uint8Array || (t = t.toString());
        for (var e = r.bytesToWords(t), s = 8 * t.length, f = 1732584193, c = -271733879, h = -1732584194, l = 271733878, p = 0; p < e.length; p++)
            e[p] = 16711935 & (e[p] << 8 | e[p] >>> 24) | 4278255360 & (e[p] << 24 | e[p] >>> 8);
        e[s >>> 5] |= 128 << s % 32,
            e[14 + (s + 64 >>> 9 << 4)] = s;
        var d = a._ff
            , v = a._gg
            , y = a._hh
            , g = a._ii;
        for (p = 0; p < e.length; p += 16) {
            var w = f
                , b = c
                , m = h
                , x = l;
            f = d(f, c, h, l, e[p + 0], 7, -680876936),
                l = d(l, f, c, h, e[p + 1], 12, -389564586),
                h = d(h, l, f, c, e[p + 2], 17, 606105819),
                c = d(c, h, l, f, e[p + 3], 22, -1044525330),
                f = d(f, c, h, l, e[p + 4], 7, -176418897),
                l = d(l, f, c, h, e[p + 5], 12, 1200080426),
                h = d(h, l, f, c, e[p + 6], 17, -1473231341),
                c = d(c, h, l, f, e[p + 7], 22, -45705983),
                f = d(f, c, h, l, e[p + 8], 7, 1770035416),
                l = d(l, f, c, h, e[p + 9], 12, -1958414417),
                h = d(h, l, f, c, e[p + 10], 17, -42063),
                c = d(c, h, l, f, e[p + 11], 22, -1990404162),
                f = d(f, c, h, l, e[p + 12], 7, 1804603682),
                l = d(l, f, c, h, e[p + 13], 12, -40341101),
                h = d(h, l, f, c, e[p + 14], 17, -1502002290),
                f = v(f, c = d(c, h, l, f, e[p + 15], 22, 1236535329), h, l, e[p + 1], 5, -165796510),
                l = v(l, f, c, h, e[p + 6], 9, -1069501632),
                h = v(h, l, f, c, e[p + 11], 14, 643717713),
                c = v(c, h, l, f, e[p + 0], 20, -373897302),
                f = v(f, c, h, l, e[p + 5], 5, -701558691),
                l = v(l, f, c, h, e[p + 10], 9, 38016083),
                h = v(h, l, f, c, e[p + 15], 14, -660478335),
                c = v(c, h, l, f, e[p + 4], 20, -405537848),
                f = v(f, c, h, l, e[p + 9], 5, 568446438),
                l = v(l, f, c, h, e[p + 14], 9, -1019803690),
                h = v(h, l, f, c, e[p + 3], 14, -187363961),
                c = v(c, h, l, f, e[p + 8], 20, 1163531501),
                f = v(f, c, h, l, e[p + 13], 5, -1444681467),
                l = v(l, f, c, h, e[p + 2], 9, -51403784),
                h = v(h, l, f, c, e[p + 7], 14, 1735328473),
                f = y(f, c = v(c, h, l, f, e[p + 12], 20, -1926607734), h, l, e[p + 5], 4, -378558),
                l = y(l, f, c, h, e[p + 8], 11, -2022574463),
                h = y(h, l, f, c, e[p + 11], 16, 1839030562),
                c = y(c, h, l, f, e[p + 14], 23, -35309556),
                f = y(f, c, h, l, e[p + 1], 4, -1530992060),
                l = y(l, f, c, h, e[p + 4], 11, 1272893353),
                h = y(h, l, f, c, e[p + 7], 16, -155497632),
                c = y(c, h, l, f, e[p + 10], 23, -1094730640),
                f = y(f, c, h, l, e[p + 13], 4, 681279174),
                l = y(l, f, c, h, e[p + 0], 11, -358537222),
                h = y(h, l, f, c, e[p + 3], 16, -722521979),
                c = y(c, h, l, f, e[p + 6], 23, 76029189),
                f = y(f, c, h, l, e[p + 9], 4, -640364487),
                l = y(l, f, c, h, e[p + 12], 11, -421815835),
                h = y(h, l, f, c, e[p + 15], 16, 530742520),
                f = g(f, c = y(c, h, l, f, e[p + 2], 23, -995338651), h, l, e[p + 0], 6, -198630844),
                l = g(l, f, c, h, e[p + 7], 10, 1126891415),
                h = g(h, l, f, c, e[p + 14], 15, -1416354905),
                c = g(c, h, l, f, e[p + 5], 21, -57434055),
                f = g(f, c, h, l, e[p + 12], 6, 1700485571),
                l = g(l, f, c, h, e[p + 3], 10, -1894986606),
                h = g(h, l, f, c, e[p + 10], 15, -1051523),
                c = g(c, h, l, f, e[p + 1], 21, -2054922799),
                f = g(f, c, h, l, e[p + 8], 6, 1873313359),
                l = g(l, f, c, h, e[p + 15], 10, -30611744),
                h = g(h, l, f, c, e[p + 6], 15, -1560198380),
                c = g(c, h, l, f, e[p + 13], 21, 1309151649),
                f = g(f, c, h, l, e[p + 4], 6, -145523070),
                l = g(l, f, c, h, e[p + 11], 10, -1120210379),
                h = g(h, l, f, c, e[p + 2], 15, 718787259),
                c = g(c, h, l, f, e[p + 9], 21, -343485551),
                f = f + w >>> 0,
                c = c + b >>> 0,
                h = h + m >>> 0,
                l = l + x >>> 0
        }
        return r.endian([f, c, h, l])
    }
    a._ff = function (t, n, e, r, i, o, u) {
        var a = t + (n & e | ~n & r) + (i >>> 0) + u;
        return (a << o | a >>> 32 - o) + n
    }
    a._gg = function (t, n, e, r, i, o, u) {
        var a = t + (n & r | e & ~r) + (i >>> 0) + u;
        return (a << o | a >>> 32 - o) + n
    }
    a._hh = function (t, n, e, r, i, o, u) {
        var a = t + (n ^ e ^ r) + (i >>> 0) + u;
        return (a << o | a >>> 32 - o) + n
    }
    a._ii = function (t, n, e, r, i, o, u) {
        var a = t + (e ^ (n | ~r)) + (i >>> 0) + u;
        return (a << o | a >>> 32 - o) + n
    }
    a._blocksize = 16
    a._digestsize = 16

    if (null == t)
        throw new Error("Illegal argument " + t);
    var e = r.wordsToBytes(a(t, n));
    return r.bytesToHex(e)
}
c.default = function (t, e) {
    var e = {
        utf8: {
            stringToBytes: function (t) {
                return e.bin.stringToBytes(unescape(encodeURIComponent(t)))
            },
            bytesToString: function (t) {
                return decodeURIComponent(escape(e.bin.bytesToString(t)))
            }
        },
        bin: {
            stringToBytes: function (t) {
                for (var n = [], e = 0; e < t.length; e++)
                    n.push(255 & t.charCodeAt(e));
                return n
            },
            bytesToString: function (t) {
                for (var n = [], e = 0; e < t.length; e++)
                    n.push(String.fromCharCode(t[e]));
                return n.join("")
            }
        }
    }
    var i = e.utf8
    var o = e.bin
    var u = r.wordsToBytes(function (t) {
        t.constructor == String ? t = i.stringToBytes(t) : void 0 !== n && "function" == typeof n.isBuffer && n.isBuffer(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
        var e = r.bytesToWords(t)
            , o = 8 * t.length
            , u = []
            , a = 1732584193
            , s = -271733879
            , f = -1732584194
            , c = 271733878
            , h = -1009589776;
        e[o >> 5] |= 128 << 24 - o % 32,
            e[15 + (o + 64 >>> 9 << 4)] = o;
        for (var l = 0; l < e.length; l += 16) {
            for (var p = a, d = s, v = f, y = c, g = h, w = 0; w < 80; w++) {
                if (w < 16)
                    u[w] = e[l + w];
                else {
                    var b = u[w - 3] ^ u[w - 8] ^ u[w - 14] ^ u[w - 16];
                    u[w] = b << 1 | b >>> 31
                }
                var m = (a << 5 | a >>> 27) + h + (u[w] >>> 0) + (w < 20 ? 1518500249 + (s & f | ~s & c) : w < 40 ? 1859775393 + (s ^ f ^ c) : w < 60 ? (s & f | s & c | f & c) - 1894007588 : (s ^ f ^ c) - 899497514);
                h = c,
                    c = f,
                    f = s << 30 | s >>> 2,
                    s = a,
                    a = m
            }
            a += p,
                s += d,
                f += v,
                c += y,
                h += g
        }
        return [a, s, f, c, h]
    }(t));
    return e && e.asBytes ? u : e && e.asString ? o.bytesToString(u) : r.bytesToHex(u)
}

function get_params(n) {
    var u = 'POST';
    var a = "application/json";
    var s = f.default(n);
    var h = {};
    h["type"] = a;
// var l = new Blob([n], h)['size'];
    var l = Buffer.from(n).length;
    var p = parseInt(Date.now() / 1e3, 10);
    var d = '114e9f56fb2055309c9b90bc38fdd7c5';
    var v = c.default([u, s, a, l, p, d].join("\n"));
    var y = {
        'timestamp': p,
        'verification': v,
    };
    return y;
}

function RSAEncrypt(n) {
    var RSA = new JSEncrypt();
    RSA.setPublicKey('-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDvekdPMHN3AYhm/vktJT+YJr7\ncI5DcsNKqdsx5DZX0gDuWFuIjzdwButrIYPNmRJ1G8ybDIF7oDW2eEpm5sMbL9zs\n9ExXCdvqrn51qELbqj0XxtMTIpaCHFSI50PfPpTFV9Xt/hmyVwokoOXFlAEgCn+Q\nCgGs52bFoYMtyi+xEQIDAQAB\n-----END PUBLIC KEY-----');
    return RSA.encrypt(n)
}

