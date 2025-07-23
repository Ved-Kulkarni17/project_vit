class ThreatModel:
    def __init__(self):
        print("[Model] ThreatModel initialized.")

    def predict(self, data):
        return {"prediction": "threat", "input": data}
