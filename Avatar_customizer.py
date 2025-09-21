import random

class AvatarCustomizer:
    def __init__(self, coins=0):
        self.coins = coins
        self.avatar_items = {
            'holographic_laurel_wreath': {'cost': 2, 'description': 'A shimmering, holographic laurel wreath that floats above your head.'},
            'plasma_toga': {'cost': 5, 'description': 'A toga woven from pure, shimmering plasma. A statement piece.'},
            'rocket_sandals': {'cost': 3, 'description': 'Sandals with small rocket boosters for enhanced jumping.'},
            'basic_tunic': {'cost': 0, 'description': 'A simple, yet elegant, futuristic Roman tunic.'},
            'senator_robe': {'cost': 10, 'description': 'An ornate robe signifying your status as a senior member of the Coliseum.'}
        }
        self.owned_avatar_items = []
        self.equipped_items = []

    def buy_avatar_item(self, item_name):
        if item_name in self.avatar_items and self.coins >= self.avatar_items[item_name]['cost']:
            self.coins -= self.avatar_items[item_name]['cost']
            self.owned_avatar_items.append(item_name)
            return f"Avatar item acquired: {self.avatar_items[item_name]['description']}"
        else:
            return "Not enough coins for this avatar item. Go win some fights!"

    def equip_avatar_item(self, item_name):
        if item_name in self.owned_avatar_items:
            if item_name not in self.equipped_items:
                self.equipped_items.append(item_name)
                return f"{item_name} equipped. You look magnificent!"
            else:
                return f"You already have {item_name} equipped."
        return "You don't own this item. Buy it from the avatar shop first!"

    def unequip_avatar_item(self, item_name):
        if item_name in self.equipped_items:
            self.equipped_items.remove(item_name)
            return f"{item_name} unequipped."
        return "You don't have that item equipped."

    def view_owned_items(self):
        if not self.owned_avatar_items:
            return "You don't own any avatar items yet."
        return "You own: " + ", ".join(self.owned_avatar_items)

    def view_shop(self):
        shop_listings = ["Welcome to the Avatar Shop!"]
        for item, details in self.avatar_items.items():
            shop_listings.append(f"- {item} (Cost: {details['cost']}): {details['description']}")
        return "\n".join(shop_listings)

# Usage:
# customizer = AvatarCustomizer(10)
# print(customizer.view_shop())
# print("\\n" + customizer.buy_avatar_item('plasma_toga'))
# print(customizer.buy_avatar_item('holographic_laurel_wreath'))
# print(customizer.buy_avatar_item('senator_robe')) # Fails, not enough coins
# print("\\n" + customizer.view_owned_items())
# print("\\n" + customizer.equip_avatar_item('plasma_toga'))
# print(customizer.equip_avatar_item('plasma_toga')) # Fails, already equipped
# print(customizer.unequip_avatar_item('plasma_toga'))
# print(customizer.equip_avatar_item('senator_robe')) # Fails, not owned
