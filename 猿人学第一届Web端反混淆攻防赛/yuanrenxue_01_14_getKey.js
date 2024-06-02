window = global;

var $_0x3a61;

function get_true_array(enc_array, offset) {
    ++offset
    while (--offset) {
        enc_array['push'](enc_array['shift']());
    }
    $_0x3a61 = enc_array
}

var $_0x3d67 = function (_0x483274, _0x3a6124) {
    _0x483274 = _0x483274 - 0;
    var _0x3d67a9 = $_0x3a61[_0x483274];

    var _0x47950d = function (_0x5e4d69, _0x366ed3) {
        var _0x49bd8f = [],
            _0x131425 = 0,
            _0x268854,
            _0x542be0 = '',
            _0x5b9891 = '';

        _0x5e4d69 = atob(_0x5e4d69);

        for (var _0x5a4196 = 0, _0x1fb71e = _0x5e4d69['length']; _0x5a4196 < _0x1fb71e; _0x5a4196++) {
            _0x5b9891 += '%' + ('00' + _0x5e4d69['charCodeAt'](_0x5a4196)['toString'](16))['slice'](-2);
        }

        _0x5e4d69 = decodeURIComponent(_0x5b9891);

        var _0x3a4962;

        for (_0x3a4962 = 0; _0x3a4962 < 256; _0x3a4962++) {
            _0x49bd8f[_0x3a4962] = _0x3a4962;
        }

        for (_0x3a4962 = 0; _0x3a4962 < 256; _0x3a4962++) {
            _0x131425 = (_0x131425 + _0x49bd8f[_0x3a4962] + _0x366ed3['charCodeAt'](_0x3a4962 % _0x366ed3['length'])) % 256;
            _0x268854 = _0x49bd8f[_0x3a4962];
            _0x49bd8f[_0x3a4962] = _0x49bd8f[_0x131425];
            _0x49bd8f[_0x131425] = _0x268854;
        }

        _0x3a4962 = 0;
        _0x131425 = 0;

        for (var _0x3ef48f = 0; _0x3ef48f < _0x5e4d69['length']; _0x3ef48f++) {
            _0x3a4962 = (_0x3a4962 + 1) % 256;
            _0x131425 = (_0x131425 + _0x49bd8f[_0x3a4962]) % 256;
            _0x268854 = _0x49bd8f[_0x3a4962];
            _0x49bd8f[_0x3a4962] = _0x49bd8f[_0x131425];
            _0x49bd8f[_0x131425] = _0x268854;
            _0x542be0 += String['fromCharCode'](_0x5e4d69['charCodeAt'](_0x3ef48f) ^ _0x49bd8f[(_0x49bd8f[_0x3a4962] + _0x49bd8f[_0x131425]) % 256]);
        }

        return _0x542be0;
    };
    $_0x3d67['eMHwUn'] = _0x47950d;
    $_0x3d67['EmGQug'] = {};
    var _0x37182a = $_0x3d67['EmGQug'][_0x483274];
    if (_0x37182a === undefined) {
        _0x3d67a9 = $_0x3d67['eMHwUn'](_0x3d67a9, _0x3a6124);
        $_0x3d67['EmGQug'][_0x483274] = _0x3d67a9;
    } else {
        _0x3d67a9 = _0x37182a;
    }
    return _0x3d67a9;
};

function get_key(enc_array, offset, v14, v142) {
    get_true_array(eval(enc_array), offset);
    eval(v14);
    eval(v142);
    return {
        'v14': window['v14'],
        'v142': window['v142']
    };
}

