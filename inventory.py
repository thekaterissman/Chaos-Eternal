# inventory.py - Manages player resources.

from collections import defaultdict

class Inventory:
    """
    Manages a player's inventory of resources.
    This class provides methods to add, remove, and check resource quantities,
    as well as display the current inventory.
    """
    def __init__(self):
        """
        Initializes the inventory with a defaultdict for easy resource management.
        """
        self.resources = defaultdict(int)

    def add_resource(self, resource_name, quantity):
        """
        Adds a specified quantity of a resource to the inventory.
        """
        if quantity > 0:
            self.resources[resource_name] += quantity
            return True
        return False

    def remove_resource(self, resource_name, quantity):
        """
        Removes a specified quantity of a resource from the inventory.
        Returns False if the resource is not available in sufficient quantity.
        """
        if self.has_resources({resource_name: quantity}):
            self.resources[resource_name] -= quantity
            return True
        return False

    def has_resources(self, required_resources):
        """
        Checks if the inventory contains at least the required quantities of resources.
        - required_resources: A dictionary like {'wood': 10, 'stone': 5}
        """
        for resource, quantity in required_resources.items():
            if self.resources[resource] < quantity:
                return False
        return True

    def __str__(self):
        """
        Returns a string representation of the current inventory.
        """
        if not self.resources:
            return "Your inventory is empty."

        # Filter out resources with a quantity of 0
        items = [f"- {name.capitalize()}: {quantity}" for name, quantity in self.resources.items() if quantity > 0]

        if not items:
            return "Your inventory is empty."

        return "Your inventory:\n" + "\n".join(items)
