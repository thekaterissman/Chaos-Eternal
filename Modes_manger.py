import random
import copy
from Wellness import Wellness
from Aichaosbrain import AIChaosBrain
from OracleQuest import available_quests

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds
        self.self_mode_unlocked = False
        self.wellness = Wellness()
        self.brain = AIChaosBrain()
        self.brain.load_memory() # Load AI memory on init
        self.active_quest = None

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
                return "Self Mode activated. Available activities: meditate, breathe, sound_therapy, cleanse, tarot, horoscope."
            else:
                return "Hunter Mode: Self-pick teams. Hunt or be hunted."
        return "Invalid mode – chaos only!"

    def do_wellness_activity(self, activity):
        if self.current_mode != 'self':
            return "You must be in Self Mode to perform wellness activities."

        # Perform the activity
        activity_result = ""
        if activity == 'meditate':
            activity_result = self.wellness.meditation()
        elif activity == 'breathe':
            activity_result = self.wellness.breathing_exercise()
        elif activity == 'sound_therapy':
            activity_result = self.wellness.sound_therapy()
        elif activity == 'cleanse':
            activity_result = self.wellness.cleansing()
        elif activity == 'tarot':
            activity_result = self.brain.tarot_reading()
        elif activity == 'horoscope':
            activity_result = self.brain.get_horoscope()
        else:
            return "Unknown wellness activity."

        # Check if the result is a prophecy that starts a quest
        if isinstance(activity_result, str) and activity_result.startswith("PROPHECY"):
            quest_key = None
            if "meditate to decipher the symbol" in activity_result:
                quest_key = "celestial_armor"

            if quest_key and (not self.active_quest or self.active_quest.name != available_quests[quest_key].name):
                self.active_quest = copy.deepcopy(available_quests[quest_key])
                return f"A new quest has begun! {self.active_quest.get_current_stage_description()}"
            return activity_result

        # If no prophecy was triggered, check for quest advancement
        if self.active_quest:
            advancement_message = self.active_quest.attempt_to_advance(activity)
            if advancement_message:
                if self.active_quest.is_complete:
                    self.active_quest = None
                return advancement_message

        return activity_result

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
# # Simulate getting a prophecy
# print("You received a prophecy from a horoscope reading!")
# manager.active_quest = copy.deepcopy(available_quests['celestial_armor'])
# print(manager.active_quest.get_current_stage_description())
# # Advance the quest
# print(manager.do_wellness_activity('meditate'))
# print(manager.do_wellness_activity('sound_therapy'))
# print(manager.do_wellness_activity('cleanse'))
