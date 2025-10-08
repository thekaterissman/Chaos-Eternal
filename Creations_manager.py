import random

class CreationsManager:
    """
    Manages the creation and storage of player-designed cosmetic awards.
    This system allows players to create their own unique items and share them.
    """
    def __init__(self):
        """
        Initializes the Creations Manager.
        - creations: A dictionary to store all created items, with the creator's name as the key.
        """
        self.creations = {}

    def create_award(self, character_name, is_vip, item_type, item_name, item_description):
        """
        Allows a player to design and create a new cosmetic item.

        Args:
            character_name (str): The name of the character creating the item.
            is_vip (bool): The VIP status of the creating character.
            item_type (str): The type of item (e.g., 'hat', 'glasses', 'shoes').
            item_name (str): The name of the new item.
            item_description (str): A player-written description for the item.

        Returns:
            str: A confirmation message.
        """
        if character_name not in self.creations:
            self.creations[character_name] = []

        new_item = {
            'type': item_type,
            'name': item_name,
            'description': item_description,
            'creator': character_name,
            'is_vip_creation': is_vip
        }

        self.creations[character_name].append(new_item)

        return f"A new masterpiece is born! '{item_name}', a {item_type}, has been crafted by {character_name}. Description: '{item_description}'"

    def get_vip_creations(self):
        """
        Retrieves a list of all items created by VIP players.

        Returns:
            list: A list of VIP creation dictionaries.
        """
        vip_items = []
        for creator_items in self.creations.values():
            for item in creator_items:
                if item.get('is_vip_creation', False):
                    vip_items.append(item)
        return vip_items

    def get_all_creations(self):
        """
        Retrieves a list of all items created by all players.

        Returns:
            list: A list of all creation dictionaries.
        """
        all_items = []
        for creator_items in self.creations.values():
            all_items.extend(creator_items)
        return all_items