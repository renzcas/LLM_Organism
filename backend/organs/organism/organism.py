import json
import importlib
from pathlib import Path

class Organism:
    def __init__(self):
        self.organs = {}
        self.registry_path = Path(__file__).parent / "organs.json"
        self.load_organs()

    def load_organs(self):
        """
        Loads all organs defined in organs.json.
        Dynamically imports each module and instantiates the organ class.
        """
        if not self.registry_path.exists():
            raise FileNotFoundError(f"Organ registry not found: {self.registry_path}")

        with open(self.registry_path, "r") as f:
            registry = json.load(f)

        for entry in registry:
            if not entry.get("active", False):
                continue

            module_path = entry["module"]
            class_name = entry["class"]
            organ_name = entry["name"]

            try:
                module = importlib.import_module(module_path)
                cls = getattr(module, class_name)
                instance = cls()
                self.organs[organ_name] = instance
                print(f"[Organism] Loaded organ: {organ_name}")

            except Exception as e:
                print(f"[Organism] Failed to load organ {organ_name}: {e}")

    def get(self, organ_name: str):
        """
        Retrieve an organ instance by name.
        """
        return self.organs.get(organ_name)

    def health(self):
        """
        Returns health status of all loaded organs.
        """
        return {
            name: organ.health() if hasattr(organ, "health") else {"status": "unknown"}
            for name, organ in self.organs.items()
        }
