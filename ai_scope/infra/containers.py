import os
import re
import subprocess


PATH = r'containers/logs/'


def create_log_directory():
    if not os.path.exists(PATH):
        print(f"Creating log directory: {PATH}")
        os.makedirs(PATH)


def get_running_containers():
    try:
        result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"],
                                stdout=subprocess.PIPE, text=True, check=True)
        containers = result.stdout.strip().split("\n")
        return [c for c in containers if c]
    except subprocess.CalledProcessError:
        print("Error fetching running containers.")
        return []


def fetch_logs(container_name):
    try:
        result = subprocess.run(["docker", "logs", container_name],
                                stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        print(f"Error fetching logs for container: {container_name}")
        return ""


def filter_logs_for_errors(log_lines):
    error_pattern = re.compile(r"(?i)error")
    return [line for line in log_lines if error_pattern.search(line)]


def main():

    create_log_directory()

    containers = get_running_containers()
    if not containers:
        print("No running containers found.")
        return

    for container in containers:
        print(f"Fetching logs for container: {container}")

        logs = fetch_logs(container)
        if not logs:
            print(f"No logs found for container: {container}")
            continue

        log_lines = logs.splitlines()

        # Truncate to the last 100 lines if there are more than 1000 lines
        if len(log_lines) > 1000:
            log_lines = log_lines[-100:]
            print(f"Log truncated to the last 100 lines for container: {container}")

        # Save raw logs
        raw_log_file = os.path.join(PATH, f"{container}.log")
        with open(raw_log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(log_lines))
        print(f"Raw logs saved to {raw_log_file}")

        # Filter logs for errors
        filtered_logs = filter_logs_for_errors(log_lines)
        if not filtered_logs:
            print(f"No errors found for container: {container}")
            continue

        # Save filtered logs
        filtered_log_file = os.path.join(PATH, f"{container}_error.log")
        with open(filtered_log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_logs))
        print(f"Filtered logs saved to {filtered_log_file}")

    print(f"Log extraction complete. Check the {PATH} directory.")


if __name__ == "__main__":
    main()
