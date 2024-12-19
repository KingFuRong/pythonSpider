const {JSDOM} = require("jsdom");

var window = global;
window['window'] = window;
window.bmak = {
    startTs: Date.now()
};
var Bq = [4095, 1, 0, 63, 8, 255, 127, 39, 65793, 4294967295, 4282663, 65535, 8388607, 8888888, 1024, 2048, 3600, 4096, 3, 5, 6, 13, 100, 9, 17, 19, 28, 30, 10, 2, 112, 4, 999999, 32, 2222, 1.81, 22, 11, 3600000, 1.43, 333, 1000]
var cxI = "";
var MP = "";
var vH = new (window['Array'])(Bq[6]);
var dQI = false;

function YC(jZI, f6I) {
    return jZI < f6I;
}

function cw(KB, pp) {
    return KB >> pp;
}

function t0(P0, mK) {
    return P0 & mK;
}

function Hb(Zz, kB) {
    return Zz % kB;
}

function Ut() {
    if (window["Date"]["now"] && typeof window["Date"]["now"]() === 'number') {
        return window["Date"]["now"]();
    } else {
        return +new (window["Date"])();
    }
}

function OV(ECI, M3I) {
    return ECI - M3I;
}

function Dj(Gj) {
    return !Gj;
}

function Dp(I6, Rw) {
    return I6 === Rw;
}

function BY(DbI) {
    return -DbI;
}

function O3(bK, kp) {
    return bK !== kp;
}

function C7(cA, HW) {
    return cA >= HW;
}

function NK(CKI, YnI) {
    return CKI + YnI;
}

function xz(Ms, jz) {
    return Ms * jz;
}

function Bj() {
    return window["Math"]["floor"](window["Math"]["random"]() * 100000 + 10000);
}

function qZ(jK) {
    if (jK == null)
        return -1;
    try {
        var VZ = 0;
        for (var jB = 0; jB < jK["length"]; jB++) {
            var r8 = jK["charCodeAt"](jB);
            if (r8 < 128) {
                VZ = VZ + r8;
            }
        }
        return VZ;
    } catch (dp) {
        return -2;
    }
}

function z6(UAI, RwI) {
    return UAI == RwI;
}

function Ph(m2I) {
    var p6I = ['text', 'search', 'url', 'email', 'tel', 'number'];
    m2I = m2I["toLowerCase"]();
    if (p6I["indexOf"](m2I) !== -1)
        return 0;
    else if (m2I === 'password')
        return 1;
    else
        return 2;
}

function wdI(input_tags) {
    // if (Dj(dQI)) {
    //     try {
    //         var SEI = ws.length;
    //         var TD = Dj([]);
    //         YXI = NK(YXI, BH()[vP(UC)](rf, hH, p7, Dj(Dj([])), N3, xg));
    //         var mQI = KX[z5()[Cl(T6)](mN, J2)][dXI()[MdI(MK)](I0, p7, Wb)](RY()[PA(Ug)].call(null, tp, qW, Dj(x0), Vz));
    //         if (O3(mQI[dXI()[MdI(vl)](Zf, JV, CM)], undefined)) {
    //             YXI = NK(YXI, RY()[PA(N3)].call(null, jU, lz, bP, pw));
    //             jII = KX[O3(typeof vA()[ng(Lg)], NK('', [][[]])) ? vA()[ng(Gs)](N5, T0) : vA()[ng(KK)].apply(null, [gB, Mz])][vA()[ng(tr)](f8, cz)](sdI(jII, KK));
    //         } else {
    //             YXI = NK(YXI, k2()[OW(gJ)].apply(null, [Gp, AL, Rq, q5, bH, p7]));
    //             jII = KX[vA()[ng(Gs)].call(null, N5, T0)][vA()[ng(tr)].call(null, f8, cz)](sdI(jII, vG[dXI()[MdI(XY)].call(null, rr, MC, J2)]()));
    //         }
    //     } catch (YdI) {
    //         ws.splice(OV(SEI, p7), Infinity, DZ);
    //         YXI = NK(YXI, z5()[Cl(TJ)](dJ, Pj));
    //         jII = KX[vA()[ng(Gs)](N5, T0)][vA()[ng(tr)](f8, cz)](sdI(jII, Bq[gJ]));
    //     }
    //     dQI = Dj(Z4);
    // }
    input_tags = '<html><body>' + input_tags.join('') + '</body></html>';
    var dom = new JSDOM(input_tags);

    var YSI = '';
    var ccI = BY(1);
    var tdI = dom.window['document']['getElementsByTagName']("input");
    for (var FD = 0; YC(FD, tdI['length']); FD++) {
        var FXI = tdI[FD];
        var U4I = qZ(FXI['getAttribute']('name'));
        var KkI = qZ(FXI['getAttribute']('id'));
        var A4I = FXI['getAttribute']('required');
        var f1I = z6(A4I, null) ? 0 : 1;
        var N9I = FXI['getAttribute']('type');
        var xdI = z6(N9I, null) ? BY(1) : Ph(N9I);
        var mGI = FXI['getAttribute']('autocomplete');
        if (z6(mGI, null))
            ccI = BY(1);
        else {
            mGI = mGI['toLowerCase']();
            if (Dp(mGI, 'off'))
                ccI = 0;
            else if (Dp(mGI, 'on'))
                ccI = 1;
            else
                ccI = 2;
        }
        var q9I = FXI['defaultValue'];
        var W4I = FXI['value'];
        var GEI = 0;
        var T1I = 0;
        if (q9I && O3(q9I['length'], 0)) {
            T1I = 1;
        }
        if (W4I && O3(W4I['length'], 0) && (Dj(T1I) || O3(W4I, q9I))) {
            GEI = 1;
        }
        if (O3(xdI, 2)) {
            YSI = ''['concat'](NK(YSI, xdI), ',')['concat'](ccI, ',')['concat'](GEI, ',')['concat'](f1I, ',')['concat'](KkI, ',')['concat'](U4I, ',')['concat'](T1I, ';');
        }
    }
    var QmI;
    return QmI = YSI, QmI;
}

function k6(RAI) {
    var CLI = {};
    var YMI = RAI;
    for (var MUI = 0; YC(MUI, YMI['length']); MUI += 2)
        CLI[YMI[MUI]] = YMI[NK(MUI, 1)];
    var ItI;
    return ItI = CLI, ItI;
}

function QFI() {
    if (Dj({})) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj([])) {
    } else if (Dj(Dj(0))) {
    } else if (Dj([])) {
    } else if (Dj([])) {
    } else if (Dj(1)) {
    } else if (Dj([])) {
    } else if (Dj({})) {
    } else if (Dj(Dj(0))) {
    } else if (Dj({})) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj([])) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj({})) {
    } else if (Dj(Dj(0))) {
    } else if (Dj([])) {
    } else if (Dj({})) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj(1)) {
    } else if (Dj(Dj(0))) {
    } else if (Dj(1)) {
    } else if (Dj(Dj(0))) {
    } else if (Dj([])) {
    } else if (Dj([])) {
    } else if (Dj(Dj(0))) {
    } else if (Dj(1)) {
    } else if (Dj(1)) {
    } else if (Dj({})) {
    } else if (Dj(Dj(0))) {
    } else if (Dj(Dj(0))) {
    } else if (Dj({})) {
    } else if (Dj(Dj(0))) {
    } else if (Dj(Dj(0))) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj(Dj(0))) {
    } else if (Dj([])) {
    } else if (Dj(1)) {
    } else if (Dj({})) {
    } else if (Dj(1)) {
    } else if (Dj({})) {
    } else if (Dj([])) {
    } else if (Dj({})) {
    } else if (Dj(Dj(0))) {
    } else if (Dj(1)) {
    } else if (Dj(1)) {
    } else if (Dj(Dj(1))) {
        return function JmI(UEI) {
            var SII = NK(UEI['startTimestamp'], UEI['deltaTimestamp']);
            var LSI = Bj();
            var VSI = xz(SII, LSI);
            var cSI = window['parseInt'](window['Math']['sqrt'](VSI), 10);
            var WEI = [cSI, LSI];
            var MkI;
            return MkI = WEI['join']('|'), MkI;
        };
    }
}

function H4(deltaTimestamp, env_enc, R4G, totVel) {
    function text_to_binary(text, salt) {
        var cipher_number = 5381;
        var text_length = text.length;
        for (let i = 0; i < text_length; i++) {
            cipher_number = (cipher_number * 33) ^ text.charCodeAt(i);
        }
        cipher_number = (cipher_number >>> 0) + salt;
        var cipher_binary = cipher_number.toString(2);
        return {cipher_number, cipher_binary};
    }

    var first_original_text = `${totVel}${JSON.stringify(window['window'].bmak['startTs'])}) Chrome/131.0.0.0 Safari/537.36${R4G}`;
    var first_binary_text = text_to_binary(first_original_text, 0);
    var second_original_text = deltaTimestamp + env_enc + R4G
    var second_binary_text = text_to_binary(second_original_text, first_binary_text['cipher_number']);
    var cipher_key = "a3cd9efghiYjklm7opqrs1uvwQxyBz2";
    var cipher_array = []
    var cipher_number = first_binary_text['cipher_binary']
    for (let i = 0; i < cipher_key.length; i++) {
        if (cipher_number[i % cipher_number.length] === "1") {
            cipher_array.push(cipher_key[i]);
        } else if (i % 3 === 0) {
            cipher_array.push(cipher_key[i]);
        }
    }

    var cipher_text = [];
    cipher_text.push("")
    for (let i = 0; i < 6; i++) {
        let first_num = parseInt(second_binary_text['cipher_binary'][i])
        let second_num = cipher_array[i % cipher_array.length].charCodeAt(0)
        let third_num = (second_num >> first_num) | (second_num << 5)
        let fourth_num = (second_num << (3 * first_num)) - second_num
        let fifth_num = (first_num * 7) ^ (second_num + 2)

        cipher_text[0] += cipher_array[Math.abs(third_num * fourth_num - fifth_num) % cipher_array.length]
    }

    var third_original_text = `${R4G}${window['window'].bmak['startTs'] + deltaTimestamp}`
    cipher_text.push("")
    for (let i = 0; i < third_original_text.length; i++) {
        cipher_text[1] += cipher_array[parseInt(third_original_text.charAt(i)) % cipher_array.length]
    }
    return cipher_text[1] + cipher_text[0];
}

function KEI(bm_sz) {
    var dh = [8888888, 9911307];
    var rGI = bm_sz;
    if (O3(rGI, Dj({}))) {
        var SXI = 7;
        var ZRI = Dj(Dj(0));
        var smI = window['decodeURIComponent'](rGI)['split']('~');
        if (C7(smI['length'], 4)) {
            var RGI = window['parseInt'](smI[2], 10);
            RGI = window['isNaN'](RGI) ? gxI : RGI;
            dh[Bq[2]] = RGI;
        }
    }
    var tRI;
    return tRI = dh, tRI;
}

function OO(fpI) {
    var NsI = fpI[0];
    var sVI = fpI[1];
    var S6I;
    var nsI;
    var cbI;
    var lBI;
    var OVI = ":";
    var GCI = NsI["split"](OVI);
    for (lBI = 0; YC(lBI, GCI['length']); lBI++) {
        S6I = Hb(t0(cw(sVI, 8), Bq[11]), GCI['length']);
        sVI *= Bq[8];
        sVI &= 4294967295;
        sVI += 4282663;
        sVI &= Bq[12];
        nsI = Hb(t0(cw(sVI, 8), Bq[11]), GCI['length']);
        sVI *= 65793;
        sVI &= Bq[9];
        sVI += 4282663;
        sVI &= Bq[12];
        cbI = GCI[S6I];
        GCI[S6I] = GCI[nsI];
        GCI[nsI] = cbI;
    }
    var vcI;
    return vcI = GCI['join'](OVI), vcI;
}

function Lr(xH, vv) {
    if (Dj(MP)) {
        for (var cP = 0; YC(cP, 127); ++cP) {
            if (YC(cP, 32) || Dp(cP, Bq[7]) || Dp(cP, 34) || Dp(cP, 92)) {
                vH[cP] = BY(1);
            } else {
                vH[cP] = MP['length'];
                MP += window['String']['fromCharCode'](cP);
            }
        }
    }
    var O5 = "";
    for (var tg = 0; YC(tg, xH['length']); tg++) {
        var ET = xH['charAt'](tg);
        var KA = t0(cw(vv, 8), 65535);
        vv *= Bq[8];
        vv &= Bq[9];
        vv += Bq[10];
        vv &= 8388607;
        var Kr = vH[xH['charCodeAt'](tg)];
        if (Dp(typeof ET['codePointAt'], 'function')) {
            var VT = ET['codePointAt'](0);
            if (C7(VT, 32) && YC(VT, 127)) {
                Kr = vH[VT];
            }
        }
        if (C7(Kr, 0)) {
            var HJ = Hb(KA, MP['length']);
            Kr += HJ;
            Kr %= MP['length'];
            ET = MP[Kr];
        }
        O5 += ET;
    }
    var H9I;
    return H9I = O5, H9I;
}

function NKI(F7I) {
    var jVI = '3';
    var nbI = '0';
    var SzI = 1;
    var UbI = 0;
    var YNI = 'xqSWzvRJGvg0H6FxfCngl4+2Q1rxnC+iZq6fuG4DSCE=';
    var KnI = [jVI, nbI, SzI, UbI, F7I[Bq[2]], YNI];
    var C6I = KnI['join'](';');
    var tKI;
    return tKI = C6I, tKI;
}

function Akamai_cookie(bm_sz, input_tags, url) {
    var kkI = Ut();
    var BRI = OV(Ut(), window['window'].bmak['startTs']);
    var HRI = "do_en";
    var TEI = "dm_en";
    var OQI = "t_en";
    var gFI = ''['concat'](HRI, ',')['concat'](TEI, ',')['concat'](OQI);
    var pkI = wdI(input_tags);
    var zkI = url['replace'](new (window['RegExp'])('\\\\|"','g'), '');
    var VXI = ('')['concat'](0, ',')['concat'](Bq[2]);

    var EpI = Ut();
    var XpI = [
        {"tsd": 0},
        {"swi": 1536},
        {"wih": 776},
        {"npl": 5},
        {"hal": 867258819993},
        {"hz1": 426773},
        {"ucs": "8102"},
        {"ran": "0.06919885234"},
        {"ash": 864},
        {"asw": 1536},
        {"nal": "en-US"},
        {"adp": "cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1"},
        {"ibr": 0},
        {"xag": 12147},
        {"wow": 1536},
        {"pha": 0},
        {"wiw": 150},
        {"nap": "Gecko"},
        {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"},
        {"she": 864},
        {"nps": "20030107"},
        {"dau": 0},
        {"wdr": 0}
    ]
    var H6I = QFI()(k6(['startTimestamp', window['window'].bmak['startTs'], 'deviceData', XpI.map(obj => Object.values(obj)).flat().join(','), 'mouseMoveData', '', 'totVel', 0, 'deltaTimestamp', BRI]));
    var ZnI = H4(BRI, H6I, 0, 0);
    var ZVI = OV(Ut(), EpI);
    var wVI = [
        {"kevl": 1},
        {"mevl": 32},
        {"tevl": 32},
        {"devl": 0},
        {"dmvl": 0},
        {"pevl": 0},
        {"tovl": 0},
        {"delt": 2},
        {"it": 0},
        {"sts": window['window'].bmak['startTs']},
        {"fct": -999999},
        {"dd2": 18555},
        {"kc": 0},
        {"mc": 0},
        {"ww8": 0},
        {"pc": 0},
        {"tc": 0},
        {"ssts": 3},
        {"tst": 0},
        {"rval": "-1"},
        {"rcfp": "-1"},
        {"nfas": 30261693},
        {"jsrf": "PiZtE"},
        {"jsrf1": 83184},
        {"jsrf2": 66},
        {"signals": "0"},
        {"mwd": "0"},
        {"hea": ""},
        {"dvc": `${ZnI},${ZVI},i+c+f+l+j+g+h+e+b+d+`},
        {"srd": "0"}
    ]
    var g1I = {
        "ver": "xqSWzvRJGvg0H6FxfCngl4+2Q1rxnC+iZq6fuG4DSCE=",
        "fpt": "-1",
        "fpc": "94",
        "ajr": H6I,
        "din": XpI,
        "eem": gFI,
        "ffs": pkI,
        "vev": "",
        "inf": pkI,
        "ajt": VXI,
        "kev": "",
        "dme": "",
        "mev": "",
        "doe": "",
        "pur": zkI,
        "pev": "",
        "mst": wVI,
        "o9": 0,
        "tev": "",
        "sde": "0,0,0,0,1,0,0",
        "pmo": "",
        "dpw": "",
        "pac": "",
        "per": "8",
        "pde": "",
        "oev": "",
        "if": "",
        "fwd": [
            {
                "fmh": ""
            },
            {
                "fmz": ""
            },
            {
                "ssh": "0"
            }
        ]
    };
    var BzI = KEI(bm_sz);
    cxI = window["JSON"]["stringify"](g1I);
    var kpI = Ut();
    cxI = OO([cxI, BzI[1]]);
    kpI = OV(Ut(), kpI);
    var PCI = Ut();
    cxI = Lr(cxI, BzI[0]);
    PCI = OV(Ut(), PCI);
    var ZsI = ""['concat'](OV(Ut(), kkI), ',')['concat'](0, ',')['concat'](0, ',')['concat'](kpI, ',')['concat'](PCI, ',')['concat'](0);
    var sNI = NKI(BzI);
    cxI = ''['concat'](sNI, ';')['concat'](ZsI, ';')['concat'](cxI);

    var UII = window['JSON']['stringify'](cxI);
    var WD = '{"sensor_data":'['concat'](UII, '}');
    return WD
}
