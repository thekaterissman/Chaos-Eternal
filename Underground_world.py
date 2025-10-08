# Underground_world.py - Defines the exclusive, premium-only underground world.

class UndergroundWorld:
    """
    Contains the descriptions and logic for the exclusive underground areas,
    accessible only to premium members. The descriptive text is designed to
    simulate a rich VR and haptic experience.
    """
    def __init__(self):
        """
        Initializes the Underground World.
        """
        self.current_location = None
        print("Underground world created. Access is restricted.")

    def enter_world(self):
        """
        Provides the initial entry description for the underground world.
        """
        self.current_location = "hub"
        return (
            "HAPTICS: A low, bass-heavy vibration hums through your suit as a hidden door slides open. "
            "The air grows cool and smells of ozone and damp earth. You have entered the Underground."
        )

    def explore_location(self, location_name):
        """
        Provides a detailed, immersive description of a specific location within the underground world.

        Args:
            location_name (str): The name of the location to explore ('rave', 'forest', 'racetrack').

        Returns:
            str: The descriptive text for the location.
        """
        if location_name == 'rave':
            self.current_location = 'rave'
            return (
                "RAVE: The bass intensifies, syncing with your heartbeat until you can't tell the difference. "
                "HAPTICS: The floor vibrates with a life of its own. Neon flora pulses in time with the music, "
                "casting shifting, electric-blue patterns on the cavern walls. A crowd of avatars, their "
                "outfits glowing, moves as one. The energy is infectious."
            )
        elif location_name == 'forest':
            self.current_location = 'forest'
            return (
                "FOREST: You step out of the rave cavern into a vast, bioluminescent forest. The air is cool and "
                "alive with the chirps of unseen, holographic creatures. HAPTICS: A gentle breeze, carrying the "
                "scent of glowing moss, brushes against your skin. The long stretch of woods is lit by towering, "
                "pulsing mushrooms and floating spores that glitter like dust in a moonbeam."
            )
        elif location_name == 'racetrack':
            self.current_location = 'racetrack'
            return (
                "RACETRACK: You arrive at a sleek, subterranean racetrack. The track is a ribbon of pure light, "
                "twisting through glowing crystal formations. HAPTICS: The low growl of high-performance vehicles "
                "vibrates in your chest. The air crackles with competitive energy. This is where legends are made."
            )
        else:
            return "That location is not on the map of the Underground."

    def get_current_location(self):
        """
        Returns the player's current location in the underground world.
        """
        return self.current_location