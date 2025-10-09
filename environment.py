import random

class Environment:
    """
    Manages the game's environmental conditions, including time of day,
    weather, and their effects on the game world.
    """
    def __init__(self):
        self.hour = 8  # Start at 8 AM (0-23)
        self.weather = "clear"  # e.g., "clear", "rainy", "stormy"
        self.wind_speed = 0  # Represents wind intensity, affects movement

    def advance_time(self, hours=1):
        """Advances the game time by a given number of hours."""
        self.hour = (self.hour + hours) % 24

    def get_time_of_day(self):
        """Returns the current period of the day as a string."""
        if 5 <= self.hour < 12:
            return "morning"
        elif 12 <= self.hour < 17:
            return "afternoon"
        elif 17 <= self.hour < 21:
            return "evening"
        else:
            return "night"

    def get_description(self):
        """
        Returns a string describing the current environmental conditions.
        """
        time_of_day = self.get_time_of_day()
        return f"It is {time_of_day}. The weather is {self.weather} with a wind speed of {self.wind_speed}."

    def update(self):
        """
        Updates the environment. For now, this advances time by 1 hour.
        """
        self.advance_time()