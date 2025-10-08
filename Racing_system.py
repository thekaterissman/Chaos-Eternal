# Racing_system.py - Manages the logic for the new underground racing mode.

import random

class RacingSystem:
    """
    Manages the state and actions for the premium underground racing mode.
    The system is designed to provide a thrilling, text-based racing experience.
    """
    def __init__(self, vehicle_customizer):
        """
        Initializes the Racing System.

        Args:
            vehicle_customizer (VehicleCustomizer): The player's vehicle for performance stats.
        """
        self.vehicle_customizer = vehicle_customizer
        self.race_in_progress = False
        self.player_position = 0
        self.opponent_position = 0
        self.race_length = 100 # An arbitrary length for the race

    def start_race(self):
        """
        Starts a new race, resetting all state variables.
        """
        self.race_in_progress = True
        self.player_position = 0
        self.opponent_position = 0
        return (
            "HAPTICS: The engine roars to life, a deep vibration that you feel in your bones. "
            "A holographic countdown appears in the air: 3... 2... 1... GO! You slam the accelerator."
        )

    def handle_race_action(self, action):
        """
        Processes a player's action during a race and updates the race state.

        Args:
            action (str): The racing action taken by the player (e.g., 'boost', 'drift').

        Returns:
            str: A descriptive string of the outcome of the action.
        """
        if not self.race_in_progress:
            return "There is no race in progress. Start one from the racetrack."

        # Opponent makes a move
        self.opponent_position += random.randint(15, 25)

        # Get performance bonus from upgrades
        bonus = self.vehicle_customizer.get_performance_bonus(action)

        # Player makes a move
        if action == 'boost':
            move_distance = int(random.randint(20, 30) * bonus)
            self.player_position += move_distance
            action_desc = (
                "You hit the boost! HAPTICS: A powerful G-force presses you into your seat. The rush of air is a physical force, "
                "and you feel the wind whip past your helmet as the psychedelic forest blurs into a tunnel of light."
            )
        elif action == 'drift':
            move_distance = int(random.randint(10, 18) * bonus)
            self.player_position += move_distance
            action_desc = (
                "You execute a perfect drift around a sharp, crystalline corner. HAPTICS: You feel the tires lose and regain grip, "
                "a controlled slide that gains you precious inches, your upgraded tires holding the line beautifully."
            )
        else: # A generic 'drive' action
            move_distance = int(random.randint(15, 22) * bonus)
            self.player_position += move_distance
            action_desc = "You focus on the racing line, weaving through the track with precision."

        # Check for race end
        if self.player_position >= self.race_length or self.opponent_position >= self.race_length:
            self.race_in_progress = False
            if self.player_position > self.opponent_position:
                return f"{action_desc}\nWINNER! You cross the finish line just ahead of your opponent! The crowd roars your name."
            else:
                return f"{action_desc}\nSo close! Your opponent zips past the finish line just before you. A tough loss, but an incredible race."

        # Continue race
        position_report = f"You are at {self.player_position}m, your opponent is at {self.opponent_position}m."
        return f"{action_desc}\n{position_report}"