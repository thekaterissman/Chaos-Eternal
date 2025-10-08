import random
import json

class AIChaosBrain:
    """
    Simulates an AI that adapts to player actions and introduces chaotic events.
    This class is designed to create surprising and dynamic gameplay moments
    based on the player's recent behavior.
    """
    def __init__(self):
        """
        Initializes the AI brain.
        - player_moves: A list to store the player's recent actions.
        - fears: A list of potential "twist" events the AI can trigger.
        - memory_file: The file where the AI's "memory" of player moves is stored.
        - chaos_level: A dynamic measure of game intensity.
        - event_history: A log of past twists to avoid repetition.
        """
        self.player_moves = []
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die', 'meteor_shower', 'gravity_inversion']
        self.memory_file = 'chaos_memory.json'
        self.chaos_level = 1
        self.event_history = []

    def learn_move(self, move):
        """
        Records a player's move, adjusts chaos, and saves it to memory.
        Aggressive moves increase the chaos level, while passive ones decrease it.
        """
        self.player_moves.append(move)
        if move in ['fight', 'raid', 'attack']:
            self.chaos_level += 1
        elif move in ['dodge', 'reflect', 'create']:
            self.chaos_level = max(1, self.chaos_level - 1)

        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]
        self.save_memory()

    def throw_twist(self):
        """
        Triggers a chaotic event based on player moves and chaos level.
        Higher chaos levels unlock more intense and unpredictable twists.
        The AI avoids repeating the same twist immediately.
        """
        # Filter out the last event to ensure variety
        available_fears = [fear for fear in self.fears if fear not in self.event_history[-1:]]

        # More intense twists are unlocked at higher chaos levels
        if self.chaos_level >= 5:
            twist = random.choice(available_fears)
            self.event_history.append(twist)
            if twist == 'meteor_shower':
                return "A meteor shower rains down! Haptic impacts rattle your teeth."
            elif twist == 'gravity_inversion':
                return "Gravity inverts! The world flips, and your stomach lurches."

        # Standard twists for mid-level chaos
        if 'dodge' in self.player_moves[-3:]:
            twist = random.choice(available_fears)
            self.event_history.append(twist)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            return "AI adapts: Basic roar from Leo. Feel it rumble."

    def save_memory(self):
        """
        Saves player moves and chaos level to a JSON file for persistence.
        """
        memory = {'moves': self.player_moves, 'chaos_level': self.chaos_level, 'event_history': self.event_history}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        """
        Loads player data from the JSON file, including moves, chaos level, and history.
        """
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
                self.chaos_level = memory.get('chaos_level', 1)
                self.event_history = memory.get('event_history', [])
        except FileNotFoundError:
            pass

# Usage: brain = AIChaosBrain(); brain.load_memory(); print(brain.throw_twist())
