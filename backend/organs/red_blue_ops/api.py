from .red_team import RedTeamOrgan
from .blue_team import BlueTeamOrgan

class RedBlueOps:
    def __init__(self):
        self.red = RedTeamOrgan()
        self.blue = BlueTeamOrgan()

    def run(self, signal: dict):
        mode = signal.get("mode", "red")
        if mode == "blue":
            return self.blue.run(signal)
        return self.red.run(signal)
