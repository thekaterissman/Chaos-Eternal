# kate.py - The central game logic for The Coliseum: Chaos Eternal

from .Aichaosbrain import AIChaosBrain
from .Beast_bestiary import BeastBestiary
from .Gotcha_fails_system import GotchaFailsSystem
from .Modes_manager import ModesManager
from .characters import Kate, Amya, Holly
from .light_therapy import LightTherapyManager

class Game:
    """
    The main game engine, responsible for managing all game systems and running the game loop.
    This class is now initialized with a player profile to manage state.
    """
    def __init__(self, player_profile):
        """
        Initializes the game using a PlayerProfile instance.
        """
        self.player_profile = player_profile
        self.character = self.get_character_class(player_profile.character_name)

        self.ai_brain = AIChaosBrain(self.player_profile.ai_memory)
        self.bestiary = BeastBestiary(coins=10)
        self.fails_system = GotchaFailsSystem()
        self.modes_manager = ModesManager()
        self.light_therapy_manager = LightTherapyManager()

        self.modes_manager.current_mode = self.player_profile.current_mode

    def get_character_class(self, character_name):
        """Returns the character class instance based on the name."""
        if character_name.lower() == 'amya':
            return Amya()
        elif character_name.lower() == 'holly':
            return Holly()
        else: # Default to Kate
            return Kate()

    def check_level_up(self, messages):
        """Checks if the player has enough XP to level up."""
        if self.modes_manager.xp >= self.player_profile.level * 100:
            self.player_profile.level += 1
            messages.append(f"**** LEVEL UP! You are now Level {self.player_profile.level}. ****")
            messages.append("**** You earned 5 coins! ****")

    def game_loop_turn(self, player_action):
        """
        Simulates a single turn of the game, updates the player profile,
        and returns a list of messages to display.
        """
        messages = [f"--- Your action: {player_action} ---"]

        if player_action.startswith("switch_mode"):
            try:
                mode = player_action.split(" ")[1]
                mode_message = self.modes_manager.switch_mode(mode)
                messages.append(mode_message)
                if "Invalid" not in mode_message:
                    self.player_profile.current_mode = self.modes_manager.current_mode
                    self.player_profile.save()
            except IndexError:
                messages.append("Invalid switch_mode command. Use 'switch_mode [mode]'.")
            return messages

        self.ai_brain.learn_move(player_action)
        twist_message = self.ai_brain.throw_twist()
        messages.append(f"AI: {twist_message}")
        if "AI adapts" not in twist_message:
            self.player_profile.score += 50
            messages.append(f"** Score +50 for AI twist! Total Score: {self.player_profile.score} **")

        if self.player_profile.current_mode == 'therapy':
            if "create with" in player_action:
                try:
                    color = player_action.split("with ")[1].replace(" light", "")
                    therapy_message = self.light_therapy_manager.create_with_light(color)
                    messages.append(therapy_message)
                    self.player_profile.score += 5
                except IndexError:
                    messages.append("Invalid create command. Use 'create with [color] light'.")
            elif "reflect" in player_action:
                therapy_message = self.light_therapy_manager.reflect_on_aura()
                messages.append(therapy_message)
                self.player_profile.score += 5
            else:
                messages.append(f"You take a deep breath, focusing on the light within. (Try 'reflect on your inner aura')")

        elif player_action == "use ability":
            ability_message = self.character.special_ability()
            messages.append(ability_message)
            self.player_profile.score += 75
            messages.append(f"** Score +75 for special ability! Total Score: {self.player_profile.score} **")

        elif player_action == "fail":
            fail_message = self.fails_system.add_fail("You tripped on a cosmic banana peel.")
            messages.append(fail_message)
            self.player_profile.score -= 10
            messages.append(f"** Score -10 for failing! Total Score: {self.player_profile.score} **")

        else:
            xp_message = self.modes_manager.earn_xp(player_action)
            messages.append(xp_message)
            self.player_profile.score += 10
            messages.append(f"** Score +10 for action! Total Score: {self.player_profile.score} **")

        self.check_level_up(messages)

        # Persist the AI's memory back to the player's profile
        self.player_profile.ai_memory = self.ai_brain.player_moves
        self.player_profile.save()

        messages.append("--- Turn End ---")
        return messages