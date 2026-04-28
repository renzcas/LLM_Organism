#!/bin/bash

echo "Scaffolding LLM_Organism structure..."

# Backend core
mkdir -p backend/core
mkdir -p backend/api
mkdir -p backend/ecosystem

# Organs
mkdir -p backend/organs/reverse_engineering
mkdir -p backend/organs/opcode_knowledge/data
mkdir -p backend/organs/symbolic_exec
mkdir -p backend/organs/cfg_visualizer
mkdir -p backend/organs/func_fingerprinting
mkdir -p backend/organs/memory_model
mkdir -p backend/organs/ssa_engine
mkdir -p backend/organs/solver
mkdir -p backend/organs/callgraph
mkdir -p backend/organs/teaching

# Frontend cockpit
mkdir -p frontend/cockpit/panels
mkdir -p frontend/cockpit/layout
mkdir -p frontend/assets

# Opcode knowledge starter files
touch backend/organs/opcode_knowledge/engine.py
touch backend/organs/opcode_knowledge/api.py
touch backend/organs/opcode_knowledge/__init__.py

# Data files
touch backend/organs/opcode_knowledge/data/x86_32.json
touch backend/organs/opcode_knowledge/data/x86_64.json
touch backend/organs/opcode_knowledge/data/ida_map.json
touch backend/organs/opcode_knowledge/data/categories.json
touch backend/organs/opcode_knowledge/data/flags.json

# Teaching panel frontend
touch frontend/cockpit/panels/OpcodeCard.jsx

echo "Done. Your organism skeleton is ready."
