import json
from pathlib import Path

DATA = Path(__file__).parent / "data"

class OpcodeKnowledge:
    def __init__(self):
        self.x86_32 = self._load("x86_32.json")
        self.x86_64 = self._load("x86_64.json")
        self.ida_map = self._load("ida_map.json")
        self.categories = self._load("categories.json")
        self.flags = self._load("flags.json")

    def _load(self, name):
        path = DATA / name
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def lookup(self, mnemonic, mode="x86_64"):
        table = self.x86_64 if mode == "x86_64" else self.x86_32
        m = mnemonic.lower()
        return [op for op in table if op.get("mnemonic", "").lower() == m]

    def normalize_ida(self, ida_mnemonic):
        return self.ida_map.get(ida_mnemonic.lower())

    def category_of(self, mnemonic):
        for cat, ops in self.categories.items():
            if mnemonic.lower() in ops:
                return cat
        return "unknown"
