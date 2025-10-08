import random

class ModesManager:
    """
    Manages game modes, including mixing them to create unique synergies.
    This class tracks player progression and allows for dynamic, interconnected
    gameplay experiences.
    """
    def __init__(self):
        """
        Initializes the Modes Manager.
        - active_modes: A set of currently active game modes.
        - xp: The player's persistent experience points.
        - shelters: A list of player-built structures in survival mode.
        - mode_synergies: A dictionary defining the outcomes of mixing modes.
        """
        self.active_modes = {'hunter'}
        self.xp = 0
        self.shelters = []
        self.mode_synergies = {
            ('hunter', 'raid'): "Hunter's Raid: Track and steal from opponents with enhanced stealth.",
            ('survival', 'pvp'): "Survival PvP: Craft weapons on the fly in a fight to the death.",
            ('therapy', 'hunter'): "Mindful Hunter: Pacify beasts instead of killing them for unique rewards."
        }

    def switch_mode(self, mode):
        """
        Switches the game to a new mode, clearing previous modes.
        Provides a descriptive message for the selected mode.
        """
        self.active_modes = {mode}
        if mode == 'survival':
            return "Survival Mode: Craft vines to blades. XP sticks – no resets!"
        elif mode == 'pvp':
            return "PvP: Teams self-select. Mix crews, clash in the arena!"
        else:
            return "Hunter Mode: Self-pick teams. Hunt or be hunted."

    def mix_modes(self, mode1, mode2):
        """
        Mixes two modes to create a unique, synergistic experience.
        The outcome is determined by predefined synergies.
        """
        self.active_modes = {mode1, mode2}
        synergy_key = tuple(sorted((mode1, mode2)))
        if synergy_key in self.mode_synergies:
            return self.mode_synergies[synergy_key]
        return f"Mixed: {mode1} + {mode2} = Pure chaos! The world remakes itself in 5s."

    def earn_xp(self, action):
        """
        Awards XP for actions, with bonuses for synergistic play.
        If active modes have a synergy, the player earns bonus XP.
        """
        xp_gain = random.randint(10, 50)
        synergy_bonus = 0

        synergy_key = tuple(sorted(self.active_modes))
        if len(self.active_modes) > 1 and synergy_key in self.mode_synergies:
            synergy_bonus = 25  # Bonus for playing in a mixed-mode state
            xp_gain += synergy_bonus

        self.xp += xp_gain
        if 'survival' in self.active_modes:
            self.shelters.append('new_shelter')

        if synergy_bonus > 0:
            return f"Synergy Bonus! XP +{xp_gain}! Total: {self.xp}."
        return f"XP +{xp_gain - synergy_bonus}! Total: {self.xp}. Boosts Coliseum skills."

# Usage: manager = ModesManager(); print(manager.switch_mode('survival')); print(manager.earn_xp('raid'))
