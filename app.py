from flask import Flask, render_template, redirect, url_for
import numpy as np
from scipy.special import expit
import random

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
        if "Demiurge" in self.aeons:
            self.aeons["Demiurge"]["flux"] = expit(new_flux[1] - self.gnosis)
        if "Lilith" in self.aeons:
            self.aeons["Lilith"]["flux"] = min(0.9, new_flux[2] + 0.1 * self.gnosis)
        if "Adam" in self.aeons:
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

    def cosmic_report(self):
        report = {
            "gnosis": round(self.gnosis, 2),
            "pleroma_percent": round(self.pleroma * 100, 2),
            "aeons": []
        }
        for name, aeon in self.aeons.items():
            report["aeons"].append({
                "name": name,
                "flux": round(aeon["flux"], 2),
                "memories_count": len(aeon["memory"]),
                "memories": aeon["memory"]
            })
        return report

cosmos = CosmicState()

@app.route("/", methods=["GET"])
def index():
    report = cosmos.cosmic_report()
    return render_template("cosmic_state.html", report=report)

@app.route("/advance", methods=["POST"])
def advance():
    cosmos.advance_cosmos()
    if random.random() < 0.3:
        cosmos.aeons["Sophia"]["memory"].append("Whisper of Eternity")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
