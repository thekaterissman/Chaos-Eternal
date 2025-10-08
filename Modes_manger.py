import random
from World import World
from Player import Player
from Items import Items
from MusicPlayer import MusicPlayer
from Race import Race
from ColorPuzzle import ColorPuzzle
from Emotes import Emote

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds
        self.world = World()
        self.player = Player("ChaosQueen")
        self.items = Items(self.player)
        self.music_player = MusicPlayer()
        self.race = None
        self.color_puzzle = ColorPuzzle(self.player)
        self.emote_system = Emote()

    def switch_mode(self, mode):
        modes = ['hunter', 'survival', 'pvp', 'raid', 'self', 'racing', 'living_aura']
        if mode in modes:
            self.current_mode = mode
            if mode == 'living_aura':
                if self.player.has_learned_colors:
                    return "You enter the living aura. The world is vibrant and full of color. Communication is through action, not words."
                else:
                    return "You enter the living aura. The world is a muted grayscale. You feel a strange pull towards a set of pedestals."
            elif mode == 'racing':
                self.race = Race(self.player)
                return self.race.start_race()
            elif mode == 'survival':
                return "Survival Mode: Craft vines to blades. XP sticks – no resets!"
            elif mode == 'pvp':
                return "PvP: Teams self-select. Mix crews, clash in the arena!"
            elif mode == 'raid':
                return "Raid villages! Steal loot, burn down – haptics make walls crack."
            elif mode == 'self':
                return self.world.fade_constellation()
            else:
                return "Hunter Mode: Self-pick teams. Hunt or be hunted."
        return "Invalid mode – chaos only!"

    def earn_xp(self, action):
        xp_gain = int(random.randint(10, 50) * self.player.xp_rate)
        self.xp += xp_gain
        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

    def get_swag(self, item_name):
        return self.items.acquire_item(item_name)

    def use_item(self, item_name):
        if item_name == "Ancient Stones Heal Pack" and self.current_mode == "racing":
            original_heal_amount = self.items.available_items.get(item_name, {}).get("amount", 50)
            boosted_heal = original_heal_amount * 2
            if item_name in self.items.owned_items:
                self.items.owned_items.remove(item_name)
            return self.player.heal(boosted_heal)
        return self.items.use_item(item_name)

    def equip_item(self, item_name):
        return self.items.equip_item(item_name)

    def unequip_item(self, item_name):
        return self.items.unequip_item(item_name)

    def play_music(self, station_name):
        return self.music_player.select_station(station_name)

    def stop_music(self):
        return self.music_player.stop_music()

    def navigate_race(self, action=None):
        if self.current_mode != 'racing' or not self.race:
            return "You are not currently in a race."

        result = self.race.navigate_obstacle(action)
        if self.race.is_complete:
            reward_message, reward_amount = self.race.get_reward()
            self.xp += reward_amount
            return result + " " + reward_message
        return result

    def get_color_puzzle_description(self):
        return self.color_puzzle.get_description()

    def solve_color_puzzle(self, sequence):
        return self.color_puzzle.attempt_solution(sequence)

    def emote(self, emote_name):
        if self.current_mode == 'living_aura':
            return self.emote_system.perform_emote(emote_name)
        return "You can only perform emotes in the living aura."

# Usage examples
# manager = ModesManager()
# print(manager.switch_mode('living_aura'))
# print(manager.get_color_puzzle_description())
# print(manager.solve_color_puzzle(['Red', 'Green', 'Blue']))
# print(manager.switch_mode('living_aura'))
# print(manager.emote('wave'))