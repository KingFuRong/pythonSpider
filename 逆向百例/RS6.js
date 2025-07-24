
content_str = '5cokHUK6sSMfe_UlNa792e4T5.c2.VDPiQJApF9rquZSi72BSIEk5A151T7ReHbTEaWXaPDGPtJBedEeTQphRoGjuCli_PZUfzvifVHnsG77.9tIBa71Qesz.ORLV7VrD53PfVLRd5g'
setInterval = function (){}
window = top = self = global
window.name = '$_YWTU=K01mfrJBNUc9SMdAn4G10fXdin.QAeFaSV04f8sF3MV&$_YVTX=Wa&vdFm='
window.indexedDB = {}
window.addEventListener = function (arg){
    console.log('window addEventListener:', arguments)
    return undefined
}
window.attachEvent = function (arg){
    console.log('window attachEvent:', arguments)
    return true
}
window.XMLHttpRequest = function (arg){
    console.log('window XMLHttpRequest:', arguments)
    return undefined
}
window.open = function (arg){
    console.log('window open:', arguments)
}
function getMockFileSystem() {
    // 创建一个基础对象来持有 FileSystem 和 DirectoryEntry
    const mockFs = {};

    const mockRootDirectoryEntry = {
        isFile: false,
        isDirectory: true,
        name: '',
        fullPath: '/',
        filesystem: mockFs, // 循环引用
        // 在真实的 API 中，这里还会有 getFile, getDirectory 等方法
        getFile: function() { console.log("Mock getFile called"); },
        getDirectory: function() { console.log("Mock getDirectory called"); }
    };

    // 填充 mockFs 对象，完成循环引用
    mockFs.name = 'temporary:http_localhost_8080'; // 模拟一个典型的名称
    mockFs.root = mockRootDirectoryEntry;

    return mockFs;
}
window.webkitRequestFileSystem = function (type, size, successCallback, errorCallback) {
    console.log("window webkitRequestFileSystem:", arguments);
    process.nextTick(() => {
        const fileSystemObject = getMockFileSystem();
        if (successCallback) {
            successCallback(fileSystemObject);
        }
    });
    return undefined;
}
window.HTMLAnchorElement = function (arg){
    console.log('window HTMLAnchorElement:', arguments)
}
window.clientInformation = navigator
window.TEMPORARY = 0
location = {
    "ancestorOrigins": {},
    "href": "https://www.nmpa.gov.cn/datasearch/search-result.html",
    "origin": "https://www.nmpa.gov.cn",
    "protocol": "https:",
    "host": "www.nmpa.gov.cn",
    "hostname": "www.nmpa.gov.cn",
    "port": "",
    "pathname": "/datasearch/search-result.html",
    "search": "",
    "hash": ""
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    language: "en-US",
    languages: ['en-US'],
    platform: "MacIntel",
    product: "Gecko",
    productSub: "20030107",
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    vendor: "Google Inc."
}

_html = {}
_head = {
    removeChild: function (arg){
        console.log('_head removeChild:', arguments)
        return arg
    }
}
_body = {}
div = {
    getElementsByTagName: function (arg){
        console.log('div getElementsByTagName:', arguments)
        if (arg === 'i'){
            return {}
        }
    }
}
script = {
    getAttribute: function (arg){
        console.log('script getAttribute:', arguments)
        if (arg === 'r'){
            return 'm'
        }
    },
    parentElement: _head
}
meta = {
    getAttribute: function (arg){
        console.log('meta getAttribute:', arguments)
        if (arg === 'r'){
            return 'm'
        }
        if (arg === 'content'){
            return content_str
        }
    },
    parentNode: _head
}

localStorage = {
    "__#classType": "localStorage",
    removeItem: function (arg) {
        console.log('sessionStorage removeItem:', arguments)
        return undefined
    },
    getItem: function (arg){
        console.log('localStorage getItem:', arguments)
        console.log('localStorage getItem return:', localStorage[arg] || null)
        return localStorage[arg] || null
    },
    setItem: function (key, value){
        console.log('localStorage setItem:', key, value)
        localStorage[key] = value
        return undefined
    }
}
sessionStorage = {}
DOMParser = function (arg){
    console.log('DOMparser:', arguments)
    return {}
}
document = {
    documentElement: {},
    visibilityState: 'visible',
    body: _body,
    all: [_html, _head, meta, meta],
    createElement: function (arg) {
        console.log('document createElement:', arguments)
        if (arg === 'div'){
            return div
        }
        if (arg === 'a'){
            return {}
        }
        return {}
    },
    appendChild: function (arg) {
        console.log('document appendChild:', arguments)
        return arg
    },
    removeChild: function (arg) {
        console.log('document removeChild:', arguments)
        return arg
    },
    getElementsByTagName: function (arg){
        console.log('document getElementsByTagName:', arguments)
        if (arg === 'script'){
            return [script, script]
        }
        if (arg === 'meta'){
            return [meta, meta]
        }
        if (arg === 'base'){
            return {}
        }
        return null
    },
    getElementById: function (arg){
        console.log('document getElementById:', arguments)
        return null
    },
    createExpression: function (arg){
        console.log('document createExpression:', arguments)
        if (arg === '//html'){
            return {}
        }
        return {}
    },
    addEventListener: function (arg){
        console.log('document addEventListener:', arguments)
        return undefined
    },
}

// window.MutationObserver = function (){}
class MutationObserver{
    observe = function (arg){
        console.log('MutationObserver observe', arguments)
        return undefined
    }
}
window.MutationObserver = MutationObserver

function setProxy(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
          get: function(target, property, receiver) {
                   // console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], "属性值类型：", typeof target[property]);
                   console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property]);
                   return target[property];
               },
          set: function(target, property, value, receiver) {
                   console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
                   return Reflect.set(...arguments);
               }
          }`;
        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`);
    }
}

setProxy(['window', 'document', ' navigator', 'screen', 'localStorage', 'location', 'div', 'script', 'XMLHttpRequest', 'Request', 'open', '_body'])

