# backend/organs/hive.py

class HiveRegistry:
    def __init__(self):
        self.name = "HiveRegistry"
        self.version = "0.1.0"
        self.members = {}  # {id: {"status": ..., "metadata": ...}}

    def register(self, payload: dict):
        """
        Registers an organism into the hive.
        Expected payload:
        {
            "id": "unique_id",
            "metadata": {...}
        }
        """
        member_id = payload.get("id")
        metadata = payload.get("metadata", {})

        if not member_id:
            return {"error": "Missing member id"}

        self.members[member_id] = {
            "status": "active",
            "metadata": metadata
        }

        return {"registered": member_id, "count": len(self.members)}

    def update(self, payload: dict):
        """
        Updates a hive member's status or metadata.
        """
        member_id = payload.get("id")
        if member_id not in self.members:
            return {"error": "Member not found"}

        if "status" in payload:
            self.members[member_id]["status"] = payload["status"]

        if "metadata" in payload:
            self.members[member_id]["metadata"] = payload["metadata"]

        return {"updated": member_id}

    def list(self):
        """
        Returns all hive members.
        """
        return {"members": self.members}

    def health(self):
        return {
            "organ": self.name,
            "status": "ok",
            "member_count": len(self.members),
            "version": self.version
        }
