# backend/organs/memory.py

class MemoryOrgan:
    def __init__(self):
        self.name = "MemoryOrgan"
        self.version = "0.1.0"
        self.episodic = []
        self.semantic = {}

    def store(self, payload: dict):
        """
        Stores episodic or semantic memory.
        Expected payload:
        {
            "type": "episodic" | "semantic",
            "data": ...
        }
        """
        mem_type = payload.get("type")
        data = payload.get("data")

        if mem_type == "episodic":
            self.episodic.append(data)
            return {"stored": "episodic", "count": len(self.episodic)}

        elif mem_type == "semantic":
            key = payload.get("key", f"item_{len(self.semantic)}")
            self.semantic[key] = data
            return {"stored": "semantic", "key": key}

        return {"error": "Unknown memory type"}

    def retrieve(self, payload: dict):
        """
        Retrieves episodic or semantic memory.
        Expected payload:
        {
            "type": "episodic" | "semantic",
            "key": ... (for semantic)
        }
        """
        mem_type = payload.get("type")

        if mem_type == "episodic":
            return {"episodic": self.episodic}

        elif mem_type == "semantic":
            key = payload.get("key")
            if key in self.semantic:
                return {"key": key, "value": self.semantic[key]}
            return {"error": "Key not found"}

        return {"error": "Unknown memory type"}

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "episodic_count": len(self.episodic),
            "semantic_count": len(self.semantic),
            "version": self.version
        }
