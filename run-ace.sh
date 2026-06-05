#!/bin/bash

# =====================================================
# ACE - Autonomous Cognitive Engine
# Complete Automated Setup & Startup for macOS/Linux
# Just run this script - it does EVERYTHING
# =====================================================

set -e  # Exit on error

echo ""
echo "====================================================="
echo " ACE - Autonomous Cognitive Engine"
echo " Automated Setup & Launch"
echo "====================================================="
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# =====================================================
# Step 1: Check Python Installation
# =====================================================
echo "[STEP 1/6] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "ERROR: Python 3 is not installed"
    echo ""
    echo "SOLUTION:"
    echo ""
    echo "macOS:"
    echo "  brew install python3"
    echo ""
    echo "Ubuntu/Debian:"
    echo "  sudo apt-get install python3 python3-pip python3-venv"
    echo ""
    echo "CentOS/RHEL:"
    echo "  sudo yum install python3 python3-pip"
    echo ""
    exit 1
fi
echo "[DONE] Python found: $(python3 --version)"
echo ""

# =====================================================
# Step 2: Create Virtual Environment (if needed)
# =====================================================
echo "[STEP 2/6] Setting up Python environment..."
if [ ! -d "venv" ]; then
    echo "        Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "[DONE] Virtual environment created"
else
    echo "[DONE] Virtual environment already exists"
fi
echo ""

# =====================================================
# Step 3: Activate Virtual Environment
# =====================================================
echo "[STEP 3/6] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo "[DONE] Environment activated"
echo ""

# =====================================================
# Step 4: Upgrade pip and Install Dependencies
# =====================================================
echo "[STEP 4/6] Upgrading pip and installing dependencies..."
echo "        This may take 2-3 minutes. Please wait..."
python3 -m pip install --upgrade pip setuptools wheel
if [ $? -ne 0 ]; then
    echo "WARNING: pip upgrade had issues, continuing anyway..."
fi

pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies"
    echo ""
    echo "TROUBLESHOOTING:"
    echo "1. Check your internet connection"
    echo "2. Try running this command manually:"
    echo "   pip install -r requirements.txt --no-cache-dir"
    echo "3. If issues persist, check logs"
    echo ""
    exit 1
fi
echo "[DONE] All dependencies installed"
echo ""

# =====================================================
# Step 5: Create .env Configuration
# =====================================================
echo "[STEP 5/6] Setting up configuration..."
if [ ! -f ".env" ]; then
    echo "        Creating .env file..."
    cp .env.example .env
    if [ $? -ne 0 ]; then
        echo "WARNING: Could not copy .env, using defaults"
    fi
    echo "[DONE] Configuration created"
else
    echo "[DONE] Configuration already exists"
fi
echo ""

# =====================================================
# Step 6: Create Required Directories
# =====================================================
echo "[STEP 6/6] Preparing workspace..."
mkdir -p logs
mkdir -p artifacts/projects
mkdir -p artifacts/code_snippets
mkdir -p artifacts/memory
mkdir -p artifacts/downloads
echo "[DONE] Workspace ready"
echo ""

# =====================================================
# Launch ACE
# =====================================================
echo "====================================================="
echo " LAUNCHING ACE BACKEND"
echo "====================================================="
echo ""
echo " Backend: http://localhost:5000"
echo " Health:  http://localhost:5000/health"
echo ""
echo " Press Ctrl+C to stop"
echo ""

python3 main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: ACE failed to start"
    echo ""
    echo "Troubleshooting:"
    echo "1. Ensure port 5000 is not in use"
    echo "2. Check that Python 3.8+ is installed"
    echo "3. Review logs in the 'logs' folder"
    echo ""
    exit 1
fi
