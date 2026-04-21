# backend/organs/pipeline.py

class PipelineOrgan:
    def __init__(self):
        self.name = "PipelineOrgan"
        self.version = "0.1.0"

    def run(self, payload: dict, organism):
        """
        Runs a multi-step reasoning pipeline.
        Expected payload:
        {
            "steps": [
                {"organ": "attention", "method": "compute", "payload": {...}},
                {"organ": "symbolic", "method": "compute", "payload": {...}},
                {"organ": "decision", "method": "compute", "payload": {...}},
                {"organ": "memory", "method": "store", "payload": {...}}
            ]
        }
        """
        steps = payload.get("steps", [])
        results = []

        for step in steps:
            organ_name = step.get("organ")
            method_name = step.get("method")
            step_payload = step.get("payload", {})

            organ = organism.get(organ_name)
            if not organ:
                results.append({"error": f"Organ '{organ_name}' not found"})
                continue

            method = getattr(organ, method_name, None)
            if not method:
                results.append({"error": f"Method '{method_name}' not found in organ '{organ_name}'"})
                continue

            try:
                result = method(step_payload)
                results.append(result)
            except Exception as e:
                results.append({"error": str(e)})

        return {
            "organ": self.name,
            "version": self.version,
            "results": results
        }

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "version": self.version
        }
