@echo off
title KB Sidecar Shutdown
setlocal enabledelayedexpansion

echo ========================================
echo   KB KNOWLEDGE SYSTEM: SIDECAR STOP
echo ========================================

:: Port for the Sidecar
set PORT=5002

echo Searching for KB processes on port %PORT%...

set FOUND=0
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :%PORT% ^| findstr LISTENING') do (
    echo   Killing process PID %%a on port %PORT%...
    taskkill /F /PID %%a >nul 2>&1
    set FOUND=1
)

if %FOUND%==0 (
    echo No active Sidecar processes found on port %PORT%.
) else (
    echo Sidecar has been stopped.
)

echo.
echo DONE.
timeout /t 3

