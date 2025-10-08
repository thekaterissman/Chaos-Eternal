# kate.py - The central game logic for The Coliseum: Chaos Eternal

from Aichaosbrain import AIChaosBrain
from Beast_bestiary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manager import ModesManager
from characters import Kate, Amya, Holly
from Player_mood import PlayerMood
from Visuals_engine import VisualsEngine
from Meta_play_store import MetaPlayStore
from Player_account import PlayerAccount
from Underground_world import UndergroundWorld
from Racing_system import RacingSystem
from Vehicle_customizer import VehicleCustomizer


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

        # Core systems
        self.modes_manager = ModesManager()
        self.ai_brain = AIChaosBrain(self.modes_manager)
        self.bestiary = BeastBestiary(self.modes_manager, coins=60) # Start with more coins for premium pass
        self.fails_system = GotchaFailsSystem()

        # Immersion and Monetization Systems
        self.player_mood = PlayerMood()
        self.visuals_engine = VisualsEngine(self.player_mood)
        self.player_account = PlayerAccount()
        self.meta_store = MetaPlayStore(self.bestiary, self.player_account)

        # Premium Content Systems
        self.underground_world = UndergroundWorld()
        self.vehicle_customizer = VehicleCustomizer(self.bestiary)
        self.racing_system = RacingSystem(self.vehicle_customizer)

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

        # 3. Update player mood based on the action before handling it
        self.player_mood.update_mood(player_action)
        print(self.visuals_engine.get_visual_description())

        # 4. Handle specific, simulated actions
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

        elif player_action.startswith("store"):
            parts = player_action.split(" ")
            if len(parts) > 1:
                if parts[1] == 'list':
                    print(self.meta_store.list_items())
                elif parts[1] == 'buy' and len(parts) > 2:
                    item_key = parts[2]
                    buy_message = self.meta_store.buy_item(item_key, self.power_ups)
                    print(buy_message)
                else:
                    print("Invalid store command. Use 'store list' or 'store buy [item_key]'.")
            else:
                print("Invalid store command. Use 'store list' or 'store buy [item_key]'.")


        elif player_action.startswith("switch_character"):
            try:
                char_name = player_action.split(" ")[1]
                switch_message = self.switch_character(char_name)
                print(switch_message)
            except IndexError:
                print("Invalid switch_character command. Use 'switch_character [name]'.")

        elif player_action.startswith("enter underground"):
            if self.player_account.has_premium():
                print(self.underground_world.enter_world())
            else:
                print("Access denied. A Premium Access Pass is required. Visit the store.")

        elif player_action.startswith("explore"):
            if self.underground_world.get_current_location():
                try:
                    location = player_action.split(" ")[1]
                    print(self.underground_world.explore_location(location))
                except IndexError:
                    print("Invalid command. Use 'explore [location]'.")
            else:
                print("You must be in the underground to explore it. Use 'enter underground' first.")

        elif player_action.startswith("customize") or player_action.startswith("upgrade"):
            parts = player_action.split(" ")
            command = parts[0]
            if command == 'customize' and len(parts) == 3:
                sub_command, value = parts[1], parts[2]
                if sub_command == 'color':
                    print(self.vehicle_customizer.customize_color(value))
                elif sub_command == 'type':
                    print(self.vehicle_customizer.set_vehicle_type(value))
                else:
                    print("Invalid command. Use 'customize color [color]' or 'customize type [type]'.")
            elif command == 'upgrade' and len(parts) == 2:
                part_name = parts[1]
                print(self.vehicle_customizer.upgrade_part(part_name))
            else:
                print("Invalid vehicle command. Use 'customize color [color]', 'customize type [type]', or 'upgrade [part]'.")

        elif player_action == "vehicle status":
            print(self.vehicle_customizer.get_description())

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
                # Add check for racing mode prerequisites
                if mode == 'racing' and self.underground_world.get_current_location() != 'racetrack':
                    print("ACCESS DENIED: You must be at the racetrack to enter racing mode.")
                else:
                    mode_message = self.modes_manager.switch_mode(mode)
                    print(mode_message)
            except IndexError:
                print("Invalid switch_mode command. Use 'switch_mode [mode]'.")

        elif player_action == "start race":
            if self.modes_manager.current_mode == 'racing':
                print(self.racing_system.start_race())
            else:
                print("You can only start a race when you are in 'racing' mode at the racetrack.")

        else:
            # Handle actions based on the current mode
            if self.modes_manager.current_mode == 'racing':
                # Pass racing actions to the racing system
                race_message = self.racing_system.handle_race_action(player_action)
                print(race_message)
            elif self.modes_manager.current_mode == 'therapy':
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

        # 5. Check for level up at the end of the turn
        self.check_level_up()

        # 6. Final mood update and visual description for the end of the turn
        self.player_mood.update_mood(player_action) # Update mood again after all effects
        print(self.visuals_engine.get_visual_description())

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
