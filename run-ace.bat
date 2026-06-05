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
echo  Automated Setup and Launch
echo ======================================================
echo.

REM Get current directory
set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

REM =====================================================
REM Step 1: Check Python Installation
REM =====================================================
echo [STEP 1/5] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python not found
    echo.
    echo Download from: https://www.python.org
    echo Make sure to CHECK "Add Python to PATH" during install
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do echo        %%i
echo.

REM =====================================================
REM Step 2: Create Virtual Environment
REM =====================================================
echo [STEP 2/5] Setting up environment...
if not exist "venv" (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Could not create environment
        pause
        exit /b 1
    )
)
call venv\Scripts\activate.bat
echo.

REM =====================================================
REM Step 3: Install Dependencies
REM =====================================================
echo [STEP 3/5] Installing dependencies (this takes ~1 minute)...
python -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
if errorlevel 1 (
    echo.
    echo ERROR: Installation failed
    echo.
    echo Try this command manually:
    echo pip install -r requirements.txt --no-binary :all: --no-cache-dir
    echo.
    pause
    exit /b 1
)
echo.

REM =====================================================
REM Step 4: Setup Configuration
REM =====================================================
echo [STEP 4/5] Preparing workspace...
if not exist ".env" copy .env.example .env
mkdir logs 2>nul
mkdir artifacts 2>nul
mkdir artifacts\projects 2>nul
mkdir artifacts\code_snippets 2>nul
mkdir artifacts\memory 2>nul
echo.

REM =====================================================
REM Step 5: Launch ACE
REM =====================================================
echo [STEP 5/5] Starting ACE...
echo.
echo ======================================================
echo  ACE Backend Running
echo ======================================================
echo.
echo  URL: http://localhost:5000
echo  Health: http://localhost:5000/health
echo.
echo  Press Ctrl+C to stop
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: ACE failed
    echo.
    pause
    exit /b 1
)

pause
