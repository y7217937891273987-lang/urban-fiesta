@echo off
REM =====================================================
REM ACE - Autonomous Cognitive Engine
REM Complete Automated Setup & Startup for Windows
REM Just double-click this file - it does EVERYTHING
REM =====================================================

setlocal enabledelayedexpansion

echo.
echo ======================================================
echo  ACE - Autonomous Cognitive Engine
echo  Automated Setup & Launch
echo ======================================================
echo.

REM Get current directory
set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

REM =====================================================
REM Step 1: Check Python Installation
REM =====================================================
echo [STEP 1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo SOLUTION:
    echo 1. Download Python 3.8+ from https://www.python.org
    echo 2. During installation, CHECK "Add Python to PATH"
    echo 3. Click "Install Now"
    echo 4. After installation, run this script again
    echo.
    pause
    exit /b 1
)
echo [DONE] Python found: 
for /f "tokens=*" %%i in ('python --version') do echo        %%i
echo.

REM =====================================================
REM Step 2: Create Virtual Environment (if needed)
REM =====================================================
echo [STEP 2/6] Setting up Python environment...
if not exist "venv" (
    echo        Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [DONE] Virtual environment created
) else (
    echo [DONE] Virtual environment already exists
)
echo.

REM =====================================================
REM Step 3: Activate Virtual Environment
REM =====================================================
echo [STEP 3/6] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo [DONE] Environment activated
echo.

REM =====================================================
REM Step 4: Upgrade pip (important!)
REM =====================================================
echo [STEP 4/6] Upgrading pip and installing dependencies...
echo        This may take 2-3 minutes. Please wait...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo WARNING: pip upgrade had issues, continuing anyway...
)

REM Install requirements with error handling
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo.
    echo TROUBLESHOOTING:
    echo 1. Check your internet connection
    echo 2. Try running this command manually:
    echo    pip install -r requirements.txt --no-cache-dir
    echo 3. If issues persist, check logs/pip_error.log
    echo.
    pause
    exit /b 1
)
echo [DONE] All dependencies installed
echo.

REM =====================================================
REM Step 5: Create .env Configuration
REM =====================================================
echo [STEP 5/6] Setting up configuration...
if not exist ".env" (
    echo        Creating .env file...
    copy .env.example .env >nul 2>&1
    if errorlevel 1 (
        echo WARNING: Could not copy .env, using defaults
    )
    echo [DONE] Configuration created
) else (
    echo [DONE] Configuration already exists
)
echo.

REM =====================================================
REM Step 6: Create Required Directories
REM =====================================================
echo [STEP 6/6] Preparing workspace...
if not exist "logs" mkdir logs
if not exist "artifacts" mkdir artifacts
if not exist "artifacts\projects" mkdir artifacts\projects
if not exist "artifacts\code_snippets" mkdir artifacts\code_snippets
if not exist "artifacts\memory" mkdir artifacts\memory
if not exist "artifacts\downloads" mkdir artifacts\downloads
echo [DONE] Workspace ready
echo.

REM =====================================================
REM Launch ACE
REM =====================================================
echo ======================================================
echo  LAUNCHING ACE BACKEND
echo ======================================================
echo.
echo  Backend: http://localhost:5000
echo  Health:  http://localhost:5000/health
echo.
echo  Press Ctrl+C to stop
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: ACE failed to start
    echo.
    echo Troubleshooting:
    echo 1. Ensure port 5000 is not in use
    echo 2. Check that Python 3.8+ is installed
    echo 3. Review logs in the 'logs' folder
    echo.
    pause
    exit /b 1
)

pause
