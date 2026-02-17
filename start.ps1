# LLM API Client - Easy Launcher
# Usage: .\start.ps1 "Your question here"

param(
    [string]$Prompt = ""
)

# Change to script directory
Set-Location $PSScriptRoot

# Check if API key is set
if (-not $env:ROUTERAI_API_KEY) {
    Write-Host ""
    Write-Host "ERROR: API key not set!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Set your API key first:" -ForegroundColor Yellow
    Write-Host '  $env:ROUTERAI_API_KEY="sk-WE-Sx1kuAb-Tr3wEyq6y3QdiCkGjlsB0"' -ForegroundColor Green
    Write-Host ""
    exit 1
}

# Run with or without prompt
if ($Prompt -ne "") {
    python llm_api_client.py $Prompt
} else {
    python llm_api_client.py
}
