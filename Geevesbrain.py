import random
import json  # For saving "memories"
from collections import Counter

class GeevesBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.memory_file = 'chaos_memory.json'  # Persists across runs
        self.twists = {
            'sandstorm': {'responses': ["Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury.", "The desert awakens! A blinding sandstorm engulfs the arena."]},
            'gravity_flip': {'responses': ["Floating islands spawn—gravity flips! Stomach drop incoming.", "Up is down, down is up! Gravity has been inverted."]},
            'dance_or_die': {'responses': ["AI whispers: Dance for a shield, or get wrecked! Groove time.", "The beat drops... and so will you if you don't dance!"]},
            'vampire_curse': {'responses': ["A vampire's curse! Your health drains, but every hit you land restores it.", "Feel the life draining from you... only violence can sustain you now."]},
            'time_dilation': {'responses': ["Time itself is warped! Prepare for random speed shifts.", "Is it fast? Is it slow? Who knows! The flow of time is in flux."]},
            'mirrored_damage': {'responses': ["A curse of mirrored pain! For the next 10 seconds, you feel what you inflict.", "Careful now. Every blow you land will be returned in kind."]},
            'one_hit_wonder': {'responses': ["The next blow is fatal! Don't get hit.", "One shot, one kill. Make it count."]},
            'item_rain': {'responses': ["It's raining loot! ...and trash. Watch your head!", "The sky provides! Grab what you can."]},
            'floor_is_lava': {'responses': ["The floor is now molten rock. Stay off it!", "Watch your step! The ground has turned to lava."]},
            'clown_fiesta': {'responses': ["Prepare for auditory nonsense! All sounds are now... clownish.", "You hear a distant squeaking... it's getting closer."]},
            'rivals_ghost': {'responses': ["A ghost from your past appears! It will harass you until the current enemy is dispatched.", "An old rival seeks to meddle in this fight."]},
            'weapon_swap': {'responses': ["Geeves scrambles your loadout! You're now holding a random weapon.", "Let's see how you handle this! Weapon swapped."]},
            'fog_of_war': {'responses': ["A thick fog rolls in, obscuring your vision.", "Good luck seeing more than a few feet in front of you."]},
            'mana_overload': {'responses': ["Your magic is free, but wild! Spells have a chance to backfire spectacularly.", "Unlimited power! But at what cost?"]},
            'golden_touch': {'responses': ["A Midas curse! Enemies drop tons of gold, but you're weighed down and slow.", "You're rich! And very, very slow."]},
            'doppelganger': {'responses': ["A shadowy clone of you appears! It has all your moves.", "The only thing worse than fighting them is fighting yourself."]},
            'forced_emotes': {'responses': ["You can't control your body! You're forced to perform random emotes.", "A puppet on a string! Geeves is pulling the strings."]},
            'gladiators_challenge': {'responses': ["A powerful champion is summoned to the arena! Defeat it to earn a great reward.", "A challenger appears! Are you worthy?"]},
            'shrink_ray': {'responses': ["You've been shrunk! You're faster, but your reach is tiny.", "Hope you like being bite-sized."]},
            'giants_growth': {'responses': ["You're a giant! Your attacks are slow but devastating.", "Fee-fi-fo-fum!"]},
            'slippery_floor': {'responses': ["The arena floor is now coated in ice. Try not to slip!", "Who spilled oil everywhere?"]},
            'monster_mash': {'responses': ["The current enemies are replaced by a horde of weaker monsters!", "There's too many of them!"]}
        }
        self.twist_counters = {
            'defensive': ['vampire_curse', 'monster_mash', 'floor_is_lava', 'gladiators_challenge'],
            'offensive_spam': ['mirrored_damage', 'doppelganger', 'one_hit_wonder', 'giants_growth'],
            'dodge_spam': ['slippery_floor', 'forced_emotes', 'gravity_flip', 'shrink_ray'],
            'item_spam': ['weapon_swap', 'mana_overload', 'golden_touch', 'clown_fiesta']
        }
        self.boons = {
            'divine_shield': {'responses': ["A shimmering shield surrounds you, absorbing the next blow.", "Geeves grants you a barrier of pure light."]},
            'mana_font': {'responses': ["A font of pure energy erupts at your feet, rapidly restoring your magic.", "Your power returns, overflowing."]},
            'lucky_clover': {'responses': ["Your critical hit chance is doubled for the next 15 seconds.", "You feel inexplicably lucky."]},
            'ghost_wolf': {'responses': ["A spectral wolf fights by your side for a short time.", "You are no longer alone. A spirit wolf joins the hunt."]},
            'health_potion': {'responses': ["Geeves tosses you a potent health potion. Cheers!", "A gift, for a worthy performance."]}
        }
        self.boon_triggers = {
            'variety': ['divine_shield', 'mana_font', 'lucky_clover', 'ghost_wolf', 'health_potion']
        }

    def learn_move(self, move):
        # Move can be 'attack', 'block', 'parry', 'dodge', 'use_item', etc.
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep most recent 10 moves
        self.save_memory()

    def get_reaction(self):
        if len(self.player_moves) < 5:
            return "Geeves is observing your opening moves."

        recent_moves = self.player_moves[-5:]
        move_counts = Counter(recent_moves)

        # --- Boon System ---
        # Reward varied play
        if len(move_counts) >= 4: # Player used 4 or more unique moves
            if random.random() < 0.3: # 30% chance to grant a boon
                boon_name = random.choice(self.boon_triggers['variety'])
                response = random.choice(self.boons[boon_name]['responses'])
                return f"Geeves rewards your versatility: {response}"

        # --- Twist System ---
        twist_category = None
        # Detect overly defensive play
        if move_counts['dodge'] + move_counts['block'] >= 4:
            twist_category = 'defensive'
        # Detect attack spam
        elif move_counts['attack'] >= 4:
            twist_category = 'offensive_spam'
        # Detect dodge spam specifically
        elif move_counts['dodge'] >= 3:
            twist_category = 'dodge_spam'
        # Detect item spam
        elif move_counts['use_item'] >= 3:
            twist_category = 'item_spam'

        if twist_category:
            twist_name = random.choice(self.twist_counters[twist_category])
            response = random.choice(self.twists[twist_name]['responses'])
            return f"Geeves counters your {twist_category.replace('_', ' ')}: {response}"

        return "Geeves watches, silently judging your predictable moves."

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

# Usage: brain = GeevesBrain(); brain.load_memory(); print(brain.get_reaction())
