from flask import Flask, jsonify
from flask_cors import CORS  # Essential for web communication
import numpy as np
from scipy.special import expit

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

class CosmicState:
    # ... [keep existing class code unchanged] ...

@app.route('/advance', methods=['POST'])  # Explicit POST declaration
def advance():
    if "Demiurge" in cosmos.aeons:
        cosmos.advance_cosmos()
    return jsonify(cosmos.report())

# ... [rest of routes] ...

if __name__ == '__main__':
    app.run()
