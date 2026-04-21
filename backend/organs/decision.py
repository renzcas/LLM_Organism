# backend/organs/decision.py

class DecisionOrgan:
    def __init__(self):
        self.name = "DecisionOrgan"
        self.version = "0.1.0"

    def compute(self, payload: dict):
        """
        Selects an action based on symbolic inputs.
        Expected payload:
        {
            "symbols": [...],
            "policy": "max" | "min" | "first" | "random"
        }
        """
        import random

        symbols = payload.get("symbols", [])
        policy = payload.get("policy", "first")

        if not symbols:
            return {"error": "No symbols provided"}

        if policy == "first":
            action = symbols[0]

        elif policy == "max":
            action = max(symbols)

        elif policy == "min":
            action = min(symbols)

        elif policy == "random":
            action = random.choice(symbols)

        else:
            return {"error": f"Unknown policy: {policy}"}

        return {
            "organ": self.name,
            "version": self.version,
            "policy": policy,
            "action": action
        }

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "version": self.version
        }
