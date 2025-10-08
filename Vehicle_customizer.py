# Vehicle_customizer.py - Manages vehicle customization and upgrades.

class VehicleCustomizer:
    """
    Manages the player's customizable vehicle, including its type,
    cosmetic appearance, and performance upgrades.
    """
    def __init__(self, bestiary):
        """
        Initializes the player's vehicle.

        Args:
            bestiary (BeastBestiary): The instance of the bestiary, used for coin transactions.
        """
        self.bestiary = bestiary
        self.vehicle_type = 'car' # Default vehicle
        self.color = 'matte black'
        self.performance_parts = {
            'engine': {'level': 1, 'max_level': 5, 'boost_bonus': 0.1},
            'tires': {'level': 1, 'max_level': 5, 'drift_bonus': 0.1}
        }
        self.upgrade_costs = {
            'engine': 20,
            'tires': 15
        }
        print("Vehicle customizer garage is now open. Default car is ready.")

    def set_vehicle_type(self, v_type):
        """Sets the vehicle type (e.g., 'car' or 'truck')."""
        if v_type in ['car', 'truck']:
            self.vehicle_type = v_type
            return f"Vehicle type set to: {self.vehicle_type}."
        return "Invalid vehicle type. Choose 'car' or 'truck'."

    def customize_color(self, new_color):
        """
        Customizes the vehicle's color for a fee.
        """
        cost = 5 # A flat fee for a paint job
        if self.bestiary.coins >= cost:
            self.bestiary.coins -= cost
            self.color = new_color
            return f"Your {self.vehicle_type} has been painted {self.color} for {cost} coins."
        return f"Not enough coins for a paint job. You need {cost} coins."

    def upgrade_part(self, part_name):
        """
        Upgrades a performance part to the next level for a fee.
        """
        if part_name not in self.performance_parts:
            return f"Invalid part: {part_name}. Choose 'engine' or 'tires'."

        part = self.performance_parts[part_name]
        if part['level'] >= part['max_level']:
            return f"Your {part_name} is already at the maximum level."

        cost = self.upgrade_costs[part_name] * part['level'] # Cost increases with level
        if self.bestiary.coins >= cost:
            self.bestiary.coins -= cost
            part['level'] += 1
            return (f"Your {part_name} has been upgraded to Level {part['level']} for {cost} coins! "
                    f"HAPTICS: You hear the satisfying *clink* of new hardware being installed.")
        return f"Not enough coins to upgrade {part_name}. You need {cost} coins."

    def get_performance_bonus(self, action):
        """
        Calculates the performance bonus for a given racing action based on upgrades.
        """
        if action == 'boost':
            return 1.0 + (self.performance_parts['engine']['level'] * self.performance_parts['engine']['boost_bonus'])
        elif action == 'drift':
            return 1.0 + (self.performance_parts['tires']['level'] * self.performance_parts['tires']['drift_bonus'])
        return 1.0 # No bonus for other actions

    def get_description(self):
        """
        Returns a string describing the current state of the vehicle.
        """
        return (f"Your vehicle: A {self.color} {self.vehicle_type} with a "
                f"Level {self.performance_parts['engine']['level']} engine and "
                f"Level {self.performance_parts['tires']['level']} tires.")