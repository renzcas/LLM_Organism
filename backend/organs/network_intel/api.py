# backend/organs/network_intel/api.py

from fastapi import APIRouter
from .routing_engine import RoutingEngine
from .dpi_simulator import DPISimulator
from .geolocation_engine import GeolocationEngine

router = APIRouter(prefix="/network-intel", tags=["Network Intelligence"])

routing_engine = RoutingEngine()
dpi_engine = DPISimulator()
geo_engine = GeolocationEngine()


@router.get("/routing")
def get_routing(mode: str):
    return routing_engine.get_routing_info(mode)


@router.get("/dpi")
def get_dpi(routing_mode: str, firewall: str, obfuscation: str):
    return dpi_engine.analyze(routing_mode, firewall, obfuscation)


@router.get("/geolocation")
def get_geo(routing_mode: str, exit_ip: str):
    return geo_engine.lookup(routing_mode, exit_ip)
