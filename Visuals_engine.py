# Visuals_engine.py - Generates dynamic visual descriptions based on player mood.

class VisualsEngine:
    """
    Creates descriptive, memorable text that reflects the player's emotional state,
    simulating a "heart-sync" effect on the game's environment.
    """
    def __init__(self, player_mood):
        """
        Initializes the Visuals Engine.

        Args:
            player_mood (PlayerMood): An instance of the PlayerMood class to track mood.
        """
        self.player_mood = player_mood

    def get_visual_description(self):
        """
        Generates a visual description of the world based on the current player mood.

        Returns:
            str: A string containing the descriptive text.
        """
        mood = self.player_mood.get_mood()

        if mood == 'excited':
            return ("VISUALS: The arena pulses with a neon-red light, matching the frantic beat of your heart. "
                    "The roar of the crowd is a physical shockwave, and the very air crackles with energy.")
        elif mood == 'tense':
            return ("VISUALS: The world seems to shrink, the colors draining to a monochrome grey. "
                    "Long, distorted shadows stretch from every corner, and a low, dissonant hum fills the air.")
        elif mood == 'calm':
            return ("VISUALS: A soft, golden light bathes the arena. The sounds of a distant, holographic waterfall "
                    "echo gently, and the air feels still and peaceful. The sand glitters like a field of diamonds.")
        else:
            return "VISUALS: The arena stands vast and silent, waiting for the next moment of chaos or calm."