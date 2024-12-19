# Directory to store logs
$logDir = "./container_logs"
if (-Not (Test-Path -Path $logDir)) {
    Write-Host "Creating log directory: $logDir"
    New-Item -ItemType Directory -Path $logDir
}

# Get all running Docker containers
$containers = docker ps --format "{{.Names}}"

# Check if containers were found
if (-Not $containers) {
    Write-Host "No running containers found."
    return
}

# Loop through each container and extract logs
foreach ($container in $containers) {
    Write-Host "Fetching logs for container: $container"

    # Extract logs
    $logFile = "$logDir\$container`_error.log"
    $logs = docker logs $container | Out-String

    # Debugging: Check if raw logs were retrieved
    if (-Not $logs) {
        Write-Host "No logs found for container: $container"
        continue
    } else {
        Write-Host "Raw logs retrieved for container: $container"
    }

    # Split logs into lines
    $logLines = $logs -split "`n"

    # Truncate to the last 100 lines if there are more than 1000 lines
    if ($logLines.Count -gt 1000) {
        $logLines = $logLines[-100..-1]  # Get the last 100 lines
        Write-Host "Log truncated to the last 100 lines for container: $container"
    }

    # Write raw logs directly for debugging
    $rawLogFile = "$logDir\$container`.log"
    $logLines | Out-File -FilePath $rawLogFile -Encoding UTF8
    Write-Host "Raw logs saved to $rawLogFile"

    # Filter logs for errors
    $filteredLogs = $logLines | Select-String -Pattern "(?i)error" | ForEach-Object { $_.ToString() }

    # Debugging: Check if filtered logs exist
    if (-Not $filteredLogs) {
        Write-Host "No errors found for container: $container"
        continue
    } else {
        Write-Host "Filtered error logs retrieved for container: $container"
    }

    # Write filtered logs to file
    $filteredLogs | Out-File -FilePath $logFile -Encoding UTF8
    Write-Host "Filtered logs saved to $logFile"
}

Write-Host "Log extraction complete. Check the $logDir directory."
exit 0
