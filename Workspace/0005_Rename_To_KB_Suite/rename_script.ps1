
$root = "D:\HRD_TechCarrot_2\MasterAISuite-Distributable"
$items = Get-ChildItem -Path $root -Recurse -Exclude ".git", "Workspace", "node_modules", ".gemini"

# 1. Replace content in text files
$textExtensions = @(".md", ".json", ".txt", ".py", ".bat", ".ps1", ".js", ".html")
foreach ($item in $items) {
    if ($item.PSIsContainer -eq $false -and $textExtensions -contains $item.Extension) {
        $content = Get-Content -Path $item.FullName -Raw
        $newContent = $content -replace "KB_Suite", "KB_Suite"
        $newContent = $newContent -replace "KB", "KB"
        $newContent = $newContent -replace "KB", "KB"
        $newContent = $newContent -replace "KB", "KB"
        $newContent = $newContent -replace "KB\.exe", "kb.exe"
        $newContent = $newContent -replace "KB_embed_server\.py", "kb_embed_server.py"
        $newContent = $newContent -replace "KB_gateway\.py", "kb_gateway.py"
        $newContent = $newContent -replace "KB_Sidecar_Deploy", "KB_Sidecar_Deploy"
        
        if ($content -ne $newContent) {
            Set-Content -Path $item.FullName -Value $newContent -Encoding UTF8
            Write-Host "Updated content in: $($item.FullName)"
        }
    }
}

# 2. Rename files (specific names)
Get-ChildItem -Path $root -Recurse -Filter "*KB*" -Exclude ".git" | Rename-Item -NewName { $_.Name -replace "KB", "kb" } -ErrorAction SilentlyContinue
Get-ChildItem -Path $root -Recurse -Filter "*KB_Suite*" -Exclude ".git" | Rename-Item -NewName { $_.Name -replace "KB_Suite", "KB_Suite" } -ErrorAction SilentlyContinue

# 3. Rename specific directories if they still exist with old names
if (Test-Path "$root\KB_Suite") {
    Rename-Item -Path "$root\KB_Suite" -NewName "KB_Suite"
}
if (Test-Path "$root\KB_Suite\KB_Sidecar_Deploy") {
    Rename-Item -Path "$root\KB_Suite\KB_Sidecar_Deploy" -NewName "KB_Sidecar_Deploy"
}

Write-Host "Rename and content replacement complete."

