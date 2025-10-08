import random

class WorldEvents:
    """
    Manages random world events that can occur during gameplay.
    These events are designed to add surprise and unpredictability to the game,
    making the world feel more alive and chaotic.
    """
    def __init__(self):
        """
        Initializes the World Events manager.
        - events: A list of possible world events, each with a description and effect.
        """
        self.events = [
            {'name': 'cosmic_aurora', 'description': 'A vibrant cosmic aurora fills the sky, boosting all players\' morale.', 'effect': 'xp_boost'},
            {'name': 'market_day', 'description': 'A bustling market appears in the lobby, offering rare items for a limited time.', 'effect': 'special_vendor'},
            {'name': 'beast_migration', 'description': 'A herd of majestic beasts stampedes through the arena, creating a temporary obstacle course.', 'effect': 'arena_hazard'}
        ]

    def trigger_random_event(self):
        """
        Triggers a random world event from the list of possible events.
        Returns the event's data so the main game loop can apply its effects.
        """
        event = random.choice(self.events)
        return event