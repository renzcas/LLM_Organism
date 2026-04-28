import json
import re

def parse_sdm(text_file, out_file):
    ops = []
    with open(text_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current = None

    for line in lines:
        line = line.strip()

        # Detect mnemonic
        m = re.match(r"^([A-Z][A-Z0-9]+)\s+", line)
        if m:
            if current:
                ops.append(current)
            current = {"mnemonic": m.group(1).lower(), "encodings": []}
            continue

        # Detect opcode encoding
        if current and "opcode" in line.lower():
            current["encodings"].append({"opcode": line})

    if current:
        ops.append(current)

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(ops, f, indent=2)

    print("Done:", out_file)
