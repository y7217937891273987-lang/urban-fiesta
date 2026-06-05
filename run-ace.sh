#!/bin/bash

# ACE - Autonomous Cognitive Engine startup script for macOS/Linux

echo "========================================"
echo " ACE - Autonomous Cognitive Engine"
echo " macOS/Linux Startup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[1/5] Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[2/5] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
else
    echo "[2/5] Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo ""

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo ""

# Copy .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "[5/5] Creating .env file from template..."
    cp .env.example .env
fi
echo ""

echo "========================================"
echo " Starting ACE Backend (Port 5000)..."
echo "========================================"
echo ""

# Start the backend
python main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to start ACE"
    exit 1
fi
