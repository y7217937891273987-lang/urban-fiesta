@echo off
REM ACE - Autonomous Cognitive Engine
REM Windows Startup - NO BUILD TOOLS NEEDED
REM This is the ONLY command you need to run

setlocal enabledelayedexpansion

echo.
echo ======================================================
echo  ACE - Autonomous Cognitive Engine
echo ======================================================
echo.

cd /d "%~dp0"

echo [1/3] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Download from python.org
    pause
    exit /b 1
)
echo Done
echo.

echo [2/3] Creating environment and installing packages...
if not exist "venv" python -m venv venv
call venv\Scripts\activate.bat
pip install --quiet -r requirements.txt 2>nul
echo Done
echo.

echo [3/3] Starting ACE...
echo.
echo ======================================================
echo  ACE is running at http://localhost:5000
echo  Press Ctrl+C to stop
echo ======================================================
echo.

python main.py
pause
