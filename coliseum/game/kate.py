# kate.py - The central game logic for The Coliseum: Chaos Eternal

from .Aichaosbrain import AIChaosBrain
from .Beast_bestiary import BeastBestiary
from .Gotcha_fails_system import GotchaFailsSystem
from .Modes_manager import ModesManager
from .characters import Kate, Amya, Holly

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

        # These systems are stateless and can be initialized on each request.
        self.ai_brain = AIChaosBrain()
        self.bestiary = BeastBestiary(coins=10) # Simplified for now
        self.fails_system = GotchaFailsSystem()
        self.modes_manager = ModesManager()

        # Load AI memory
        self.ai_brain.load_memory()

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
            # In a real game, coin rewards would be persistent.
            # self.bestiary.coins += 5
            messages.append("**** You earned 5 coins! ****")

    def game_loop_turn(self, player_action):
        """
        Simulates a single turn of the game, updates the player profile,
        and returns a list of messages to display.
        """
        messages = [f"--- Your action: {player_action} ---"]

        # 1. AI learns and acts
        self.ai_brain.learn_move(player_action)
        twist_message = self.ai_brain.throw_twist()
        messages.append(f"AI: {twist_message}")
        if "AI adapts" not in twist_message:
            self.player_profile.score += 50
            messages.append(f"** Score +50 for AI twist! Total Score: {self.player_profile.score} **")

        # 2. Handle actions
        if player_action == "use ability":
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
            # Generic action for simplicity
            xp_message = self.modes_manager.earn_xp(player_action)
            messages.append(xp_message)
            self.player_profile.score += 10
            messages.append(f"** Score +10 for action! Total Score: {self.player_profile.score} **")

        # 3. Check for level up
        self.check_level_up(messages)

        # 4. Save player state
        self.player_profile.save()
        self.ai_brain.save_memory()

        messages.append("--- Turn End ---")
        return messages