from ai.fun import RoastAgent
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    roast_agent = RoastAgent()
    user_input = request.form.get('user_input')
    if not user_input:
        return render_template('index.html', response="Please enter something to roast.")

    try:
        reply = roast_agent.roast_me(user_input=user_input)
        return render_template('index.html', response=reply)

    except Exception as e:
        return render_template('index.html', response=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
