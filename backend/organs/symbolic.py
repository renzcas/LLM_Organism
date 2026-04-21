# backend/organs/symbolic.py

class SymbolicOrgan:
    def __init__(self):
        self.name = "SymbolicOrgan"
        self.version = "0.1.0"

    def compute(self, payload: dict):
        """
        Converts raw inputs into symbolic structures.
        Expected payload:
        {
            "tokens": [...],
            "mode": "pairs" | "triples" | "graph"
        }
        """
        tokens = payload.get("tokens", [])
        mode = payload.get("mode", "pairs")

        if not tokens:
            return {"error": "No tokens provided"}

        if mode == "pairs":
            symbols = [(tokens[i], tokens[i+1]) 
                       for i in range(len(tokens)-1)]

        elif mode == "triples":
            symbols = [(tokens[i], tokens[i+1], tokens[i+2]) 
                       for i in range(len(tokens)-2)]

        elif mode == "graph":
            symbols = {
                "nodes": list(set(tokens)),
                "edges": [(tokens[i], tokens[i+1]) 
                          for i in range(len(tokens)-1)]
            }

        else:
            return {"error": f"Unknown mode: {mode}"}

        return {
            "organ": self.name,
            "version": self.version,
            "mode": mode,
            "symbols": symbols
        }

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "version": self.version
        }
