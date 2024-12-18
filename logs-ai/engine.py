import os
import openai

# Configure OpenAI API key
openai.api_key = "your_openai_api_key"

# Directory containing logs
log_dir = "./container_logs"

# Function to summarize a log file
def summarize_log(file_path):
    with open(file_path, "r") as f:
        log_content = f.read()

    if not log_content.strip():
        return "No errors found in this log."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes error logs."},
            {"role": "user", "content": f"Summarize the following error log:\n\n{log_content}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Process each log file
for log_file in os.listdir(log_dir):
    log_path = os.path.join(log_dir, log_file)
    if os.path.isfile(log_path):
        print(f"Summarizing log: {log_file}")
        summary = summarize_log(log_path)
        print(f"Summary for {log_file}:\n{summary}\n")
