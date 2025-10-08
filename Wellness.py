import random

class Wellness:
    def __init__(self):
        pass

    def breathing_exercise(self):
        return "Haptic suit pulses gently. A calm voice guides you: 'Breathe in... hold... breathe out.' The air shimmers."

    def sound_therapy(self):
        sounds = ['crystal bowls', 'Tibetan gongs', 'binaural beats']
        sound = random.choice(sounds)
        return f"A wave of {sound} washes over you. Your mind clears. The arena floor hums with peace."

    def cleansing(self):
        return "A holographic waterfall of light washes over you, cleansing away the chaos. You feel refreshed and renewed."

    def meditation(self):
        return "The world fades to a soft glow. The AI's voice is a gentle whisper, guiding you to a state of deep calm. Your thoughts settle like dust, and you find a new level of focus."

# Usage:
# wellness = Wellness()
# print(wellness.breathing_exercise())
# print(wellness.sound_therapy())
# print(wellness.cleansing())
# print(wellness.meditation())
