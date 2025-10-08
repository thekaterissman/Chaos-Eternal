# game.py - A demonstration of the game's features, including mood, visuals, and the store.

from kate import Game

def run_immersion_scenario():
    """
    Runs a scenario to demonstrate the new immersion features:
    - Player Mood
    - Visuals Engine
    - Meta Play Store
    """
    print("--- Starting Simulation: Immersion and Monetization Demo ---")

    # Initialize the main Game object, which now contains all subsystems
    game = Game()

    print("\nInitial State:")
    print(f"Player Mood: {game.player_mood.get_mood()}")
    print(f"Coins: {game.bestiary.coins}")
    print(game.visuals_engine.get_visual_description())
    print("-" * 20)

    # A sequence of actions designed to showcase the new features
    actions = [
        # 1. Start with an exciting action to change the mood
        "fight",

        # 2. Use an ability to keep the excitement high
        "use ability",

        # 3. Experience a failure to see the mood shift to tense
        "fail",

        # 4. Switch to a calm activity
        "switch_mode therapy",
        "reflect",

        # 5. Interact with the new Meta Play Store
        "store list",
        "store buy shield_potion", # Player has 20 coins, can afford this (cost 10)
        "store buy holographic_aura", # Player has 10 coins left, can afford this (cost 8)
        "store buy jetpack_refuel", # Player has 2 coins left, cannot afford this (cost 5)

        # 6. Use a newly purchased item
        "use_powerup shield_potion"
    ]

    # Execute the actions one by one
    for action in actions:
        game.game_loop_turn(action)
        # A small divider to make the turn-by-turn output clearer
        print("-" * 20)

    print("\n--- Simulation Ended ---")
    print(f"Final Score: {game.score}")
    print(f"Final Level: {game.level}")
    print(f"Final Coins: {game.bestiary.coins}")
    print(f"Final Mood: {game.player_mood.get_mood()}")


if __name__ == "__main__":
    run_immersion_scenario()