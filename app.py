from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Optional: a simple class structure (correctly indented)
class GnosticOracle:
    def __init__(self):
        self.state = "initial"

    def next_step(self, user_input):
        # Insert your actual logic here
        return {
            "gnosis": "Unveiling",
            "pleroma": 91,
            "aeons": {
                "Sophia": {"flux": "dancing", "memories": "hidden"},
                "Logos": {"flux": "burning", "memories": "clear"}
            }
        }

oracle = GnosticOracle()

@app.route('/advance', methods=['POST'])
def advance():
    data = request.get_json()
    response = oracle.next_step(data.get("input", ""))
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
