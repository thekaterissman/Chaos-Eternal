# game.py - A demonstration of the premium access and racing features.

from kate import Game

def run_premium_content_scenario():
    """
    Runs a scenario to demonstrate the new premium features:
    - Purchasing premium access from the store.
    - Entering the exclusive underground world.
    - Exploring the new areas.
    - Participating in the new racing mode.
    """
    print("--- Starting Simulation: Premium Content and Racing Demo ---")

    # Initialize the main Game object
    game = Game()

    print("\nInitial State:")
    print(f"Player has premium access: {game.player_account.has_premium()}")
    print(f"Coins: {game.bestiary.coins}")
    print("-" * 20)

    # A sequence of actions designed to showcase the new features
    actions = [
        # 1. Try to access premium content without a pass (and fail)
        "enter underground",

        # 2. Purchase the premium pass from the store
        "store buy premium_access",

        # 3. Try to access the content again (and succeed)
        "enter underground",

        # 4. Explore the new underground world
        "explore rave",
        "explore forest",
        "explore racetrack",

        # 5. Switch to racing mode (only possible at the racetrack)
        "switch_mode racing",

        # 6. Start and complete a race
        "start race",
        "drive",
        "boost",
        "drift",
        "boost", # Go for the win
        "boost"
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
    print(f"Player has premium access: {game.player_account.has_premium()}")


if __name__ == "__main__":
    run_premium_content_scenario()