from app.config import Config
from flask import Flask, render_template, jsonify


app = Flask(__name__)
index = r'/index.html'


@app.route('/')
def home() -> render_template:
    return render_template(index)


@app.route('/health', methods=['GET'])
def health() -> jsonify:
    return jsonify({"message": "Service is healthy"}), 200


if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.APP_PORT, debug=Config.DEBUG)
