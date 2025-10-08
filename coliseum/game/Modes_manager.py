import random

class ModesManager:
    """
    Manages the different game modes, player XP, and persistent creations.
    This class allows for dynamic switching between modes and tracks player
    progression that carries across different gameplay experiences.
    """
    def __init__(self):
        """
        Initializes the Modes Manager.
        - current_mode: The active game mode.
        - xp: The player's experience points, which are persistent.
        - shelters: A list representing player-built structures in survival mode.
        """
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds

    def switch_mode(self, mode):
        """
        Switches the game to a new mode.
        Provides a descriptive message for the selected mode.
        """
        modes = ['hunter', 'survival', 'pvp', 'raid', 'therapy']
        if mode in modes:
            self.current_mode = mode
            if mode == 'survival':
                return "Survival Mode: Craft vines to blades. XP sticks – no resets!"
            elif mode == 'pvp':
                return "PvP: Teams self-select. Mix crews, clash in the arena!"
            elif mode == 'raid':
                return "Raid villages! Steal loot, burn down – haptics make walls crack."
            elif mode == 'therapy':
                return "Therapy Mode: A peaceful space. No combat, just creation and reflection."
            else:
                return "Hunter Mode: Self-pick teams. Hunt or be hunted."
        return "Invalid mode – chaos only!"

    def earn_xp(self, action):
        """
        Awards XP to the player for completing an action.
        XP is a core progression mechanic that boosts skills across all modes.
        In survival mode, actions can also result in building persistent structures.
        """
        xp_gain = random.randint(10, 50)
        self.xp += xp_gain
        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')  # Build persists
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        """
        Simulates the mixing of two game modes to create a unique experience.
        This reflects the dynamic, player-driven nature of the game world.
        """
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

# Usage: manager = ModesManager(); print(manager.switch_mode('survival')); print(manager.earn_xp('raid'))
