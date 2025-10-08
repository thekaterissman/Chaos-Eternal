import random

class LightTherapyManager:
    """
    Manages the Light Therapy mode, providing creative and reflective actions
    based on light and color.
    """
    def create_with_light(self, color="white"):
        """
        Generates a message for creating something with a specific color of light.
        """
        creations = [
            "a shimmering bridge",
            "a delicate, glowing flower",
            "a pulsating orb of energy",
            "a silent, watching sentinel",
            "a swirling vortex of particles",
        ]
        return f"You weave {color} light into the form of {random.choice(creations)}. The air hums with gentle energy."

    def reflect_on_aura(self):
        """
        Generates a message for a reflective action based on the player's aura.
        """
        auras = [
            "a warm, golden radiance, full of courage",
            "a cool, blue calm, like a still lake",
            "a vibrant, green energy, teeming with life",
            "a soft, violet glow, hinting at deep wisdom",
            "a chaotic, sparkling energy, full of potential",
        ]
        return f"You look inward, sensing your aura. It is {random.choice(auras)}."

    def get_light_therapy_actions(self):
        """
        Returns a list of suggested actions for the Light Therapy mode.
        """
        return [
            "Create with golden light",
            "Create with blue light",
            "Reflect on your inner aura",
            "Breathe in the light",
        ]