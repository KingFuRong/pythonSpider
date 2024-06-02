var CryptoJS = require('crypto-js')


/**
 * @param {string} wordStr  页数 + 鼠标轨迹作为被加密文本
 * @param {string} keyStr   时间戳/1000取整转16进制作为key密钥
 * @param {string} ivStr    时间戳/1000取整转16进制作为iv偏移量
 */
function AES_CBC_ENCRYPT(wordStr, keyStr, ivStr) {
    //将word的utf8转为wordArray数据
    let word = CryptoJS.enc.Utf8.parse(wordStr);
    //将key的utf8转为wordArray数据
    let key = CryptoJS.enc.Utf8.parse(keyStr);
    //将iv的utf8转为wordArray数据
    let iv = CryptoJS.enc.Utf8.parse(ivStr);
    //进行加密处理(第一个参数是要加密的word,第二个是密钥,第三个是配置参数)
    let encrypted = CryptoJS.AES.encrypt(word, key, {
        //配置偏移量,如果mode为ECB模式则不需要这个参数
        iv,
        //模式选择CBC(模式介绍可以到百度查看,这里不讲述)
        mode: CryptoJS.mode.CBC,
        //填充使用Pkcs7(注意大小写)
        padding: CryptoJS.pad.Pkcs7
    });
    //使用toString()处理返回
    return encrypted.toString();
}


var t = Date['parse'](new Date()) / 1000;
var keyStr = t.toString(16) + t.toString(16);
var ivStr = t.toString(16) + t.toString(16);

function get_v(wordStr) {
    return {
        'v': AES_CBC_ENCRYPT(wordStr, keyStr, ivStr),
        't': t
    };
}