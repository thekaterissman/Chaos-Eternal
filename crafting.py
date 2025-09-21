# crafting.py - Handles crafting logic.

class Crafting:
    """
    Manages crafting recipes and processes crafting requests.
    This class holds the definitions for all craftable items and interacts
    with the player's inventory to create them.
    """
    def __init__(self):
        """
        Initializes the crafting system with a dictionary of recipes.
        Each recipe specifies the required resources and quantities.
        """
        self.recipes = {
            'shelter': {
                'description': 'A sturdy shelter to protect from the elements.',
                'resources': {'wood': 10, 'stone': 10},
                'haptic_feedback': 'You feel the ground shake as you complete the shelter! Haptics: A low rumble vibrates through your feet.'
            },
            'blade': {
                'description': 'A sharp stone blade, a basic survival tool.',
                'resources': {'stone': 2, 'vines': 5},
                'haptic_feedback': 'You feel the sharp edge of the blade against your palm. Haptics: A faint, sharp buzz.'
            }
        }

    def get_recipe(self, item_name):
        """
        Returns the recipe for a given item, if it exists.
        """
        return self.recipes.get(item_name.lower())

    def craft(self, item_name, inventory):
        """
        Attempts to craft an item.
        Checks the inventory for required resources, and if available,
        consumes them and returns a success message.
        """
        recipe = self.get_recipe(item_name)
        if not recipe:
            return "You don't know how to craft that."

        required = recipe['resources']
        if not inventory.has_resources(required):
            missing_items = []
            for resource, needed in required.items():
                if inventory.resources.get(resource, 0) < needed:
                    missing_items.append(f"{needed} {resource}")
            return f"You don't have enough resources. You need: {', '.join(missing_items)}."

        # Consume resources
        for resource, quantity in required.items():
            inventory.remove_resource(resource, quantity)

        # In a real game, this would add an item to the inventory.
        # For now, we just return a success message with haptic feedback.
        return f"You successfully crafted a {item_name}! {recipe['haptic_feedback']}"
