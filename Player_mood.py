# Player_mood.py - Manages the player's emotional state to influence game events.

class PlayerMood:
    """
    Tracks and manages the player's emotional state based on in-game actions.
    The mood is used by other systems, like the VisualsEngine, to create a more
    dynamic and responsive experience.
    """
    def __init__(self):
        """
        Initializes the player's mood.
        - mood: The current emotional state ('calm', 'excited', 'tense').
        """
        self.mood = 'calm'
        print("Player mood initialized to: calm")

    def update_mood(self, action):
        """
        Updates the player's mood based on the last action they took.

        Args:
            action (str): The player's last action (e.g., 'fight', 'fail', 'use ability').
        """
        if action in ['fight', 'use ability', 'ride beast']:
            self.mood = 'excited'
        elif action == 'fail':
            self.mood = 'tense'
        elif action in ['reflect', 'create']:
            self.mood = 'calm'
        # Other actions don't change the mood significantly.

        print(f"Player mood updated to: {self.mood}")

    def get_mood(self):
        """
        Returns the current mood.

        Returns:
            str: The player's current mood.
        """
        return self.mood