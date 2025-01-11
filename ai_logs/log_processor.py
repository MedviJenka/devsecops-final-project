import requests
from flask import Flask, request, jsonify


app = Flask(__name__)

# AI Engine Endpoint
AI_ENGINE_URL = "http://ai-engine:8000/summarize"


@app.route("/process_logs", methods=["POST"])
def process_logs():
    try:
        logs = request.json.get("logs", [])
        if not logs:
            return jsonify({"error": "No logs provided"}), 400

        # Send logs to AI Engine for summarization
        response = requests.post(AI_ENGINE_URL, json={"logs": logs})
        if response.status_code != 200:
            return jsonify({"error": "Failed to summarize logs"}), 500

        summary = response.json().get("summary")
        return jsonify({"summary": summary}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
