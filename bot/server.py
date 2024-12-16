from core.config import AppConfig, PortConfig
from bot.ai import RoastAgent
from flask import Flask, request, jsonify


roast_agent = RoastAgent()
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
        # Get user input from the POST request
        data = request.get_json()
        if 'input' not in data:
            return jsonify({"error": "Invalid input. 'input' field is required."}), 400

        user_input = data['input']
        roast_response = roast_agent.roast_me(user_input)

        return jsonify({"roast": roast_response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host=AppConfig.HOST, port=PortConfig.AI_PORT, debug=AppConfig.DEBUG)
