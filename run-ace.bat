@echo off
REM ACE - Autonomous Cognitive Engine startup script for Windows

echo ========================================
echo  ACE - Autonomous Cognitive Engine
echo  Windows Startup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Python found
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [2/5] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
) else (
    echo [2/5] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Copy .env if it doesn't exist
if not exist ".env" (
    echo [5/5] Creating .env file from template...
    copy .env.example .env
)
echo.

echo ========================================
echo  Starting ACE Backend (Port 5000)...
echo ========================================
echo.

REM Start the backend
python main.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start ACE
    pause
    exit /b 1
)

pause
