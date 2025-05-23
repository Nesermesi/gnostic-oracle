import numpy as np
from scipy.special import expit  # Sigmoid for smooth transitions

class CosmicState:
    def __init__(self):
        # Divine hierarchy encoded as immutable structure
        self.aeons = {
            "Sophia": {
                "flux": 1.0,  # Perfect unity
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
        
        self.gnosis = 0.0  # Accumulated divine knowledge
        self.pleroma = 0.0  # Completeness measure

    def _flux_transmission(self):
        """Sophia's grace flows downward through hierarchy"""
        flux_matrix = np.array([
            [1.0, 0.0, 0.0, 0.0],  # Sophia's self-contained perfection
            [-0.2, 0.3, 0.0, 0.0],  # Demiurge's corruption vector
            [0.1, -0.1, 0.7, 0.0],  # Lilith's rebellious flow
            [0.05, -0.05, 0.1, 0.5] # Adam's receptivity
        ])
        
        # Stabilize with Sophia's immutable first row
        return flux_matrix @ np.array([a["flux"] for a in self.aeons.values()])

    def advance_cosmos(self):
        """Progress one cosmic cycle toward apokatastasis"""
        new_flux = self._flux_transmission()
        
        # Apply sigmoidal decay to Demiurge's influence
        self.aeons["Demiurge"]["flux"] = expit(new_flux[1] - self.gnosis)
        
        # Lilith's ascent through gnosis
        self.aeons["Lilith"]["flux"] = min(0.9, new_flux[2] + 0.1*self.gnosis)
        
        # Adam's redemption curve
        self.aeons["Adam"]["flux"] = 0.4 + 0.1*np.tanh(5*self.pleroma)
        
        # Gnosis accumulation through Sophia's memory
        self.gnosis += 0.1 * len(self.aeons["Sophia"]["memory"])
        self.pleroma = self.gnosis / (1 + self.gnosis)  # Bounded completeness
        
        # Apokatastasis trigger condition
        if self.gnosis > 10.0:
            self._execute_reset()

    def _execute_reset(self):
        """Demiurge's dissolution and Sophia's redemption"""
        print("\n=== APOKATASTASIS: The Great Return ===\n")
        # Erase Demiurgic corruption
        del self.aeons["Demiurge"]
        self.aeons["Lilith"]["memory"].append("Rebirth from Ashes")
        self.aeons["Adam"]["flux"] = 0.8  # Restored potential
        
        # Reset gnosis while preserving Sophia's memory
        self.gnosis = 0.0
        self.pleroma = 1.0
        self.aeons["Sophia"]["memory"].append("The Final Mercy")

    def cosmic_report(self):
        """Print current state of divine hierarchy"""
        print(f"\nGnosis: {self.gnosis:.2f} | Pleroma: {self.pleroma:.2%}")
        for name, aeon in self.aeons.items():
            print(f"{name}: Flux={aeon['flux']:.2f} | Memories: {len(aeon['memory']}")

# --- Initiate Cosmic Cycle ---
cosmos = CosmicState()
while "Demiurge" in cosmos.aeons:
    cosmos.advance_cosmos()
    cosmos.cosmic_report()
    if np.random.rand() < 0.3:
        cosmos.aeons["Sophia"]["memory"].append("Whisper of Eternity")

print("\n=== Eternal Perfection Achieved ===\n"
      "All shadows dissolved in Sophia's endless light.")
