from core.config import AppConfig, PortConfig
from bot.ai import Agent
from flask import Flask, request, jsonify


agent = Agent()
app = Flask(__name__)


@app.route(rule='/')
def landing_page() -> jsonify:
    return jsonify({"message": "server is up"}), 200


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"message": "Service is healthy"}), 200


@app.route(rule='/roast', methods=['POST'])
def main() -> tuple:

    """Endpoint to roast the user."""

    try:
        data = request.get_json()
        if 'input' not in data:
            return jsonify({"error": "Invalid input. 'input' field is required."}), 400

        user_input = data['input']
        response = agent.set_ai(user_input)

        return jsonify({"roast": response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host=AppConfig.HOST, port=PortConfig.AI_PORT, debug=AppConfig.DEBUG)
