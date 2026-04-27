# backend/organs/network_intel/routing_engine.py

class RoutingEngine:
    """
    Handles VPN / Tor / Proxy routing simulation.
    """

    def get_routing_info(self, mode: str) -> dict:
        if mode == "VPN":
            return {
                "exit_ip": "185.22.91.14",
                "encryption": "AES-256 / WireGuard",
                "latency": "42 ms",
                "obfuscation": "Off",
            }

        if mode == "Tor":
            return {
                "exit_ip": "Tor Exit Node",
                "encryption": "Multi-layer (3 hops)",
                "latency": "180 ms",
                "obfuscation": "Onion Routing",
            }

        if mode == "Proxy":
            return {
                "exit_ip": "203.0.113.50",
                "encryption": "None",
                "latency": "25 ms",
                "obfuscation": "None",
            }

        return {"error": "Unknown routing mode"}
