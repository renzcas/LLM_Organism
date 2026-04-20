import re
import os
import sys
from pathlib import Path

RAW_FILE = "conversation_intake/raw.txt"
OUT_DIR = Path("conversation_intake/incoming")

CODE_BLOCK = re.compile(r"```(.*?)```", re.DOTALL)

def main():
    if not os.path.exists(RAW_FILE):
        print("No raw.txt found.")
        return

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    blocks = CODE_BLOCK.findall(text)

    if not blocks:
        print("No code blocks found.")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for i, block in enumerate(blocks, start=1):
        ext = detect_extension(block)
        filename = OUT_DIR / f"block_{i}{ext}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(block.strip())

    print(f"Extracted {len(blocks)} code blocks.")

def detect_extension(block: str):
    if block.strip().startswith("import") or "def " in block:
        return ".py"
    if block.strip().startswith("{"):
        return ".json"
    if block.strip().startswith("resource") or "terraform" in block.lower():
        return ".tf"
    if block.strip().startswith("<"):
        return ".html"
    if ":" in block.split("\n")[0]:
        return ".yml"
    return ".txt"

if __name__ == "__main__":
    main()
