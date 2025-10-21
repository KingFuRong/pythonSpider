// Called from (LR): 0x76083cd3b8|0x76083cd3b8 libtiny.so!0x1573b8
// 0x76083cd3b8 libtiny.so!0x1573b8
// 0x76083cd058 libtiny.so!0x157058
// 0x76083cb970 libtiny.so!0x155970
// 0x76083cbc5c libtiny.so!0x155c5c
// 0x76083cae40 libtiny.so!0x154e40
// 0x76084b6aa4 libtiny.so!0x240aa4
// 0x76084c67c0 libtiny.so!0x2507c0
// 0x760839bd74 libtiny.so!0x125d74
// 0x764acb0548
// 0x764acb066c
// 0x764accb680
// 0x764acb7768
// 0x764acb7b1c
// 0x764acb85c0
// 0x764acbada8
// 0x764ac14d60

// --- 配置区域 ---
const targetLibrary = "libtiny.so";
// const targetFunctionOffset = 0x157054;
const targetOffsets = [0x156E68, 0x157048, 0x156F88];
// -----------------

function hook_function() {
    console.log(`[*] Searching for library: ${targetLibrary}`);
    for (const offset of targetOffsets) {
        const module = Process.findModuleByName(targetLibrary);
        if (!module) {
            console.error(`[!] Library ${targetLibrary} not found. Ensure it's loaded.`);
            return;
        }

        const baseAddr = module.base;
        const funcAddr = baseAddr.add(offset);
        console.log(`[+] Found ${targetLibrary} at ${baseAddr}`);
        console.log(`[+] Hooking sub_156E10 at address: ${funcAddr} offset: 0x${offset.toString(16)}`);

        Interceptor.attach(funcAddr, {
            onEnter: function (args) {

                const threadId = Process.getCurrentThreadId();
                const value_ptr = this.context.x19;
                const x1_ptr = this.context.x19;
                console.log(`Argument x19: ${value_ptr}  (TID:${threadId})  Address: 0x${offset.toString(16)}`);

                if (x1_ptr.isNull()) {
                    console.log("    |-- a1 is a NULL pointer.");
                } else {
                    try {
                        let lr_ptr = this.context.lr;
                        let caller_symbol = DebugSymbol.fromAddress(lr_ptr);
                        console.log('Called from (LR): ' + lr_ptr + '|' + caller_symbol);
                        console.log('value:' + value_ptr.readCString() + '\n')
                    } catch (e) {
                        console.log(`    |-- [!] Failed to read memory: ${e.message}`);
                    }
                }
            },

            onLeave: function (retval) {
                console.log(`  <-- Leaving sub_156E10`);
                console.log(`      Return Value (in x0): ${retval}`);
                console.log(`========================================================================\n`);
            }
        });
    }
}

function hook_call_constructors_test() {
    let get_soname = null;
    let call_constructors_addr = null;
    let hook_call_constructors_addr = true;

    const linkerName = Process.pointerSize === 4 ? "linker" : "linker64";
    const linker = Process.findModuleByName(linkerName);

    let symbols = linker.enumerateSymbols();
    for (let index = 0; index < symbols.length; index++) {
        let symbol = symbols[index];
        if (symbol.name == "__dl__ZN6soinfo17call_constructorsEv") {
            call_constructors_addr = symbol.address;
        } else if (symbol.name == "__dl__ZNK6soinfo10get_sonameEv") {
            get_soname = new NativeFunction(symbol.address, "pointer", ["pointer"]);
        }
    }

    // hook_file_read()
    if (hook_call_constructors_addr && call_constructors_addr && get_soname) {
        Interceptor.attach(call_constructors_addr, {
            onEnter: function (args) {
                let soinfo = args[0];
                let soname = get_soname(soinfo).readCString();
                if (soname && soname.includes('libtiny.so')) {
                    var so = Process.findModuleByName(soname)
                    console.log('so_base:' + so.base)
                    hook_function()
                }
            }
        });
    }
}

function main(){
    hook_call_constructors_test()
}


setImmediate(main);
