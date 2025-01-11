from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/summarize", methods=["POST"])
def summarize_logs():
    try:
        logs = request.json.get("logs", [])
        if not logs:
            return jsonify({"error": "No logs provided"}), 400

        # Summarize logs using OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following logs:\n{logs}",
            max_tokens=100,
        )
        summary = response.choices[0].text.strip()
        return jsonify({"summary": summary}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
