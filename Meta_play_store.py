# Meta_play_store.py - A simulated in-game store for purchasing virtual goods.

class MetaPlayStore:
    """
    Simulates an in-game marketplace where players can purchase power-ups,
    cosmetic effects, and other virtual items using in-game currency.
    """
    def __init__(self, bestiary):
        """
        Initializes the Meta Play Store.

        Args:
            bestiary (BeastBestiary): The instance of the bestiary, used to access the player's coin balance.
        """
        self.bestiary = bestiary
        self.items = {
            'jetpack_refuel': {
                'name': 'Jetpack Refuel',
                'cost': 5,
                'type': 'power-up',
                'description': 'Refuels your jetpack for another exhilarating flight.'
            },
            'cosmic_confetti': {
                'name': 'Cosmic Confetti',
                'cost': 2,
                'type': 'cosmetic',
                'description': 'A shower of glittering cosmic confetti follows your every move for a short time.'
            },
            'shield_potion': {
                'name': 'Shield Potion',
                'cost': 10,
                'type': 'power-up',
                'description': 'Grants a temporary shield that absorbs one hit.'
            },
            'holographic_aura': {
                'name': 'Holographic Aura',
                'cost': 8,
                'type': 'cosmetic',
                'description': 'Surrounds you with a shimmering, customizable holographic aura.'
            }
        }
        print("Meta Play Store is now open for business!")

    def list_items(self):
        """
        Displays all items available for purchase in the store.

        Returns:
            str: A formatted string listing all available items.
        """
        if not self.items:
            return "The store is currently empty."

        item_list = "--- Welcome to the Meta Play Store! ---\n"
        for key, item in self.items.items():
            item_list += (f"- {item['name']} ({item['type']}) | Cost: {item['cost']} coins\n"
                          f"  Description: {item['description']}\n")
        item_list += f"\nYou have {self.bestiary.coins} coins.\n"
        return item_list

    def buy_item(self, item_key, power_ups_inventory):
        """
        Allows the player to purchase an item from the store.

        Args:
            item_key (str): The key of the item to purchase (e.g., 'jetpack_refuel').
            power_ups_inventory (dict): The player's power-up inventory to update.

        Returns:
            str: A message indicating the result of the transaction.
        """
        if item_key not in self.items:
            return f"Item '{item_key}' not found in the store."

        item = self.items[item_key]
        cost = item['cost']

        if self.bestiary.coins >= cost:
            self.bestiary.coins -= cost

            # Add the item to the player's inventory if it's a power-up
            if item['type'] == 'power-up':
                # Simplified: for now, we just add the item name. A real implementation
                # would need to handle stacking or specific effects.
                if item_key in power_ups_inventory:
                    power_ups_inventory[item_key]['quantity'] += 1
                else:
                    # A more robust system would be needed for new power-up types
                    # This is a simplification for the text-based game.
                    power_ups_inventory[item_key] = {'quantity': 1, 'effect': item['description']}

            return (f"You purchased '{item['name']}' for {cost} coins. "
                    f"You have {self.bestiary.coins} coins remaining.")
        else:
            return (f"You do not have enough coins to buy '{item['name']}'. "
                    f"You need {cost} coins, but you only have {self.bestiary.coins}.")