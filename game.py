# game.py - A demonstration of vehicle customization and racing.

from kate import Game

def run_vehicle_customization_scenario():
    """
    Runs a scenario to demonstrate the new vehicle customization features:
    - Customizing a vehicle's color and type.
    - Upgrading performance parts.
    - Experiencing the performance boost during a race.
    """
    print("--- Starting Simulation: Vehicle Customization and Racing Demo ---")

    # Initialize the main Game object
    game = Game()

    # Start with premium access for this demo to get right to the action
    game.player_account.upgrade_to_premium()
    print("-" * 20)

    # A sequence of actions designed to showcase the new features
    actions = [
        # 1. Enter the underground world and head to the racetrack
        "enter underground",
        "explore racetrack",

        # 2. Check the default vehicle status
        "vehicle status",

        # 3. Customize the vehicle
        "customize color electric-blue",
        "customize type truck",

        # 4. Upgrade performance parts (costs coins)
        "upgrade engine", # Cost: 20
        "upgrade engine", # Cost: 40 (Player has 60 coins, so this will fail)
        "upgrade tires",  # Cost: 15 (Player has 40 coins left, can afford)

        # 5. Check the final vehicle status
        "vehicle status",

        # 6. Start a race to feel the difference
        "switch_mode racing",
        "start race",
        "boost", # Should be more effective now with Level 2 engine
        "drift", # Should be more effective now with Level 2 tires
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
    print(f"Final Vehicle Status: {game.vehicle_customizer.get_description()}")


if __name__ == "__main__":
    run_vehicle_customization_scenario()