import random
import json  # For saving "memories"

class AIChaosBrain:
    """
    Simulates an AI that adapts to player actions and introduces chaotic events.
    This class is designed to create surprising and dynamic gameplay moments
    based on the player's recent behavior.
    """
    def __init__(self, modes_manager):
        """
        Initializes the AI brain.
        - modes_manager: An instance of ModesManager to access difficulty settings.
        - player_moves: A list to store the player's recent actions.
        - fears: A list of potential "twist" events the AI can trigger.
        - memory_file: The file where the AI's "memory" of player moves is stored.
        """
        self.modes_manager = modes_manager
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die', 'wind', 'rain', 'temperature_hot', 'temperature_cold']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs

    def learn_move(self, move):
        """
        Records a player's move and saves it to memory.
        This allows the AI to "learn" from the player's actions.
        """
        self.player_moves.append(move)
        # Keep only the 10 most recent moves to stay adaptive.
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        """
        Triggers a chaotic event based on the player's recent moves and difficulty.
        If the player is defensive ('dodge'), the AI introduces a major environmental shift.
        Otherwise, it provides a more standard challenge.
        """
        difficulty = self.modes_manager.difficulty
        twist_sensitivity = 3  # Default for medium

        if difficulty == 'easy':
            twist_sensitivity = 2
        elif difficulty == 'hard':
            twist_sensitivity = 4

        # If the player has dodged in their last `twist_sensitivity` moves, trigger a "fear".
        if len(self.player_moves) >= twist_sensitivity and 'dodge' in self.player_moves[-twist_sensitivity:]:
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            elif twist == 'wind':
                return "Howling winds whip through the arena! Haptics: Buffeting gusts. Brace yourself."
            elif twist == 'rain':
                return "A downpour begins! Haptics: Cold rain on your skin. The ground is getting slick."
            elif twist == 'temperature_hot':
                return "A wave of heat washes over you! Haptics: Feel the furnace blast."
            elif twist == 'temperature_cold':
                return "A bitter cold seeps into your suit! Haptics: Frost crawling on your skin."
            else:
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            # Standard AI response for less defensive players.
            return "AI adapts: Basic roar from Leo. Feel it rumble."

    def save_memory(self):
        """
        Saves the player's move history to a JSON file for persistence.
        This allows the AI to remember player behavior across game sessions.
        """
        memory = {'moves': self.player_moves}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        """
        Loads the player's move history from the JSON file.
        This enables the AI to recall past interactions at the start of a new session.
        """
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos, no memory file found.

# Usage: brain = AIChaosBrain(); brain.load_memory(); print(brain.throw_twist())
