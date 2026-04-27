import { useState, useEffect, useCallback } from "react";

export function useNetworkIntel() {
  const [routing, setRouting] = useState(null);
  const [dpi, setDpi] = useState(null);
  const [geo, setGeo] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchRouting = useCallback(async (mode) => {
    try {
      setLoading(true);
      const res = await fetch(`/network-intel/routing?mode=${mode}`);
      const data = await res.json();
      setRouting(data);
      setError(null);
    } catch (err) {
      setError("Routing fetch failed");
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchDpi = useCallback(async (routingMode, firewall, obfuscation) => {
    try {
      setLoading(true);
      const url = `/network-intel/dpi?routing_mode=${routingMode}&firewall=${firewall}&obfuscation=${obfuscation}`;
      const res = await fetch(url);
      const data = await res.json();
      setDpi(data);
      setError(null);
    } catch (err) {
      setError("DPI fetch failed");
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchGeo = useCallback(async (routingMode, exitIp) => {
    try {
      setLoading(true);
      const url = `/network-intel/geolocation?routing_mode=${routingMode}&exit_ip=${exitIp}`;
      const res = await fetch(url);
      const data = await res.json();
      setGeo(data);
      setError(null);
    } catch (err) {
      setError("Geolocation fetch failed");
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    routing,
    dpi,
    geo,
    loading,
    error,
    fetchRouting,
    fetchDpi,
    fetchGeo,
  };
}
