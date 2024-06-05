var window = global;

(function () {
    window._cf_chl_opt = {
        cvId: '3',
        cZone: 'challenges.cloudflare.com',
        cTplV: 5,
        chlApivId: '0',
        chlApiWidgetId: '2sv5h',
        chlApiSitekey: '0x4AAAAAAAKC1nc26lcmHwc5',
        chlApiMode: 'managed',
        chlApiSize: 'normal',
        chlApiRcV: '2/a1kWVkoWtbyEEae',
        chlApiTimeoutEncountered: 0,
        chlTimeoutMs: 120000,
        cK: "visitor-time",
        cType: 'chl_api_m',
        cNounce: '64832',
        cRay: '88d663c57a001d8f',
        cHash: '21f0d56f15e31af',
        cFPWv: 'g',
        cLt: 'n',
        cRq: {
            ru: 'aHR0cDovL2NoYWxsZW5nZXMuY2xvdWRmbGFyZS5jb20vY2RuLWNnaS9jaGFsbGVuZ2UtcGxhdGZvcm0vaC9nL3R1cm5zdGlsZS9pZi9vdjIvYXYwL3JjdjEvaDJndkM0TXZrdzFEUDBmLzJzdjVoLzB4NEFBQUFBQUFLQzFuYzI2bGNtSHdjNS9saWdodC9ub3JtYWw=',
            ra: 'cHl0aG9uLXJlcXVlc3RzLzIuMzEuMA==',
            rm: 'R0VU',
            d: 'TuTAvtQvinxWRQOo3BM6yGd0Eh0go0HWwUhNPfHubxHmJPMGNrxwBYbqN99EVTC0XZGPJdjyNRYPOsxgjRiyNNpFNYwI5tSbxXY9bw6br5EKDNPTxHXHfWEqh3WjwMSZsTmyKC/xdiuX//QhjiQwgChvWmzsHZkTDexKlwy9L8aTACzdHJVVYXMgR6PHjn5z53VkZsOcyvZNmzfRiXQjzg5QhT7VAFsscqWosjT+XVwRmZ7suDHkCeoipC8Og7KtUnzc7Cl6qx9j0/Q4a0NxWmZYGw0OuFubVseZlrrpYAIwrc3NYIRrGUUB1xNKeoAN8i0qeZEH1ZTIMEAUuIrADQtOD4Nft65LGQf50bkLHfWV44cc32J8t1ON8FRrxvJkGjwzvslR4ZKLs6wXhFDvknIjbLBPlCjGSCedt1RdBD4b//zvpwB8XwGjPKDgYRVKqduLhV9KTpeq9gQwMjmkvpQ+5AvV+Q+8n9HKl2LBl6VNaNNPwtx18H9hZ9OdqLSNwY2RE7pB18Q3LzilLXstMH4A2Zk7XToPHlNQiT2QmMaXLApQtP5VECHRvOl/IW3E76CNcCFiXbsEnZa5NYYT+oHHMl2YiJDYfSvn8r1+BsZqhooLxxXfMAVqPZL+1r6dzTirzh8P6kBPWrY9h7AYRE1SR91RMTEp7ok/FF6mlG7TQ+T7tItWVsrtObES/ChuX7P+SuyUeXOJMqWL9Y/YxVpdhaoqZN9djLmpCmMHrrQWNi9iyl/SGLv5BPBc+cCo5GRfxrdTFPWIqhUQwZbN3umcdyNxVAe/C4BqzoBN5ynvUcQ3Qg6GZhmOPJqmmCYphbIqXBuwqt4vL1qJTA3n4bJtaNqDHsGjjjQAo3FAtc+6G+yFSI3p9teILx2er/k22SWtMpuoltsoibtevGDCgHmbWNGM2vxaQR95hcZ2MwM=',
            t: 'MTcxNzMyMDI1OS40NDc=',
            m: 'Kr09vyxMuHxPwWYjT1n77YsDnX3cfjIUw+Zis290fnA=',
            i1: 'rm2V54vG9YYM4Q/BwFY4bA==',
            i2: 'Gq+PXwKc0tcn8K0G78la9A==',
            uh: 'YE9XOpG5TeHmhA1zfs5mxC8CrRZzq2a/+r+OU7dliYQ=',
            hh: 'WCiLdNo2uN2aXsfJJhG2HFkP3bOo0fw8tsFAppLisvs=',
            zh: '9D+zbxCfwBPyr1pF5Wb5E9kRItcGU2xCgzO1zGTKToQ=',
        },
        refresh: function () {
            if (window['parent']) {
                window['parent'].postMessage({
                    source: 'cloudflare-challenge',
                    widgetId: '2sv5h',
                    nextRcV: '2/a1kWVkoWtbyEEae',
                    event: 'reloadRequest',
                }, "*");
            }
        }
    };
    var handler = function (event) {
        var e = event.data;
        if (e.source && e.source === 'cloudflare-challenge' && e.event === 'meow' && e.widgetId === window._cf_chl_opt.chlApiWidgetId) {
            if (window['parent']) {
                window['parent'].postMessage({
                    source: 'cloudflare-challenge',
                    widgetId: window._cf_chl_opt.chlApiWidgetId,
                    event: 'food',
                    seq: e.seq,
                }, "*");
            }
        }
    }
    if (window.addEventListener) {
        window.addEventListener('message', handler);
    } else {
        window.attachEvent('onmessage', handler);
    }
}());