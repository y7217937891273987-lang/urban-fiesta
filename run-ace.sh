#!/bin/bash

# =====================================================
# ACE - Autonomous Cognitive Engine
# Automated Setup and Launch
# =====================================================

echo ""
echo "====================================================="
echo " ACE - Autonomous Cognitive Engine"
echo " Automated Setup and Launch"
echo "====================================================="
echo ""

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# =====================================================
# Step 1: Check Python
# =====================================================
echo "[STEP 1/5] Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "ERROR: Python 3 not found"
    echo ""
    echo "Install with:"
    echo "  macOS: brew install python3"
    echo "  Ubuntu: sudo apt-get install python3 python3-venv"
    echo ""
    exit 1
fi
python3 --version
echo ""

# =====================================================
# Step 2: Create Virtual Environment
# =====================================================
echo "[STEP 2/5] Setting up environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
echo ""

# =====================================================
# Step 3: Install Dependencies
# =====================================================
echo "[STEP 3/5] Installing dependencies (this takes ~1 minute)..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
echo ""

# =====================================================
# Step 4: Setup Configuration
# =====================================================
echo "[STEP 4/5] Preparing workspace..."
if [ ! -f ".env" ]; then
    cp .env.example .env
fi
mkdir -p logs
mkdir -p artifacts/projects
mkdir -p artifacts/code_snippets
mkdir -p artifacts/memory
echo ""

# =====================================================
# Step 5: Launch ACE
# =====================================================
echo "[STEP 5/5] Starting ACE..."
echo ""
echo "====================================================="
echo " ACE Backend Running"
echo "====================================================="
echo ""
echo " URL: http://localhost:5000"
echo " Health: http://localhost:5000/health"
echo ""
echo " Press Ctrl+C to stop"
echo ""

python3 main.py
