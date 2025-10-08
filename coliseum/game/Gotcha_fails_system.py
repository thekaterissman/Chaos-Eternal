import random

class GotchaFailsSystem:
    """
    Manages the game's "Fails Reel" and "Gotcha List" for anti-bullying.
    This system adds a social and humorous element to gameplay, highlighting
    epic fails and providing fun consequences for negative behavior.
    """
    def __init__(self):
        """
        Initializes the Gotcha Fails System.
        - fails_reel: A list to store descriptions of player failures.
        - gotcha_list: A list to track bullies and their punishments.
        """
        self.fails_reel = []
        self.gotcha_list = []

    def add_fail(self, fail_desc):
        """
        Adds a player's fail to the public "Fails Reel".
        This is intended to be a fun, non-punitive way to celebrate clumsy moments.
        """
        self.fails_reel.append(fail_desc)
        sound = random.choice(['kazoo solo', 'cosmic chimes', 'fart noise'])
        return f"Total Fails: {fail_desc} – Reel plays with {sound}. Crowd laughs!"

    def gotcha_bully(self, bully_name):
        """
        Adds a bully to the "Gotcha List" and assigns a random, silly punishment.
        This feature is designed to discourage toxicity and maintain a positive community.
        """
        punishments = ['neon clown face', 'virtual pie SPLAT!', 'holographic shame wave']
        punishment = random.choice(punishments)
        self.gotcha_list.append(f"{bully_name}: {punishment}")
        return f"Gotcha List lights up: {punishment} – Bullies squirm!"

# Usage: system = GotchaFailsSystem(); print(system.add_fail('epic faceplant')); print(system.gotcha_bully('troll123'))
