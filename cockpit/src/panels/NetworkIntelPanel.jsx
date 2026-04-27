import React, { useState, useMemo } from "react";
import "./symbolic-panel.css"; // reuse styling baseline if you want

const ROUTING_MODES = ["VPN", "Tor", "Proxy"];

const FIREWALL_PROFILES = ["Basic", "Moderate", "Advanced DPI"];

const OBFUSCATION_MODES = ["Off", "TLS Camouflage", "obfs4"];

function NetworkIntelPanel() {
  const [routingMode, setRoutingMode] = useState("VPN");
  const [firewallProfile, setFirewallProfile] = useState("Moderate");
  const [obfuscationMode, setObfuscationMode] = useState("Off");

  const routingMetrics = useMemo(() => {
    switch (routingMode) {
      case "VPN":
        return {
          exitIp: "185.22.91.14",
          encryption: "AES‑256 / WireGuard",
          latency: "42 ms",
          obfuscation: obfuscationMode,
        };
      case "Tor":
        return {
          exitIp: "Random Tor Exit",
          encryption: "Multi‑layer (3 hops)",
          latency: "180 ms",
          obfuscation: "Built‑in onion routing",
        };
      case "Proxy":
        return {
          exitIp: "203.0.113.50",
          encryption: "None (unless HTTPS)",
          latency: "25 ms",
          obfuscation: "None",
        };
      default:
        return {};
    }
  }, [routingMode, obfuscationMode]);

  const dpiResult = useMemo(() => {
    // Simple heuristic simulator
    if (firewallProfile === "Basic") {
      return {
        detected: false,
        fingerprint: "Looks like generic HTTPS",
        notes: [
          "Firewall only checks ports and basic patterns.",
          "Obfuscation not required to evade detection.",
        ],
      };
    }

    if (firewallProfile === "Moderate") {
      if (routingMode === "Proxy" && obfuscationMode === "Off") {
        return {
          detected: true,
          fingerprint: "Plain HTTP/HTTPS via known proxy IP",
          notes: [
            "Proxy IP range is on a known list.",
            "No obfuscation → easy to classify.",
          ],
        };
      }
      if (routingMode === "VPN" && obfuscationMode === "Off") {
        return {
          detected: true,
          fingerprint: "TLS fingerprint matches common VPN client",
          notes: [
            "DPI matches TLS handshake to VPN signature.",
            "Obfuscation could break this match.",
          ],
        };
      }
      return {
        detected: false,
        fingerprint: "TLS 1.3 (Chrome‑like)",
        notes: [
          "Obfuscation mutates fingerprint.",
          "Traffic blends with normal web browsing.",
        ],
      };
    }

    // Advanced DPI
    if (firewallProfile === "Advanced DPI") {
      if (obfuscationMode === "Off") {
        return {
          detected: true,
          fingerprint: "High‑entropy tunnel with stable timing",
          notes: [
            "Advanced DPI correlates timing, entropy, and SNI.",
            "Tunnel is flagged as probable VPN/Tor.",
          ],
        };
      }
      if (obfuscationMode === "TLS Camouflage") {
        return {
          detected: false,
          fingerprint: "Indistinguishable from major CDN traffic",
          notes: [
            "TLS parameters mimic Chrome → CDN.",
            "Blocking this would break many sites.",
          ],
        };
      }
      if (obfuscationMode === "obfs4") {
        return {
          detected: false,
          fingerprint: "Randomized, non‑signatured stream",
          notes: [
            "obfs4 defeats signature‑based detection.",
            "Only coarse blocking (all encrypted traffic) would catch this.",
          ],
        };
      }
    }

    return {
      detected: false,
      fingerprint: "Unknown",
      notes: ["No clear DPI outcome."],
    };
  }, [routingMode, firewallProfile, obfuscationMode]);

  const geoInfo = useMemo(() => {
    switch (routingMode) {
      case "VPN":
        return {
          ip: routingMetrics.exitIp,
          country: "France",
          region: "Île‑de‑France",
          isp: "OVH SAS (Hosting)",
          accuracy: "95%",
          signals: [
            "RIR Allocation: RIPE → FR",
            "BGP Routing: AS16276",
            "Latency Triangulation: Paris cluster",
            "Hosting Metadata: OVH Datacenter",
          ],
        };
      case "Tor":
        return {
          ip: "Tor Exit Node",
          country: "Varies",
          region: "Unknown",
          isp: "Volunteer Exit Operator",
          accuracy: "Low",
          signals: [
            "RIR Allocation: Depends on exit node",
            "BGP Routing: Volunteer AS",
            "Latency Triangulation: Wide variance",
            "Hosting Metadata: Mixed (residential / hosting)",
          ],
        };
      case "Proxy":
        return {
          ip: routingMetrics.exitIp,
          country: "United States",
          region: "California",
          isp: "Residential ISP (Example)",
          accuracy: "90%",
          signals: [
            "RIR Allocation: ARIN → US",
            "BGP Routing: Residential AS",
            "Latency Triangulation: US West",
            "Hosting Metadata: Residential range",
          ],
        };
      default:
        return {};
    }
  }, [routingMode, routingMetrics.exitIp]);

  return (
    <div className="panel-root symbolic-panel">
      <h2 className="panel-title">Network Intelligence Deck</h2>
      <p className="panel-subtitle">
        Traffic routing, DPI vs obfuscation, and geolocation—visualized as a cockpit organ.
      </p>

      <div className="panel-grid">
        {/* Traffic Routing Organ */}
        <section className="panel-card">
          <h3>Traffic Routing Organ</h3>
          <div className="button-row">
            {ROUTING_MODES.map((mode) => (
              <button
                key={mode}
                className={
                  "pill-button" + (routingMode === mode ? " pill-button-active" : "")
                }
                onClick={() => setRoutingMode(mode)}
              >
                {mode}
              </button>
            ))}
          </div>

          <div className="metrics-block">
            <div className="metric-row">
              <span className="metric-label">Exit IP:</span>
              <span className="metric-value">{routingMetrics.exitIp}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Encryption:</span>
              <span className="metric-value">{routingMetrics.encryption}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Latency:</span>
              <span className="metric-value">{routingMetrics.latency}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Obfuscation:</span>
              <span className="metric-value">{routingMetrics.obfuscation}</span>
            </div>
          </div>

          <RoutingDiagram routingMode={routingMode} />
        </section>

        {/* DPI vs Obfuscation Simulator */}
        <section className="panel-card">
          <h3>DPI vs Obfuscation Simulator</h3>

          <div className="control-group">
            <label className="control-label">Firewall Profile</label>
            <div className="button-row">
              {FIREWALL_PROFILES.map((profile) => (
                <button
                  key={profile}
                  className={
                    "pill-button" +
                    (firewallProfile === profile ? " pill-button-active" : "")
                  }
                  onClick={() => setFirewallProfile(profile)}
                >
                  {profile}
                </button>
              ))}
            </div>
          </div>

          <div className="control-group">
            <label className="control-label">Obfuscation Mode</label>
            <div className="button-row">
              {OBFUSCATION_MODES.map((mode) => (
                <button
                  key={mode}
                  className={
                    "pill-button" +
                    (obfuscationMode === mode ? " pill-button-active" : "")
                  }
                  onClick={() => setObfuscationMode(mode)}
                >
                  {mode}
                </button>
              ))}
            </div>
          </div>

          <div className="dpi-result">
            <div className="metric-row">
              <span className="metric-label">DPI Detection:</span>
              <span
                className={
                  "metric-value " +
                  (dpiResult.detected ? "status-bad" : "status-good")
                }
              >
                {dpiResult.detected ? "Detected" : "Not Detected"}
              </span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Fingerprint:</span>
              <span className="metric-value">{dpiResult.fingerprint}</span>
            </div>
            <ul className="notes-list">
              {dpiResult.notes.map((note, idx) => (
                <li key={idx}>{note}</li>
              ))}
            </ul>
          </div>
        </section>

        {/* Geolocation Intelligence Panel */}
        <section className="panel-card">
          <h3>IP Geolocation Intelligence</h3>

          <div className="metrics-block">
            <div className="metric-row">
              <span className="metric-label">IP:</span>
              <span className="metric-value">{geoInfo.ip}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Country:</span>
              <span className="metric-value">{geoInfo.country}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Region:</span>
              <span className="metric-value">{geoInfo.region}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">ISP:</span>
              <span className="metric-value">{geoInfo.isp}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Accuracy:</span>
              <span className="metric-value">{geoInfo.accuracy}</span>
            </div>
          </div>

          <div className="signals-block">
            <h4>Signal Sources</h4>
            <ul className="notes-list">
              {geoInfo.signals?.map((s, idx) => (
                <li key={idx}>{s}</li>
              ))}
            </ul>
          </div>

          <div className="map-placeholder">
            <span className="map-dot">●</span>
            <span className="map-label">
              {geoInfo.country} — {geoInfo.region}
            </span>
          </div>
        </section>
      </div>
    </div>
  );
}

function RoutingDiagram({ routingMode }) {
  if (routingMode === "VPN") {
    return (
      <pre className="diagram-block">
{String.raw`[Your Device]
    |
    |  Encrypt all traffic (VPN client)
    v
[Encrypted Tunnel]
    |
    v
[VPN Server]  →  [Destination Website]`}
      </pre>
    );
  }

  if (routingMode === "Tor") {
    return (
      <pre className="diagram-block">
{String.raw`[Your Device]
    |
    |  Encrypt 3 layers (onion)
    v
[Entry Node]
    |
    v
[Middle Node]
    |
    v
[Exit Node]  →  [Destination Website]`}
      </pre>
    );
  }

  // Proxy
  return (
    <pre className="diagram-block">
{String.raw`[Your Device]
    |
    |  No encryption (unless HTTPS)
    v
[Proxy Server]  →  [Destination Website]`}
    </pre>
  );
}

export default NetworkIntelPanel;
