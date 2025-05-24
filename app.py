from flask import Flask, jsonify
from flask_cors import CORS  # Essential!

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

class CosmicState:
    def __init__(self):
        self.gnosis = 0.0
        self.pleroma = 0.0
        self.aeons = ["Sophia", "Demiurge", "Lilith", "Adam"]

    def advance(self):
        self.gnosis += 1.0
        self.pleroma = self.gnosis / (1 + self.gnosis)

cosmos = CosmicState()

# 🔥 Critical POST route declaration
@app.route('/advance', methods=['POST'])  
def advance_cosmos():
    cosmos.advance()
    return jsonify({
        "gnosis": cosmos.gnosis,
        "pleroma": cosmos.pleroma,
        "aeons": cosmos.aeons
    })

if __name__ == '__main__':
    app.run()
