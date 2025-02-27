import os
import subprocess
from openai import OpenAI
from dataclasses import dataclass
from app.core.config import AppConfig
from app.core.executor import Executor


@dataclass
class ContainerAgent(Executor):

    log_dir = "logs"
    client = OpenAI(api_key=AppConfig.OPENAI_API_KEY)

    def send_logs_to_ai_agent(self, file_path) -> str:
        with open(file_path, "r") as f:
            log_content = f.read()

        if not log_content.strip():
            return "No errors found in this log."
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes error logs."},
                {"role": "user", "content": f"Summarize the following error log:\n\n{log_content}"}
            ],
            model="gpt-4o",
            temperature=0.5
        )
        content = response.choices[0].message.content
        return content

    def summarize_logs(self) -> None:
        """
        :TODO:
            ai-report folder and file
        """
        for log_file in os.listdir(self.log_dir):
            log_path = os.path.join(self.log_dir, log_file)

            if os.path.isfile(log_path):
                print(f"Summarizing log: {log_file}")
                summary = self.send_logs_to_ai_agent(log_path)
                print(f"Summary for {log_file}:\n{summary}\n")

                # Write summary to a report file
                report_file = os.path.join(r'ai_report', f"{log_file}_summary.txt")
                with open(report_file, 'w', encoding='utf-8') as file:
                    file.write(summary)
                print(f"Summary written to: {report_file}")

    def execute(self) -> None:

        try:
            self.summarize_logs()
        except subprocess.CalledProcessError as e:
            print("There are no running containers")
            print(e.stderr)
