#!/bin/bash

# Directory to store logs
log_dir="./container_logs"
mkdir -p "$log_dir"  # Create the directory if it doesn't exist

# Get all running Docker containers
containers=$(docker ps --format "{{.Names}}")

# Check if there are any running containers
if [ -z "$containers" ]; then
  echo "No running containers found."
  exit 0
fi

# Loop through each container and extract logs
for container in $containers; do
  echo "Fetching logs for container: $container"

  # Extract logs
  log_file="$log_dir/${container}_error.log"
  raw_log_file="$log_dir/${container}.log"
  logs=$(docker logs "$container")

  # Check if logs are retrieved
  if [ -z "$logs" ]; then
    echo "No logs found for container: $container"
    continue
  fi

  # Split logs into lines and count them
  log_lines=$(echo "$logs" | wc -l)

  # Truncate logs to the last 100 lines if more than 1000 lines
  if [ "$log_lines" -gt 1000 ]; then
    logs=$(echo "$logs" | tail -n 100)
    echo "Log truncated to the last 100 lines for container: $container"
  fi

  # Save raw logs
  echo "$logs" > "$raw_log_file"
  echo "Raw logs saved to $raw_log_file"

  # Filter logs for errors (case insensitive)
  filtered_logs=$(echo "$logs" | grep -i "error")

  # Check if filtered logs exist
  if [ -z "$filtered_logs" ]; then
    echo "No errors found for container: $container"
    continue
  fi

  # Save filtered logs
  echo "$filtered_logs" > "$log_file"
  echo "Filtered logs saved to $log_file"
done

echo "Log extraction complete. Check the $log_dir directory."
exit 0
