import random

class AIChaosBrain:
    """
    Simulates an AI that adapts to player actions and introduces chaotic events.
    This class is now stateless and operates on the memory provided to it.
    """
    def __init__(self, player_moves):
        """
        Initializes the AI brain with a given player's move history.
        """
        self.player_moves = player_moves
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']

    def learn_move(self, move):
        """
        Records a player's move to the current session's memory.
        """
        self.player_moves.append(move)
        # Keep only the 10 most recent moves to stay adaptive.
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]

    def throw_twist(self):
        """
        Triggers a chaotic event based on the player's recent moves.
        """
        if 'dodge' in self.player_moves[-3:]:
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            return "AI adapts: Basic roar from Leo. Feel it rumble."