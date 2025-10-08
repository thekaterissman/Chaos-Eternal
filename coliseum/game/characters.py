# characters.py - Defines the playable characters and their unique traits.

class Kate:
    """
    Represents Kate, one of the three Chaos Queens.
    Her abilities are focused on raw power and direct impact.
    """
    def __init__(self):
        self.name = "Kate"
        self.trait = "Fiery and Unstoppable"

    def special_ability(self):
        """
        Kate's special ability: summons a powerful, fiery beast.
        """
        return "Kate's scepter glows! A Phoenix of pure plasma erupts, its cry a searing blast of heat and courage."

class Amya:
    """
    Represents Amya, one of the three Chaos Queens.
    Her abilities are focused on control and strategic advantage.
    """
    def __init__(self):
        self.name = "Amya"
        self.trait = "Calm and Strategic"

    def special_ability(self):
        """
        Amya's special ability: manipulates the arena itself.
        """
        return "Amya raises her hand! The very ground shifts, creating barriers and pathways. The arena is her chessboard."

class Holly:
    """
    Represents Holly, one of the three Chaos Queens.
    Her abilities are focused on support and chaotic fun.
    """
    def __init__(self):
        self.name = "Holly"
        self.trait = "Joyful and Unpredictable"

    def special_ability(self):
        """
        Holly's special ability: introduces a fun, random element to the fight.
        """
        return "Holly laughs, and the world glitters! It starts raining jellybeans, making the ground sticky and hilarious."
