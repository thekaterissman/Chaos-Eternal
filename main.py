from Geevesbrain import GeevesBrain
from Beast_beastary import BeastEcosystem
from World_clock import WorldClock
from Reputation_engine import ReputationEngine
import time
import os

class GameWorld:
    def __init__(self):
        print("Forging the world's core systems...")
        self.geeves = GeevesBrain()
        self.ecosystem = BeastEcosystem(coins=20)
        self.clock = WorldClock()
        self.reputation = ReputationEngine()
        self.player_beasts = []
        print("The world is ready. Welcome, creator.")

    def main_loop(self):
        while True:
            print("\n" + "="*20)
            print("What is your will, creator?")
            print("1. [Status] - View the state of the world.")
            print("2. [Advance Time] - Let a day pass.")
            print("3. [Work] - Perform work to earn a coin.")
            print("4. [Buy Beast] - Purchase a new beast.")
            print("5. [Train Beast] - Train a beast to gain XP.")
            print("6. [Use Beast Ability] - Command a beast in a drill.")
            print("7. [Simulate Fight] - Test yourself and Geeves.")
            print("8. [Exit] - Leave the world.")

            choice = input("> ").lower().strip()
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice == '1':
                self.print_status()
            elif choice == '2':
                print(self.clock.advance_time())
            elif choice == '3':
                self.ecosystem.coins += 1
                print("You earn 1 coin for your efforts.")
            elif choice == '4':
                self.buy_beast_interface()
            elif choice == '5':
                self.train_beast_interface()
            elif choice == '6':
                self.use_beast_ability_interface()
            elif choice == '7':
                self.simulate_fight()
            elif choice == '8':
                print("The world will await your return.")
                break
            else:
                print("An invalid command. The world does not respond.")

    def print_status(self):
        print("\n--- WORLD STATUS ---")
        print(self.clock.get_status())
        print(self.reputation.get_status())
        print(f"Player Coins: {self.ecosystem.coins}")
        print("\n--- Player's Beasts ---")
        if not self.player_beasts:
            print("You own no beasts.")
        for beast_id in self.player_beasts:
            print(self.ecosystem.get_beast_details(beast_id))
        print("--------------------")

    def buy_beast_interface(self):
        current_event = self.clock.get_current_event()
        if current_event:
            # Add the event name to the dictionary for the ecosystem logic
            current_event['name'] = self.clock.current_event

        available_beasts = self.ecosystem.get_available_beasts(current_event)

        print("--- Beast Market ---")
        if not available_beasts:
            print("The beasts are hiding... No one is available for purchase.")
            return

        print("Available beasts for purchase:")
        for name in available_beasts:
            template = self.ecosystem.beast_templates[name]
            print(f"- {name} (Cost: {template['cost']})")

        beast_to_buy = input("Which beast do you wish to acquire? > ").lower().strip()

        message, beast_id = self.ecosystem.buy_beast(beast_to_buy, available_beasts)

        if beast_id:
            self.player_beasts.append(beast_id)
            print(f"Success! {message} Your new beast's ID is {beast_id[:8]}")
        else:
            print(message) # Print failure message

    def train_beast_interface(self):
        if not self.player_beasts:
            print("You have no beasts to train.")
            return
        print("Which beast do you want to train?")
        for i, beast_id in enumerate(self.player_beasts):
            print(f"{i+1}. {self.ecosystem.get_beast_details(beast_id)}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.player_beasts):
                beast_id = self.player_beasts[choice]
                xp_gain = random.randint(20, 50)
                print(self.ecosystem.gain_xp(beast_id, xp_gain))
            else:
                print("Invalid choice.")
        except (ValueError, IndexError):
            print("Invalid input.")

    def use_beast_ability_interface(self):
        if not self.player_beasts:
            print("You have no beasts to command.")
            return
        print("Which beast's ability do you want to use?")
        for i, beast_id in enumerate(self.player_beasts):
            print(f"{i+1}. {self.ecosystem.get_beast_details(beast_id)}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.player_beasts):
                beast_id = self.player_beasts[choice]
                beast_template = self.ecosystem.owned_beasts[beast_id]['template']
                # Geeves learns the generic move of using a beast's ability
                move = f"use_beast_{beast_template}"
                self.geeves.learn_move(move)
                print(f"\nYou command your beast...")
                time.sleep(0.5)
                print(self.ecosystem.use_beast_ability(beast_id))
                print(f"Geeves observes you using '{move}'.")
            else:
                print("Invalid choice.")
        except (ValueError, IndexError):
            print("Invalid input.")

    def simulate_fight(self):
        print("\nA challenger appears! You enter a simulated battle.")
        moves = ['attack', 'dodge', 'attack', 'block', 'use_item', 'attack', 'dodge']
        for move in moves:
            self.geeves.learn_move(move)
            print(f"You use '{move}'...")
            time.sleep(0.5)

        print("\nThe battle ends!")
        print(self.reputation.record_deed('honorable', 5, "Won a simulated battle."))

        reputation_title = self.reputation.get_reputation()
        print(f"Geeves considers your reputation: {reputation_title}")
        reaction = self.geeves.get_reaction(reputation_title)
        print(f"\nGEEVES' REACTION: {reaction}")

if __name__ == "__main__":
    world = GameWorld()
    world.main_loop()