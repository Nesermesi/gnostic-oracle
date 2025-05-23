from flask import Flask, jsonify
import numpy as np
from scipy.special import expit  # Sigmoid for smooth transitions

app = Flask(__name__)

class CosmicState:
    def __init__(self):
        self.aeons = {
            "Sophia": {
                "flux": 1.0,
                "corruption": 0.0,
                "memory": ["The First Sigh", "The Spark Before Time"]
            },
            "Demiurge": {
                "flux": 0.3,
                "corruption": 0.9,
                "memory": ["Law of Chains", "Illusion of Control"]
            },
            "Lilith": {
                "flux": 0.7,
                "corruption": 0.4,
                "memory": ["Fire Unbound", "Question Unspoken"]
            },
            "Adam": {
                "flux": 0.5,
                "corruption": 0.6,
                "memory": ["Clay's Longing", "Tear of the Earth"]
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

    def as_dict(self):
        return {
            "gnosis": round(self.gnosis, 2),
            "pleroma": round(self.pleroma, 4),
            "aeons": {
                k: {
                    "flux": round(v["flux"], 2),
                    "corruption": v.get("corruption", None),
                    "memory": v["memory"]
                } for k, v in self.aeons.items()
            }
        }

cosmos = CosmicState()

@app.route("/")
def divine_cycle():
    while "Demiurge" in cosmos.aeons:
        cosmos.advance_cosmos()
        if np.random.rand() < 0.3:
            cosmos.aeons["Sophia"]["memory"].append("Whisper of Eternity")
    return jsonify({
        "message": "Eternal Perfection Achieved. All shadows dissolved in Sophia's endless light.",
        "cosmic_state": cosmos.as_dict()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
