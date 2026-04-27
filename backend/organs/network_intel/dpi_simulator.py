# backend/organs/network_intel/dpi_simulator.py

class DPISimulator:
    """
    Simulates DPI detection vs obfuscation.
    """

    def analyze(self, routing_mode: str, firewall: str, obfuscation: str) -> dict:
        # Basic firewall
        if firewall == "Basic":
            return {
                "detected": False,
                "fingerprint": "Generic HTTPS",
                "notes": [
                    "Basic firewall only checks ports and simple patterns.",
                    "Obfuscation not required."
                ]
            }

        # Moderate firewall
        if firewall == "Moderate":
            if routing_mode == "Proxy" and obfuscation == "Off":
                return {
                    "detected": True,
                    "fingerprint": "Known proxy IP range",
                    "notes": ["Proxy IP flagged in known lists."]
                }

            if routing_mode == "VPN" and obfuscation == "Off":
                return {
                    "detected": True,
                    "fingerprint": "TLS fingerprint matches VPN client",
                    "notes": ["DPI matched TLS handshake signature."]
                }

            return {
                "detected": False,
                "fingerprint": "TLS 1.3 (Chrome-like)",
                "notes": ["Obfuscation mutated fingerprint."]
            }

        # Advanced DPI
        if firewall == "Advanced DPI":
            if obfuscation == "Off":
                return {
                    "detected": True,
                    "fingerprint": "High-entropy tunnel",
                    "notes": ["Timing + entropy correlation triggered detection."]
                }

            if obfuscation == "TLS Camouflage":
                return {
                    "detected": False,
                    "fingerprint": "CDN-like TLS parameters",
                    "notes": ["Indistinguishable from major CDN traffic."]
                }

            if obfuscation == "obfs4":
                return {
                    "detected": False,
                    "fingerprint": "Randomized obfs4 stream",
                    "notes": ["Signature-based detection defeated."]
                }

        return {"detected": False, "fingerprint": "Unknown", "notes": []}
