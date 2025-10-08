from Player import Player

class Items:
    def __init__(self, player: Player):
        self.player = player
        self.available_items = {
            "Gold Sandals": {
                "type": "swag",
                "description": "Walk with the confidence of an emperor. Provides a passive speed boost.",
                "bonus": {"stat": "speed", "amount": 2}
            },
            "Roman Toga": {
                "type": "swag",
                "description": "The classic look of a Roman senator. Increases XP gain.",
                "bonus": {"stat": "xp_rate", "amount": 0.1}  # 10% boost
            },
            "Ancient Stones Heal Pack": {
                "type": "consumable",
                "effect": "heal",
                "amount": 50,
                "description": "Heals for 50 HP. Racing boosts heal amount."
            },
            "Speed Boost": {
                "type": "consumable",
                "effect": "speed",
                "amount": 5,
                "description": "Increases speed by 5 for a short duration."
            }
        }
        self.owned_items = []
        self.equipped_items = []

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
                self.owned_items.remove(item_name)
                return self.player.heal(item["amount"])
            elif item["effect"] == "speed":
                self.owned_items.remove(item_name)
                return self.player.increase_speed(item["amount"])

        return f"Cannot use {item_name}."

    def equip_item(self, item_name):
        if item_name not in self.owned_items:
            return f"You do not own '{item_name}'."
        if item_name in self.equipped_items:
            return f"{item_name} is already equipped."

        item = self.available_items.get(item_name)
        if not item or "bonus" not in item:
            return f"{item_name} has no equippable effect."

        bonus = item["bonus"]
        if bonus["stat"] == "speed":
            self.player.increase_speed(bonus["amount"])
        elif bonus["stat"] == "xp_rate":
            self.player.increase_xp_rate(bonus["amount"])

        self.equipped_items.append(item_name)
        return f"{item_name} equipped. You feel its power!"

    def unequip_item(self, item_name):
        if item_name not in self.equipped_items:
            return f"You do not have {item_name} equipped."

        item = self.available_items.get(item_name)
        if not item or "bonus" not in item:
            return f"Error: {item_name} has no bonus to remove."

        bonus = item["bonus"]
        if bonus["stat"] == "speed":
            self.player.decrease_speed(bonus["amount"])
        elif bonus["stat"] == "xp_rate":
            self.player.decrease_xp_rate(bonus["amount"])

        self.equipped_items.remove(item_name)
        return f"{item_name} unequipped."