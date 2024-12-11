from core.config import Config
from app.roast_request import RoastRequest
from flask import Flask, render_template, request, send_from_directory, Response


app = Flask(__name__)
index = r'/index.html'


@app.route('/')
def home() -> render_template:
    return render_template(index)

@app.route('/chat', methods=['POST'])
def chat() -> str:

    roast_agent = RoastRequest()
    user_input = request.form.get('user_input')

    if not user_input:
        return render_template(index, response="Please enter something to roast.")

    try:
        reply = roast_agent.send_roast_request(user_input=user_input)
        return render_template(index, response=reply)

    except Exception as e:
        return render_template(index, response=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.APP_PORT, debug=Config.DEBUG)
