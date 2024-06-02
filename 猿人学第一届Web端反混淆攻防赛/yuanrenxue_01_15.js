window = global;

function get_m() {
    fetch('https://match.yuanrenxue.cn/static/match/match15/main.wasm').then(response =>
        response.arrayBuffer()
    ).then(bytes => WebAssembly.instantiate(bytes)).then(results => {
        instance = results.instance;
        window.q = instance.exports.encode;
        window.m = function () {
            t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
            t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
            return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
        };
        const result = ['ok', window.m()];
        console.log(JSON.stringify(result));
    })
}
