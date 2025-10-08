import random
import uuid

class BeastEcosystem:
    def __init__(self, coins=0):
        self.coins = coins
        self.beast_templates = {
            'leo_cub': {
                'cost': 1,
                'ability': 'A playful roar that slightly distracts enemies.',
                'xp_to_next_level': 100,
                'evolution': 'leo_lion'
            },
            'leo_lion': {
                'cost': 0, # Cannot be bought directly
                'ability': 'A mighty roar that stuns nearby foes for a short duration.',
                'xp_to_next_level': 500,
                'evolution': 'celestial_lion'
            },
            'celestial_lion': {
                'cost': 0,
                'ability': 'A cosmic roar that damages all enemies in a large radius and grants allies a temporary shield.',
                'xp_to_next_level': 9999, # Max level
                'evolution': None
            },
            'scorpio_hatchling': {
                'cost': 1,
                'ability': 'A weak sting that applies a minor poison effect.',
                'xp_to_next_level': 100,
                'evolution': 'scorpio_sting'
            },
            'scorpio_sting': {
                'cost': 0,
                'ability': 'A venomous sting that deals significant poison damage over time.',
                'xp_to_next_level': 500,
                'evolution': 'astral_scorpion'
            },
            'astral_scorpion': {
                'cost': 0,
                'ability': 'A cosmic sting that instantly halves an enemy\'s health and applies a permanent poison.',
                'xp_to_next_level': 9999,
                'evolution': None
            }
        }
        # owned_beasts will now store unique instances with their own progress
        # Format: { 'unique_id': {'template': 'leo_cub', 'level': 1, 'xp': 0} }
        self.owned_beasts = {}
        # Add a new rare beast for events
        self.beast_templates['phoenix_hatchling'] = {
            'cost': 25,
            'ability': 'A spark of warmth that slightly heals the user.',
            'xp_to_next_level': 200,
            'evolution': 'phoenix_firebird'
        }
        self.beast_templates['phoenix_firebird'] = {
            'cost': 0,
            'ability': 'A wave of fire that damages enemies and heals allies.',
            'xp_to_next_level': 9999,
            'evolution': None
        }

    def get_available_beasts(self, world_event=None):
        """Returns a list of beast names available for purchase based on the current world event."""
        available = []

        if world_event and world_event['type'] == 'dangerous':
            return [] # No beasts available during dangerous events

        for name, template in self.beast_templates.items():
            if template['cost'] > 0:
                # Standard beasts are always available in peaceful times
                if name in ['leo_cub', 'scorpio_hatchling']:
                    available.append(name)

                # Event-specific beasts
                if world_event and world_event['name'] == 'merchants_festival' and name == 'phoenix_hatchling':
                    available.append(name)

        return available

    def buy_beast(self, beast_name, available_beasts):
        if beast_name not in available_beasts:
            return "This beast is currently not available for purchase."

        template = self.beast_templates[beast_name]
        if self.coins >= template['cost']:
            self.coins -= template['cost']

            beast_id = str(uuid.uuid4())
            self.owned_beasts[beast_id] = {
                'template': beast_name,
                'level': 1,
                'xp': 0
            }
            return f"A new {beast_name} joins your sanctuary! Its journey begins.", beast_id
        else:
            return "Not enough coins, creator. The world is expensive.", None

    def gain_xp(self, beast_id, amount):
        if beast_id not in self.owned_beasts:
            return "Unknown beast."

        beast = self.owned_beasts[beast_id]
        beast['xp'] += amount

        template = self.beast_templates[beast['template']]
        xp_needed = template['xp_to_next_level']

        leveled_up = False
        while beast['xp'] >= xp_needed:
            beast['level'] += 1
            beast['xp'] -= xp_needed
            leveled_up = True

            # Check for evolution
            if template['evolution']:
                beast['template'] = template['evolution']
                template = self.beast_templates[beast['template']]
                xp_needed = template['xp_to_next_level']
                return f"Your {beast_id[:8]}... has Evolved into a {beast['template']}! It is now level {beast['level']}."

        if leveled_up:
            return f"Your beast {beast_id[:8]} has leveled up to level {beast['level']}!"
        return f"Your beast {beast_id[:8]} gained {amount} XP."

    def use_beast_ability(self, beast_id):
        if beast_id not in self.owned_beasts:
            return "Unknown beast."

        beast = self.owned_beasts[beast_id]
        template = self.beast_templates[beast['template']]

        # Ability could be enhanced by level in the future
        return f"Your {beast['template']} (Lvl {beast['level']}) uses its ability: {template['ability']}"

    def get_beast_details(self, beast_id):
        if beast_id not in self.owned_beasts:
            return "Unknown beast."

        beast = self.owned_beasts[beast_id]
        template = self.beast_templates[beast['template']]
        return f"Beast ID: {beast_id[:8]}, Type: {beast['template']}, Level: {beast['level']}, XP: {beast['xp']}/{template['xp_to_next_level']}"

# --- Example Usage ---
# ecosystem = BeastEcosystem(10)
# beast_id = ecosystem.buy_beast('leo_cub') # Assuming this returns the ID
# print(ecosystem.get_beast_details(beast_id))
# print(ecosystem.gain_xp(beast_id, 150))
# print(ecosystem.get_beast_details(beast_id))
# print(ecosystem.use_beast_ability(beast_id))