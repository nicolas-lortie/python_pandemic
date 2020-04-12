
class Player:
    def __init__(self, role):
        """
        Represents a player, it's role, position and hand
        :param role (int):
            0: Operations expert
            1: Medic
            2: Researcher
            3: Scientist
        """
        self.role = role
        self.position = "Atlanta" #Starting position for all players
        self.hand = []