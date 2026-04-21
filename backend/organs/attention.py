# backend/organs/attention.py

class AttentionOrgan:
    def __init__(self):
        self.name = "AttentionOrgan"
        self.version = "0.1.0"

    def compute(self, payload: dict):
        """
        Core attention computation.
        Expected payload:
        {
            "inputs": [...],
            "weights": [...optional...]
        }
        """
        inputs = payload.get("inputs", [])
        weights = payload.get("weights")

        if not inputs:
            return {"error": "No inputs provided"}

        # If no weights provided, generate uniform weights
        if weights is None:
            weights = [1.0 for _ in inputs]

        # Normalize weights
        total = sum(weights)
        if total == 0:
            normalized = [0 for _ in weights]
        else:
            normalized = [w / total for w in weights]

        # Apply attention weighting
        output = []
        for value, weight in zip(inputs, normalized):
            output.append(value * weight)

        return {
            "organ": self.name,
            "version": self.version,
            "inputs": inputs,
            "weights": normalized,
            "output": output
        }

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "version": self.version
        }