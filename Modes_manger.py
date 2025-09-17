import random

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds
        self.self_mode_unlocked = False

    def unlock_self_mode(self, payment_method, amount):
        if payment_method == 'xp' and self.xp >= amount:
            self.xp -= amount
            self.self_mode_unlocked = True
            return "Self Mode unlocked with XP!"
        elif payment_method == 'paid':
            self.self_mode_unlocked = True
            return f"Self Mode unlocked with {amount}!"
        return "Unlocking failed. Not enough XP or invalid payment method."

    def switch_mode(self, mode):
        modes = ['hunter', 'survival', 'pvp', 'raid', 'self']
        if mode in modes:
            if mode == 'self' and not self.self_mode_unlocked:
                return "Self Mode is locked. Unlock with XP or payment."
            self.current_mode = mode
            if mode == 'survival':
                return "Survival Mode: Craft vines to blades. XP sticks – no resets!"
            elif mode == 'pvp':
                return "PvP: Teams self-select. Mix crews, clash in the arena!"
            elif mode == 'raid':
                return "Raid villages! Steal loot, burn down – haptics make walls crack."
            elif mode == 'self':
                return "Self Mode: Breathe, meditate, reflect. Find your center."
            else:
                return "Hunter Mode: Self-pick teams. Hunt or be hunted."
        return "Invalid mode – chaos only!"

    def earn_xp(self, action):
        xp_gain = random.randint(10, 50)
        self.xp += xp_gain
        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')  # Build persists
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

# Usage:
# manager = ModesManager()
# print(manager.switch_mode('self'))  # See that it's locked
# manager.earn_xp('fight')
# manager.earn_xp('fight')
# print(manager.unlock_self_mode('xp', 100)) # Unlock with XP
# print(manager.switch_mode('self'))
# print(manager.unlock_self_mode('paid', '$0.99')) # Or unlock with money
# print(manager.switch_mode('self'))
