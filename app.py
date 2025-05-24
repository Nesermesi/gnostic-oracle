from flask import Flask, request, jsonif

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Gnostic Oracle backend is running."

@app.route('/advance', methods=['POST'])  # This line explicitly allows POST
def advance():
    data = request.get_json()
    user_input = data.get('message', '')

    # You can put your logic here
    reply = f"You said: {user_input}. The Oracle hears you."

    return jsonify({'response': reply})
