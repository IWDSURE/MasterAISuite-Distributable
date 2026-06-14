@echo off
title KB Sidecar Launcher
setlocal enabledelayedexpansion

echo ========================================
echo   KB KNOWLEDGE SYSTEM: SIDECAR START
echo ========================================

:: Port for the Sidecar
set PORT=5002

echo [1/3] Cleaning up port %PORT%...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :%PORT% ^| findstr LISTENING') do (
    echo   Found process PID %%a on port %PORT%. Killing...
    taskkill /F /PID %%a >nul 2>&1
)

echo [2/3] Verifying environment...
if not exist "KB_embed_server.py" (
    echo [ERROR] KB_embed_server.py not found in current directory!
    pause
    exit /b
)
if not exist "KB_gateway.py" (
    echo [ERROR] KB_gateway.py not found in current directory!
    pause
    exit /b
)

echo [3/3] Launching Embedding Sidecar...
:: Start in a new window so logs are visible
start "KB-Sidecar-Process" python KB_embed_server.py

echo.
echo SUCCESS: Sidecar triggered.
echo Please wait ~30 seconds for the AI model to load in the new window.
echo.
timeout /t 5

