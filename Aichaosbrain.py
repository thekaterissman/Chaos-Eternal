import random
import json  # For saving "memories"
from effects_renderer import EffectsRenderer
from ai_body import AIBody
from environment import Environment

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die', 'ground_quake']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs
        self.renderer = EffectsRenderer()
        self.body = AIBody(self.renderer)
        self.environment = Environment()

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                self.renderer.dance_or_die()
            elif twist == 'sandstorm':
                self.renderer.sandstorm()
            elif twist == 'ground_quake':
                self.renderer.ground_quake()
            else:
                self.renderer.floating_islands()
        else:
            # Not dodging? Maybe the AI gets curious and appears.
            if random.random() < 0.5:
                self.body.manifest()
            self.renderer.basic_roar()

        # After any twist, the body might disappear
        if self.body.is_manifested and random.random() < 0.5:
            self.body.disappear()

    def save_memory(self):
        memory = {'moves': self.player_moves}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos

# Usage:
if __name__ == '__main__':
    brain = AIChaosBrain()
    brain.load_memory()
    # Simulate some player moves
    brain.learn_move('dodge')
    brain.learn_move('dodge')
    brain.learn_move('dodge')
    brain.throw_twist()
