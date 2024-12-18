# Directory to store logs
$logDir = "container_logs"
if (-Not (Test-Path -Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir
}

# Get all running Docker containers
$containers = docker ps --format "{{.Names}}"

# Loop through each container and extract error logs
foreach ($container in $containers) {
    Write-Host "Fetching logs for container: $container"

    # Extract logs and filter for errors
    $logFile = "$logDir\$container`_error.log"
    docker logs $container 2>&1 | Select-String -Pattern "error" -CaseSensitive | Out-File -FilePath $logFile
}

Write-Host "All error logs saved to $logDir directory."
