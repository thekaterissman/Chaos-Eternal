import random
import json  # For saving "memories"

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
        """
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
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
        Triggers a chaotic event based on the player's recent moves.
        If the player is defensive ('dodge'), the AI introduces a major environmental shift.
        Otherwise, it provides a more standard challenge.
        """
        # If the player has dodged in their last 3 moves, trigger a "fear".
        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
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

    def generate_photorealistic_prompt(self):
        """
        Generates a detailed, photorealistic image prompt using a template.
        """
        shot_types = ["close-up", "medium shot", "wide shot", "dutch angle", "low-angle shot"]
        subjects = ["Kate the Fiery Queen", "Amya the Strategic Queen", "Holly the Joyful Queen", "a Leo lion", "a Scorpio sentinel", "a Taurus bull", "a celestial phoenix", "a knight on a cosmic dragon"]
        actions = ["casting a powerful spell", "in a moment of quiet reflection", "laughing maniacally", "roaring with cosmic energy", "charging with furious intent", "unfurling wings of pure plasma", "surveying the chaotic arena"]
        environments = ["an arena of floating islands", "a neon-drenched jungle", "a crystalline ice cave", "a raging volcanic caldera", "a village under a sky of two suns", "the heart of a swirling sandstorm"]
        lighting = ["dramatic, moody backlighting", "a soft, ethereal glow", "harsh, direct sunlight", "the shimmering light of a nearby nebula", "flickering torchlight", "ominous, pulsing red light"]
        moods = ["epic and awe-inspiring", "serene and contemplative", "chaotic and unpredictable", "dark and mysterious", "triumphant and glorious"]
        cameras = ["a Canon EOS R5 with a 50mm f/1.2L lens", "a Sony A7R IV with a 24-70mm G Master lens", "a Hasselblad X1D II 50C with a 90mm f/3.2 lens", "a large-format film camera"]
        textures = ["the cracked leather of her armor", "the smooth, polished surface of a magical gem", "the intricate, glowing filigree on a scepter", "the rough, textured hide of a great beast", "the shimmering, iridescent scales of a dragon"]
        aspect_ratios = ["16:9 widescreen", "1:1 square", "4:3 classic", "21:9 cinematic"]

        prompt = f"A photorealistic {random.choice(shot_types)} of {random.choice(subjects)}, {random.choice(actions)}, set in {random.choice(environments)}. The scene is illuminated by {random.choice(lighting)}, creating a {random.choice(moods)} atmosphere. Captured with {random.choice(cameras)}, emphasizing {random.choice(textures)}. The image should be in a {random.choice(aspect_ratios)} format."
        return prompt

# Usage:
if __name__ == '__main__':
    brain = AIChaosBrain()
    brain.load_memory()
    print("--- AI Twist ---")
    print(brain.throw_twist())
    print("\n--- Photorealistic Prompt ---")
    print(brain.generate_photorealistic_prompt())
