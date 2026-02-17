# PowerShell test script for RouterAI API Client
# Run this script to test the API integration

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "RouterAI API Client - Test Runner (PowerShell)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Check if API key is set
if (-not $env:ROUTERAI_API_KEY) {
    Write-Host "ERROR: ROUTERAI_API_KEY environment variable is not set!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please set your API key first:" -ForegroundColor Yellow
    Write-Host '  $env:ROUTERAI_API_KEY="your-api-key-here"' -ForegroundColor Green
    Write-Host ""
    Write-Host "Get API key from: https://routerai.ru/pages/vibe-coding-vscode-cline" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Run test
Write-Host "Running test..." -ForegroundColor Green
Write-Host ""
python test_api.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
