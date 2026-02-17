@echo off
REM Test script for RouterAI API Client
REM Sets API key and runs test

echo ============================================================
echo RouterAI API Client - Test Runner
echo ============================================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Check if API key is set
if "%ROUTERAI_API_KEY%"=="" (
    echo ERROR: ROUTERAI_API_KEY environment variable is not set!
    echo.
    echo Please set your API key first:
    echo   set ROUTERAI_API_KEY=your-api-key-here
    echo.
    echo Get API key from: https://routerai.ru/pages/vibe-coding-vscode-cline
    echo.
    goto :end
)

REM Run test
python test_api.py

:end

echo.
echo ============================================================
echo Press any key to exit...
pause >nul
