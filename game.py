from Modes_manager import ModesManager
from Aichaosbrain import AIChaosBrain
from Beast_bestiary import BeastBestiary
from characters import Kate

def run_game_scenario():
    """
    Runs a scenario to demonstrate the difficulty settings affecting the game.
    """
    print("--- Initializing Game ---")
    modes_manager = ModesManager()
    ai_brain = AIChaosBrain(modes_manager)
    # Start with more coins to test purchases
    bestiary = BeastBestiary(modes_manager, coins=20)
    player = Kate()

    print(f"Welcome, {player.name}! Your trait: {player.trait}")
    print(f"Initial mode: {modes_manager.current_mode}")
    print(f"Initial difficulty: {modes_manager.difficulty}")
    print(f"Initial coins: {bestiary.coins}")
    print("-" * 20)

    # --- SCENARIO 1: MEDIUM DIFFICULTY (DEFAULT) ---
    print("\n--- Scenario: Medium Difficulty ---")
    print(f"Current difficulty: {modes_manager.difficulty}")

    # Demonstrate AI twist
    print("\nSimulating player dodging...")
    ai_brain.learn_move('attack')
    ai_brain.learn_move('attack')
    ai_brain.learn_move('dodge')
    # On medium, this is not enough to trigger a twist (needs 3 dodges in a row)
    print("AI response (1 dodge):", ai_brain.throw_twist())
    ai_brain.learn_move('dodge')
    ai_brain.learn_move('dodge')
    print("AI response (3 dodges):", ai_brain.throw_twist())

    # Demonstrate beast cost
    print("\nAttempting to buy a knight_mount (base cost 10)...")
    print(bestiary.buy_beast('knight_mount'))
    print(f"Coins remaining: {bestiary.coins}")
    print("-" * 20)


    # --- SCENARIO 2: EASY DIFFICULTY ---
    print("\n--- Scenario: Easy Difficulty ---")
    modes_manager.set_difficulty('easy')
    print(f"Difficulty changed to: {modes_manager.difficulty}")
    ai_brain.player_moves = [] # Reset moves for a clean test
    bestiary.coins = 20 # Reset coins

    # Demonstrate AI twist (less sensitive)
    print("\nSimulating player dodging (less sensitive)...")
    ai_brain.learn_move('dodge')
    # On easy, 1 dodge is not enough to trigger a twist (needs 2)
    print("AI response (1 dodge):", ai_brain.throw_twist())
    ai_brain.learn_move('dodge')
    print("AI response (2 dodges):", ai_brain.throw_twist())

    # Demonstrate beast cost (cheaper)
    print("\nAttempting to buy a knight_mount (base cost 10)...")
    # Cost should be 10 * 0.8 = 8
    print(bestiary.buy_beast('knight_mount'))
    print(f"Coins remaining: {bestiary.coins}")
    print("-" * 20)

    # --- SCENARIO 3: HARD DIFFICULTY ---
    print("\n--- Scenario: Hard Difficulty ---")
    modes_manager.set_difficulty('hard')
    print(f"Difficulty changed to: {modes_manager.difficulty}")
    ai_brain.player_moves = [] # Reset moves
    bestiary.coins = 20 # Reset coins

    # Demonstrate AI twist (more sensitive)
    print("\nSimulating player dodging (more sensitive)...")
    ai_brain.learn_move('attack')
    ai_brain.learn_move('attack')
    ai_brain.learn_move('attack')
    ai_brain.learn_move('dodge')
    # On hard, even one dodge in the last 4 moves is enough for a twist
    print("AI response (1 dodge in last 4):", ai_brain.throw_twist())

    # Demonstrate beast cost (more expensive)
    print("\nAttempting to buy a knight_mount (base cost 10)...")
    # Cost should be 10 * 1.5 = 15
    print(bestiary.buy_beast('knight_mount'))
    print(f"Coins remaining: {bestiary.coins}")


if __name__ == "__main__":
    run_game_scenario()
