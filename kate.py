# kate.py - The central game logic for The Coliseum: Chaos Eternal

from Aichaosbrain import AIChaosBrain
from Beast_bestiary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manager import ModesManager
from characters import Kate, Amya, Holly

class Game:
    """
    The main game engine, responsible for managing all game systems and running the game loop.
    This class ties together the AI, beasts, modes, and other mechanics into a cohesive experience.
    """
    def __init__(self, character=Kate()):
        """
        Initializes the game by setting up all the core systems.

        Args:
            character (Character, optional): The player character. Defaults to Kate().
        """
        print("The Coliseum rips free, floating. The Chaos Queens rise.")
        self.score = 0
        self.level = 1
        self.power_ups = {
            'jetpack': {'quantity': 1, 'effect': 'You soar through the air on jets of plasma!'},
            'whoopee_cushion': {'quantity': 1, 'effect': 'A comical *PFFFT* distracts your opponent.'}
        }
        self.character = character
        self.ai_brain = AIChaosBrain()
        self.bestiary = BeastBestiary(coins=10) # Start with some coins
        self.fails_system = GotchaFailsSystem()
        self.modes_manager = ModesManager()

        # Load any persistent data
        self.ai_brain.load_memory()
        print(f"Welcome, {self.character.name}, the {self.character.trait} Queen. Chaos awaits.")

    def switch_character(self, character_name):
        """
        Switches the player's character.

        Args:
            character_name (str): The name of the character to switch to (e.g., 'kate', 'amya', 'holly').

        Returns:
            str: A message indicating the result of the switch.
        """
        if character_name.lower() == 'kate':
            self.character = Kate()
        elif character_name.lower() == 'amya':
            self.character = Amya()
        elif character_name.lower() == 'holly':
            self.character = Holly()
        else:
            return "Unknown character."
        return f"Switched to {self.character.name}, the {self.character.trait} Queen."

    def check_level_up(self):
        """
        Checks if the player has earned enough XP to level up and handles the level-up process.
        A simple leveling system is used where each level requires 100 XP.
        """
        # Simple leveling system: 100 XP per level
        if self.modes_manager.xp >= self.level * 100:
            self.level += 1
            print(f"**** LEVEL UP! You are now Level {self.level}. ****")
            # Give a reward for leveling up
            self.bestiary.coins += 5
            print("**** You earned 5 coins! ****")


    def game_loop_turn(self, player_action):
        """
        Simulates a single turn of the game based on a player's action.
        This is a simplified game loop for this text-based simulation.

        Args:
            player_action (str): The action taken by the player (e.g., 'fight', 'use ability').
        """
        print(f"\n--- Your action: {player_action} ---")

        # 1. AI learns from the player's move
        self.ai_brain.learn_move(player_action)

        # 2. AI has a chance to throw a twist
        twist_message = self.ai_brain.throw_twist()
        print(f"AI: {twist_message}")
        if "AI adapts" not in twist_message: # Award points for interesting twists
            self.score += 50
            print(f"** Score +50 for AI twist! Total Score: {self.score} **")

        # 3. Handle specific, simulated actions
        if player_action == "use ability":
            ability_message = self.character.special_ability()
            print(ability_message)
            self.score += 75 # Big score for using an ability
            print(f"** Score +75 for special ability! Total Score: {self.score} **")

        elif player_action.startswith("use_powerup"):
            try:
                powerup_name = player_action.split(" ")[1]
                if self.power_ups.get(powerup_name) and self.power_ups[powerup_name]['quantity'] > 0:
                    self.power_ups[powerup_name]['quantity'] -= 1
                    print(self.power_ups[powerup_name]['effect'])
                    self.score += 15
                    print(f"** Score +15 for using a power-up! Total Score: {self.score} **")
                else:
                    print(f"No {powerup_name} power-up available!")
            except IndexError:
                print("Invalid command. Use 'use_powerup [name]'.")

        elif player_action.startswith("switch_character"):
            try:
                char_name = player_action.split(" ")[1]
                switch_message = self.switch_character(char_name)
                print(switch_message)
            except IndexError:
                print("Invalid switch_character command. Use 'switch_character [name]'.")

        elif player_action == "ride beast":
            # If the player doesn't own a beast, buy one for them for demo purposes.
            if not self.bestiary.owned_beasts:
                print("You have no beasts! Let's buy one...")
                buy_message = self.bestiary.buy_beast('leo_lion')
                print(buy_message)

            # Ride the first owned beast
            if self.bestiary.owned_beasts:
                ride_message = self.bestiary.ride_beast(self.bestiary.owned_beasts[0])
                print(ride_message)
                self.score += 25
                print(f"** Score +25 for riding a beast! Total Score: {self.score} **")


        elif player_action == "fail":
            fail_message = self.fails_system.add_fail("You tripped on a cosmic banana peel.")
            print(fail_message)
            self.score -= 10 # Lose points for failing
            print(f"** Score -10 for failing! Total Score: {self.score} **")

        elif player_action.startswith("switch_mode"):
            try:
                mode = player_action.split(" ")[1]
                mode_message = self.modes_manager.switch_mode(mode)
                print(mode_message)
            except IndexError:
                print("Invalid switch_mode command. Use 'switch_mode [mode]'.")

        else:
            # Handle actions based on the current mode
            if self.modes_manager.current_mode == 'therapy':
                if player_action == 'create':
                    print("You sculpt a beautiful, shimmering star out of cosmic dust.")
                    self.score += 5
                    print(f"** Score +5 for creating! Total Score: {self.score} **")
                elif player_action == 'reflect':
                    print("You sit by a holographic waterfall, finding a moment of peace.")
                    self.score += 5
                    print(f"** Score +5 for reflecting! Total Score: {self.score} **")
                else:
                    print(f"In Therapy Mode, you gently redirect your '{player_action}' energy into a peaceful hum.")
            else:
                # For any other action, treat it as a generic action that earns XP and score.
                xp_message = self.modes_manager.earn_xp(player_action)
                print(xp_message)
                self.score += 10
                print(f"** Score +10 for action! Total Score: {self.score} **")

        # 4. Check for level up at the end of the turn
        self.check_level_up()

        print("--- Turn End ---")


if __name__ == '__main__':
    # This is a simple demonstration of how the Game class orchestrates the systems.
    # In a real application, this would be driven by actual player input.
    print("--- Starting Game Simulation ---")
    game = Game() # Starts with Kate by default

    # A predefined sequence of actions to simulate gameplay
    actions = [
        "fight",
        "switch_mode therapy",
        "create",
        "reflect",
        "fight", # Should have a different outcome in therapy mode
        "switch_mode hunter",
        "fight" # Should be back to normal
    ]
    for action in actions:
        game.game_loop_turn(action)

    print("\n--- Game Simulation Ended ---")
