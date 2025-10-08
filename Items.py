from Player import Player

class Items:
    def __init__(self, player: Player):
        self.player = player
        self.available_items = {
            "Gold Sandals": {"type": "swag", "description": "Walk with the confidence of an emperor."},
            "Roman Toga": {"type": "swag", "description": "The classic look of a Roman senator."},
            "Ancient Stones Heal Pack": {"type": "consumable", "effect": "heal", "amount": 50, "description": "Heals for 50 HP. Racing boosts heal amount."},
            "Speed Boost": {"type": "consumable", "effect": "speed", "amount": 5, "description": "Increases speed by 5 for a short duration."}
        }
        self.owned_items = []

    def acquire_item(self, item_name):
        if item_name in self.available_items:
            self.owned_items.append(item_name)
            return f"You have acquired {item_name}!"
        return f"Item '{item_name}' not found."

    def use_item(self, item_name):
        if item_name not in self.owned_items:
            return f"You do not own '{item_name}'."

        item = self.available_items.get(item_name)
        if not item:
            return "Something went wrong. Item not found in master list."

        if item["type"] == "swag":
            return f"You show off your {item_name}. {item['description']}"

        if item["type"] == "consumable":
            if item["effect"] == "heal":
                # Remove the item after use
                self.owned_items.remove(item_name)
                return self.player.heal(item["amount"])
            elif item["effect"] == "speed":
                # Remove the item after use
                self.owned_items.remove(item_name)
                return self.player.increase_speed(item["amount"])

        return f"Cannot use {item_name}."