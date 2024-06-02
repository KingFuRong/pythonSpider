window = {}

function oo0O0(mw) {
    window.b = 'dmFyIGhleGNhc2U9MDt2YXIgYjY0cGFkPSIiO3ZhciBjaHJzej0xNjtmdW5jdGlvbiBoZXhfbWQ1KGEpe3JldHVybiBiaW5sMmhleChjb3JlX21kNShzdHIyYmlubChhKSxhLmxlbmd0aCpjaHJzeikpfWZ1bmN0aW9uIGI2NF9tZDUoYSl7cmV0dXJuIGJpbmwyYjY0KGNvcmVfbWQ1KHN0cjJiaW5sKGEpLGEubGVuZ3RoKmNocnN6KSl9ZnVuY3Rpb24gc3RyX21kNShhKXtyZXR1cm4gYmlubDJzdHIoY29yZV9tZDUoc3RyMmJpbmwoYSksYS5sZW5ndGgqY2hyc3opKX1mdW5jdGlvbiBoZXhfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJoZXgoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBiNjRfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJiNjQoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBzdHJfaG1hY19tZDUoYSxiKXtyZXR1cm4gYmlubDJzdHIoY29yZV9obWFjX21kNShhLGIpKX1mdW5jdGlvbiBtZDVfdm1fdGVzdCgpe3JldHVybiBoZXhfbWQ1KCJhYmMiKT09IjkwMDE1MDk4M2NkMjRmYjBkNjk2M2Y3ZDI4ZTE3ZjcyIn1mdW5jdGlvbiBjb3JlX21kNShwLGspe3Bbaz4+NV18PTEyODw8KChrKSUzMik7cFsoKChrKzY0KT4+PjkpPDw0KSsxNF09azt2YXIgbz0xNzMyNTg0MTkzO3ZhciBuPS0yNzE3MzM4Nzk7dmFyIG09LTE3MzI1ODQxOTQ7dmFyIGw9MjcxNzMzODc4O2Zvcih2YXIgZz0wO2c8cC5sZW5ndGg7Zys9MTYpe3ZhciBqPW87dmFyIGg9bjt2YXIgZj1tO3ZhciBlPWw7bz1tZDVfZmYobyxuLG0sbCxwW2crMF0sNywtNjgwOTc2OTM2KTtsPW1kNV9mZihsLG8sbixtLHBbZysxXSwxMiwtMzg5NTY0NTg2KTttPW1kNV9mZihtLGwsbyxuLHBbZysyXSwxNyw2MDYxMDU4MTkpO249bWQ1X2ZmKG4sbSxsLG8scFtnKzNdLDIyLC0xMDQ0NTI1MzMwKTtvPW1kNV9mZihvLG4sbSxsLHBbZys0XSw3LC0xNzY0MTg4OTcpO2w9bWQ1X2ZmKGwsbyxuLG0scFtnKzVdLDEyLDEyMDAwODA0MjYpO209bWQ1X2ZmKG0sbCxvLG4scFtnKzZdLDE3LC0xNDczMjMxMzQxKTtuPW1kNV9mZihuLG0sbCxvLHBbZys3XSwyMiwtNDU3MDU5ODMpO289bWQ1X2ZmKG8sbixtLGwscFtnKzhdLDcsMTc3MDAzNTQxNik7bD1tZDVfZmYobCxvLG4sbSxwW2crOV0sMTIsLTE5NTg0MTQ0MTcpO209bWQ1X2ZmKG0sbCxvLG4scFtnKzEwXSwxNywtNDIwNjMpO249bWQ1X2ZmKG4sbSxsLG8scFtnKzExXSwyMiwtMTk5MDQwNDE2Mik7bz1tZDVfZmYobyxuLG0sbCxwW2crMTJdLDcsMTgwNDY2MDY4Mik7bD1tZDVfZmYobCxvLG4sbSxwW2crMTNdLDEyLC00MDM0MTEwMSk7bT1tZDVfZmYobSxsLG8sbixwW2crMTRdLDE3LC0xNTAyMDAyMjkwKTtuPW1kNV9mZihuLG0sbCxvLHBbZysxNV0sMjIsMTIzNjUzNTMyOSk7bz1tZDVfZ2cobyxuLG0sbCxwW2crMV0sNSwtMTY1Nzk2NTEwKTtsPW1kNV9nZyhsLG8sbixtLHBbZys2XSw5LC0xMDY5NTAxNjMyKTttPW1kNV9nZyhtLGwsbyxuLHBbZysxMV0sMTQsNjQzNzE3NzEzKTtuPW1kNV9nZyhuLG0sbCxvLHBbZyswXSwyMCwtMzczODk3MzAyKTtvPW1kNV9nZyhvLG4sbSxsLHBbZys1XSw1LC03MDE1NTg2OTEpO2w9bWQ1X2dnKGwsbyxuLG0scFtnKzEwXSw5LDM4MDE2MDgzKTttPW1kNV9nZyhtLGwsbyxuLHBbZysxNV0sMTQsLTY2MDQ3ODMzNSk7bj1tZDVfZ2cobixtLGwsbyxwW2crNF0sMjAsLTQwNTUzNzg0OCk7bz1tZDVfZ2cobyxuLG0sbCxwW2crOV0sNSw1Njg0NDY0MzgpO2w9bWQ1X2dnKGwsbyxuLG0scFtnKzE0XSw5LC0xMDE5ODAzNjkwKTttPW1kNV9nZyhtLGwsbyxuLHBbZyszXSwxNCwtMTg3MzYzOTYxKTtuPW1kNV9nZyhuLG0sbCxvLHBbZys4XSwyMCwxMTYzNTMxNTAxKTtvPW1kNV9nZyhvLG4sbSxsLHBbZysxM10sNSwtMTQ0NDY4MTQ2Nyk7bD1tZDVfZ2cobCxvLG4sbSxwW2crMl0sOSwtNTE0MDM3ODQpO209bWQ1X2dnKG0sbCxvLG4scFtnKzddLDE0LDE3MzUzMjg0NzMpO249bWQ1X2dnKG4sbSxsLG8scFtnKzEyXSwyMCwtMTkyMTIwNzczNCk7bz1tZDVfaGgobyxuLG0sbCxwW2crNV0sNCwtMzc4NTU4KTtsPW1kNV9oaChsLG8sbixtLHBbZys4XSwxMSwtMjAyMjU3NDQ2Myk7bT1tZDVfaGgobSxsLG8sbixwW2crMTFdLDE2LDE4MzkwMzA1NjIpO249bWQ1X2hoKG4sbSxsLG8scFtnKzE0XSwyMywtMzUzMDk1NTYpO289bWQ1X2hoKG8sbixtLGwscFtnKzFdLDQsLTE1MzA5OTIwNjApO2w9bWQ1X2hoKGwsbyxuLG0scFtnKzRdLDExLDEyNzI4OTMzNTMpO209bWQ1X2hoKG0sbCxvLG4scFtnKzddLDE2LC0xNTU0OTc2MzIpO249bWQ1X2hoKG4sbSxsLG8scFtnKzEwXSwyMywtMTA5NDczMDY0MCk7bz1tZDVfaGgobyxuLG0sbCxwW2crMTNdLDQsNjgxMjc5MTc0KTtsPW1kNV9oaChsLG8sbixtLHBbZyswXSwxMSwtMzU4NTM3MjIyKTttPW1kNV9oaChtLGwsbyxuLHBbZyszXSwxNiwtNzIyODgxOTc5KTtuPW1kNV9oaChuLG0sbCxvLHBbZys2XSwyMyw3NjAyOTE4OSk7bz1tZDVfaGgobyxuLG0sbCxwW2crOV0sNCwtNjQwMzY0NDg3KTtsPW1kNV9oaChsLG8sbixtLHBbZysxMl0sMTEsLTQyMTgxNTgzNSk7bT1tZDVfaGgobSxsLG8sbixwW2crMTVdLDE2LDUzMDc0MjUyMCk7bj1tZDVfaGgobixtLGwsbyxwW2crMl0sMjMsLTk5NTMzODY1MSk7bz1tZDVfaWkobyxuLG0sbCxwW2crMF0sNiwtMTk4NjMwODQ0KTtsPW1kNV9paShsLG8sbixtLHBbZys3XSwxMCwxMTI2MTE2MTQxNSk7bT1tZDVfaWkobSxsLG8sbixwW2crMTRdLDE1LC0xNDE2MzU0OTA1KTtuPW1kNV9paShuLG0sbCxvLHBbZys1XSwyMSwtNTc0MzQwNTUpO289bWQ1X2lpKG8sbixtLGwscFtnKzEyXSw2LDE3MDA0ODU1NzEpO2w9bWQ1X2lpKGwsbyxuLG0scFtnKzNdLDEwLC0xODk0NDQ2NjA2KTttPW1kNV9paShtLGwsbyxuLHBbZysxMF0sMTUsLTEwNTE1MjMpO249bWQ1X2lpKG4sbSxsLG8scFtnKzFdLDIxLC0yMDU0OTIyNzk5KTtvPW1kNV9paShvLG4sbSxsLHBbZys4XSw2LDE4NzMzMTMzNTkpO2w9bWQ1X2lpKGwsbyxuLG0scFtnKzE1XSwxMCwtMzA2MTE3NDQpO209bWQ1X2lpKG0sbCxvLG4scFtnKzZdLDE1LC0xNTYwMTk4MzgwKTtuPW1kNV9paShuLG0sbCxvLHBbZysxM10sMjEsMTMwOTE1MTY0OSk7bz1tZDVfaWkobyxuLG0sbCxwW2crNF0sNiwtMTQ1NTIzMDcwKTtsPW1kNV9paShsLG8sbixtLHBbZysxMV0sMTAsLTExMjAyMTAzNzkpO209bWQ1X2lpKG0sbCxvLG4scFtnKzJdLDE1LDcxODc4NzI1OSk7bj1tZDVfaWkobixtLGwsbyxwW2crOV0sMjEsLTM0MzQ4NTU1MSk7bz1zYWZlX2FkZChvLGopO249c2FmZV9hZGQobixoKTttPXNhZmVfYWRkKG0sZik7bD1zYWZlX2FkZChsLGUpfXJldHVybiBBcnJheShvLG4sbSxsKX1mdW5jdGlvbiBtZDVfY21uKGgsZSxkLGMsZyxmKXtyZXR1cm4gc2FmZV9hZGQoYml0X3JvbChzYWZlX2FkZChzYWZlX2FkZChlLGgpLHNhZmVfYWRkKGMsZikpLGcpLGQpfWZ1bmN0aW9uIG1kNV9mZihnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbigoZiZrKXwoKH5mKSZqKSxnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9nZyhnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbigoZiZqKXwoayYofmopKSxnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9oaChnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbihmXmteaixnLGYsZSxpLGgpfWZ1bmN0aW9uIG1kNV9paShnLGYsayxqLGUsaSxoKXtyZXR1cm4gbWQ1X2NtbihrXihmfCh+aikpLGcsZixlLGksaCl9ZnVuY3Rpb24gY29yZV9obWFjX21kNShjLGYpe3ZhciBlPXN0cjJiaW5sKGMpO2lmKGUubGVuZ3RoPjE2KXtlPWNvcmVfbWQ1KGUsYy5sZW5ndGgqY2hyc3opfXZhciBhPUFycmF5KDE2KSxkPUFycmF5KDE2KTtmb3IodmFyIGI9MDtiPDE2O2IrKyl7YVtiXT1lW2JdXjkwOTUyMjQ4NjtkW2JdPWVbYl1eMTU0OTU1NjgyOH12YXIgZz1jb3JlX21kNShhLmNvbmNhdChzdHIyYmlubChmKSksNTEyK2YubGVuZ3RoKmNocnN6KTtyZXR1cm4gY29yZV9tZDUoZC5jb25jYXQoZyksNTEyKzEyOCl9ZnVuY3Rpb24gc2FmZV9hZGQoYSxkKXt2YXIgYz0oYSY2NTUzNSkrKGQmNjU1MzUpO3ZhciBiPShhPj4xNikrKGQ+PjE2KSsoYz4+MTYpO3JldHVybihiPDwxNil8KGMmNjU1MzUpfWZ1bmN0aW9uIGJpdF9yb2woYSxiKXtyZXR1cm4oYTw8Yil8KGE+Pj4oMzItYikpfWZ1bmN0aW9uIHN0cjJiaW5sKGQpe3ZhciBjPUFycmF5KCk7dmFyIGE9KDE8PGNocnN6KS0xO2Zvcih2YXIgYj0wO2I8ZC5sZW5ndGgqY2hyc3o7Yis9Y2hyc3ope2NbYj4+NV18PShkLmNoYXJDb2RlQXQoYi9jaHJzeikmYSk8PChiJTMyKX1yZXR1cm4gY31mdW5jdGlvbiBiaW5sMnN0cihjKXt2YXIgZD0iIjt2YXIgYT0oMTw8Y2hyc3opLTE7Zm9yKHZhciBiPTA7YjxjLmxlbmd0aCozMjtiKz1jaHJzeil7ZCs9U3RyaW5nLmZyb21DaGFyQ29kZSgoY1tiPj41XT4+PihiJTMyKSkmYSl9cmV0dXJuIGR9ZnVuY3Rpb24gYmlubDJoZXgoYyl7dmFyIGI9aGV4Y2FzZT8iMDEyMzQ1Njc4OUFCQ0RFRiI6IjAxMjM0NTY3ODlhYmNkZWYiO3ZhciBkPSIiO2Zvcih2YXIgYT0wO2E8Yy5sZW5ndGgqNDthKyspe2QrPWIuY2hhckF0KChjW2E+PjJdPj4oKGElNCkqOCs0KSkmMTUpK2IuY2hhckF0KChjW2E+PjJdPj4oKGElNCkqOCkpJjE1KX1yZXR1cm4gZH1mdW5jdGlvbiBiaW5sMmI2NChkKXt2YXIgYz0iQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkrLyI7dmFyIGY9IiI7Zm9yKHZhciBiPTA7YjxkLmxlbmd0aCo0O2IrPTMpe3ZhciBlPSgoKGRbYj4+Ml0+PjgqKGIlNCkpJjI1NSk8PDE2KXwoKChkW2IrMT4+Ml0+PjgqKChiKzEpJTQpKSYyNTUpPDw4KXwoKGRbYisyPj4yXT4+OCooKGIrMiklNCkpJjI1NSk7Zm9yKHZhciBhPTA7YTw0O2ErKyl7aWYoYio4K2EqNj5kLmxlbmd0aCozMil7Zis9YjY0cGFkfWVsc2V7Zis9Yy5jaGFyQXQoKGU+PjYqKDMtYSkpJjYzKX19fXJldHVybiBmfTt3aW5kb3cuZiA9IGhleF9tZDUobXdxcXBweik=';
    var hexcase = 0;
    var b64pad = "";
    var chrsz = 16;

    function hex_md5(a) {
        return binl2hex(core_md5(str2binl(a), a.length * chrsz))
    }

    function core_md5(p, k) {
        p[k >> 5] |= 128 << ((k) % 32);
        p[(((k + 64) >>> 9) << 4) + 14] = k;
        var o = 1732584193;
        var n = -271733879;
        var m = -1732584194;
        var l = 271733878;
        for (var g = 0; g < p.length; g += 16) {
            var j = o;
            var h = n;
            var f = m;
            var e = l;
            o = md5_ff(o, n, m, l, p[g + 0], 7, -680976936);
            l = md5_ff(l, o, n, m, p[g + 1], 12, -389564586);
            m = md5_ff(m, l, o, n, p[g + 2], 17, 606105819);
            n = md5_ff(n, m, l, o, p[g + 3], 22, -1044525330);
            o = md5_ff(o, n, m, l, p[g + 4], 7, -176418897);
            l = md5_ff(l, o, n, m, p[g + 5], 12, 1200080426);
            m = md5_ff(m, l, o, n, p[g + 6], 17, -1473231341);
            n = md5_ff(n, m, l, o, p[g + 7], 22, -45705983);
            o = md5_ff(o, n, m, l, p[g + 8], 7, 1770035416);
            l = md5_ff(l, o, n, m, p[g + 9], 12, -1958414417);
            m = md5_ff(m, l, o, n, p[g + 10], 17, -42063);
            n = md5_ff(n, m, l, o, p[g + 11], 22, -1990404162);
            o = md5_ff(o, n, m, l, p[g + 12], 7, 1804660682);
            l = md5_ff(l, o, n, m, p[g + 13], 12, -40341101);
            m = md5_ff(m, l, o, n, p[g + 14], 17, -1502002290);
            n = md5_ff(n, m, l, o, p[g + 15], 22, 1236535329);
            o = md5_gg(o, n, m, l, p[g + 1], 5, -165796510);
            l = md5_gg(l, o, n, m, p[g + 6], 9, -1069501632);
            m = md5_gg(m, l, o, n, p[g + 11], 14, 643717713);
            n = md5_gg(n, m, l, o, p[g + 0], 20, -373897302);
            o = md5_gg(o, n, m, l, p[g + 5], 5, -701558691);
            l = md5_gg(l, o, n, m, p[g + 10], 9, 38016083);
            m = md5_gg(m, l, o, n, p[g + 15], 14, -660478335);
            n = md5_gg(n, m, l, o, p[g + 4], 20, -405537848);
            o = md5_gg(o, n, m, l, p[g + 9], 5, 568446438);
            l = md5_gg(l, o, n, m, p[g + 14], 9, -1019803690);
            m = md5_gg(m, l, o, n, p[g + 3], 14, -187363961);
            n = md5_gg(n, m, l, o, p[g + 8], 20, 1163531501);
            o = md5_gg(o, n, m, l, p[g + 13], 5, -1444681467);
            l = md5_gg(l, o, n, m, p[g + 2], 9, -51403784);
            m = md5_gg(m, l, o, n, p[g + 7], 14, 1735328473);
            n = md5_gg(n, m, l, o, p[g + 12], 20, -1921207734);
            o = md5_hh(o, n, m, l, p[g + 5], 4, -378558);
            l = md5_hh(l, o, n, m, p[g + 8], 11, -2022574463);
            m = md5_hh(m, l, o, n, p[g + 11], 16, 1839030562);
            n = md5_hh(n, m, l, o, p[g + 14], 23, -35309556);
            o = md5_hh(o, n, m, l, p[g + 1], 4, -1530992060);
            l = md5_hh(l, o, n, m, p[g + 4], 11, 1272893353);
            m = md5_hh(m, l, o, n, p[g + 7], 16, -155497632);
            n = md5_hh(n, m, l, o, p[g + 10], 23, -1094730640);
            o = md5_hh(o, n, m, l, p[g + 13], 4, 681279174);
            l = md5_hh(l, o, n, m, p[g + 0], 11, -358537222);
            m = md5_hh(m, l, o, n, p[g + 3], 16, -722881979);
            n = md5_hh(n, m, l, o, p[g + 6], 23, 76029189);
            o = md5_hh(o, n, m, l, p[g + 9], 4, -640364487);
            l = md5_hh(l, o, n, m, p[g + 12], 11, -421815835);
            m = md5_hh(m, l, o, n, p[g + 15], 16, 530742520);
            n = md5_hh(n, m, l, o, p[g + 2], 23, -995338651);
            o = md5_ii(o, n, m, l, p[g + 0], 6, -198630844);
            l = md5_ii(l, o, n, m, p[g + 7], 10, 11261161415);
            m = md5_ii(m, l, o, n, p[g + 14], 15, -1416354905);
            n = md5_ii(n, m, l, o, p[g + 5], 21, -57434055);
            o = md5_ii(o, n, m, l, p[g + 12], 6, 1700485571);
            l = md5_ii(l, o, n, m, p[g + 3], 10, -1894446606);
            m = md5_ii(m, l, o, n, p[g + 10], 15, -1051523);
            n = md5_ii(n, m, l, o, p[g + 1], 21, -2054922799);
            o = md5_ii(o, n, m, l, p[g + 8], 6, 1873313359);
            l = md5_ii(l, o, n, m, p[g + 15], 10, -30611744);
            m = md5_ii(m, l, o, n, p[g + 6], 15, -1560198380);
            n = md5_ii(n, m, l, o, p[g + 13], 21, 1309151649);
            o = md5_ii(o, n, m, l, p[g + 4], 6, -145523070);
            l = md5_ii(l, o, n, m, p[g + 11], 10, -1120210379);
            m = md5_ii(m, l, o, n, p[g + 2], 15, 718787259);
            n = md5_ii(n, m, l, o, p[g + 9], 21, -343485551);
            o = safe_add(o, j);
            n = safe_add(n, h);
            m = safe_add(m, f);
            l = safe_add(l, e)
        }
        return Array(o, n, m, l)
    }

    function md5_cmn(h, e, d, c, g, f) {
        return safe_add(bit_rol(safe_add(safe_add(e, h), safe_add(c, f)), g), d)
    }

    function md5_ff(g, f, k, j, e, i, h) {
        return md5_cmn((f & k) | ((~f) & j), g, f, e, i, h)
    }

    function md5_gg(g, f, k, j, e, i, h) {
        return md5_cmn((f & j) | (k & (~j)), g, f, e, i, h)
    }

    function md5_hh(g, f, k, j, e, i, h) {
        return md5_cmn(f ^ k ^ j, g, f, e, i, h)
    }

    function md5_ii(g, f, k, j, e, i, h) {
        return md5_cmn(k ^ (f | (~j)), g, f, e, i, h)
    }

    function safe_add(a, d) {
        var c = (a & 65535) + (d & 65535);
        var b = (a >> 16) + (d >> 16) + (c >> 16);
        return (b << 16) | (c & 65535)
    }

    function bit_rol(a, b) {
        return (a << b) | (a >>> (32 - b))
    }

    function str2binl(d) {
        var c = Array();
        var a = (1 << chrsz) - 1;
        for (var b = 0; b < d.length * chrsz; b += chrsz) {
            c[b >> 5] |= (d.charCodeAt(b / chrsz) & a) << (b % 32)
        }
        return c
    }

    function binl2hex(c) {
        var b = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var d = "";
        for (var a = 0; a < c.length * 4; a++) {
            d += b.charAt((c[a >> 2] >> ((a % 4) * 8 + 4)) & 15) + b.charAt((c[a >> 2] >> ((a % 4) * 8)) & 15)
        }
        return d
    }
    window.f = hex_md5(mw)
    return ''
}

request = function () {
    var _0x2268f9 = Date['parse'](new Date()) + 100000000
        , _0x57feae = oo0O0(_0x2268f9['toString']()) + window['f'];
    return _0x57feae + '丨' + _0x2268f9 / 1000;
}

console.log(request())