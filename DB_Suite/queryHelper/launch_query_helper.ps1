# Query Helper Suite Launcher

Write-Host "=== FUSION METADATA QUERY HELPER ===" -ForegroundColor Cyan

# 1. Verify Dependencies
Write-Host "[1/3] Installing backend dependencies..." -ForegroundColor Yellow
cd backend
npm install --silent

# 2. Check KB2 Sidecar
Write-Host "[2/3] Checking KB2 Embedding Sidecar..." -ForegroundColor Yellow
$sidecar = Get-NetTCPConnection -LocalPort 5002 -ErrorAction SilentlyContinue
if ($null -eq $sidecar) {
    Write-Host "WARNING: KB2 Sidecar is NOT running on port 5002." -ForegroundColor Red
    Write-Host "Semantic search will be disabled. Run 'kb2_launch.ps1' to enable it." -ForegroundColor Gray
} else {
    Write-Host "SUCCESS: KB2 Sidecar detected. Semantic search active." -ForegroundColor Green
}

# 3. Launch Backend
Write-Host "[3/3] Launching Backend API on Port 3005..." -ForegroundColor Yellow
Start-Process cmd -ArgumentList "/k", "title Query-Helper-Backend && node server.js"

Write-Host "`nSUCCESS: Query Helper is starting." -ForegroundColor Green
Write-Host "Open your browser to: http://localhost:3005" -ForegroundColor Gray
