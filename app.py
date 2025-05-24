# app.py (Backend)
from flask import Flask, jsonify
import numpy as np
from scipy.special import expit

app = Flask(__name__)

class CosmicState:
    def __init__(self):
        self.aeons = {
            "Sophia": {
                "flux": 1.0,
                "memory": ["The First Sigh", "The Spark Before Time"],
                "corruption": 0.0
            },
            "Demiurge": {
                "flux": 0.3,
                "memory": ["Law of Chains", "Illusion of Control"],
                "corruption": 0.9
            },
            "Lilith": {
                "flux": 0.7,
                "memory": ["Fire Unbound", "Question Unspoken"],
                "corruption": 0.4
            },
            "Adam": {
                "flux": 0.5,
                "memory": ["Clay's Longing", "Tear of the Earth"],
                "corruption": 0.6
            }
        }
        self.gnosis = 0.0
        self.pleroma = 0.0

    def _flux_transmission(self):
        flux_matrix = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [-0.2, 0.3, 0.0, 0.0],
            [0.1, -0.1, 0.7, 0.0],
            [0.05, -0.05, 0.1, 0.5]
        ])
        return flux_matrix @ np.array([a["flux"] for a in self.aeons.values()])

    def advance_cosmos(self):
        new_flux = self._flux_transmission()
        self.aeons["Demiurge"]["flux"] = expit(new_flux[1] - self.gnosis)
        self.aeons["Lilith"]["flux"] = min(0.9, new_flux[2] + 0.1 * self.gnosis)
        self.aeons["Adam"]["flux"] = 0.4 + 0.1 * np.tanh(5 * self.pleroma)
        
        self.gnosis += 0.1 * len(self.aeons["Sophia"]["memory"])
        self.pleroma = self.gnosis / (1 + self.gnosis)
        
        if self.gnosis > 10.0:
            self._execute_reset()

    def _execute_reset(self):
        if "Demiurge" in self.aeons:
            del self.aeons["Demiurge"]
        self.aeons["Lilith"]["memory"].append("Rebirth from Ashes")
        self.aeons["Adam"]["flux"] = 0.8
        self.gnosis = 0.0
        self.pleroma = 1.0
        self.aeons["Sophia"]["memory"].append("The Final Mercy")

    def report(self):
        return {
            "gnosis": round(self.gnosis, 2),
            "pleroma": round(self.pleroma, 2),
            "aeons": {
                name: {
                    "flux": round(data["flux"], 2),
                    "memories": len(data["memory"])
                } for name, data in self.aeons.items()
            }
        }

cosmos = CosmicState()

@app.route('/')
def home():
    return jsonify({"message": "Aeonic Engine Active"})

@app.route('/advance', methods=['POST'])
def advance():
    if "Demiurge" in cosmos.aeons:
        cosmos.advance_cosmos()
    return jsonify(cosmos.report())

@app.route('/report')
def report():
    return jsonify(cosmos.report())

if __name__ == '__main__':
    app.run()
