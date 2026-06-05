#!/bin/bash
echo ""
echo "====================================================="
echo " ACE - Autonomous Cognitive Engine"
echo "====================================================="
echo ""

set -e
cd "$( dirname "${BASH_SOURCE[0]}" )"

echo "[1/3] Checking Python..."
python3 --version
echo ""

echo "[2/3] Creating environment and installing packages..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -q -r requirements.txt
echo "Done"
echo ""

echo "[3/3] Starting ACE..."
echo ""
echo "====================================================="
echo " ACE is running at http://localhost:5000"
echo " Press Ctrl+C to stop"
echo "====================================================="
echo ""

python3 main.py
