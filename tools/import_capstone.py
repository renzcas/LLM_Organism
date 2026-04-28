from capstone import *
import json

def dump_x86(mode, out_file):
    if mode == 64:
        cs = Cs(CS_ARCH_X86, CS_MODE_64)
    else:
        cs = Cs(CS_ARCH_X86, CS_MODE_32)

    ops = []

    for ins in cs.disasm(b"\x90\x90\x90", 0x1000):
        # This is a hack: Capstone doesn't expose full opcode tables directly.
        # But we can still extract mnemonics and operand types.
        ops.append({
            "mnemonic": ins.mnemonic,
            "op_str": ins.op_str
        })

    with open(out_file, "w") as f:
        json.dump(ops, f, indent=2)

dump_x86(64, "backend/organs/opcode_knowledge/data/x86_64.json")
dump_x86(32, "backend/organs/opcode_knowledge/data/x86_32.json")
