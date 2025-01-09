from app.bot.ai import AIAgent
from flask import Flask, render_template, request, jsonify

from app.core.config import PortConfig, AppConfig

app = Flask(__name__)
index = r'/index.html'


@app.route('/')
def home() -> render_template:
    return render_template(index)


@app.route('/health', methods=['GET'])
def health() -> jsonify:
    return jsonify({"message": "Service is healthy"}), 200


@app.route('/chat', methods=['POST'])
def chat() -> str:

    roast_agent = AIAgent()
    user_input = request.form.get('user_input')

    if not user_input:
        return render_template(index, response="Please enter something to roast.")

    try:
        reply = roast_agent.get_ai_response(user_input=user_input)
        return render_template(index, response=reply)

    except Exception as e:
        return render_template(index, response=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(host=AppConfig.HOST, port=PortConfig.APP_PORT, debug=AppConfig.DEBUG)
