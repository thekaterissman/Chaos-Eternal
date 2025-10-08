import random

class CrowdDynamics:
    """
    Manages the crowd's mood and generates dynamic reactions to in-game events.
    This system makes the arena feel alive and responsive to the player's actions.
    """
    def __init__(self):
        """
        Initializes the Crowd Dynamics system.
        - mood: The current mood of the crowd, which influences their reactions.
        """
        self.mood = 'neutral' # Can be 'neutral', 'excited', 'tense', 'disappointed'

    def update_mood(self, event):
        """
        Updates the crowd's mood based on a significant game event.
        """
        if event in ['critical_hit', 'flawless_victory']:
            self.mood = 'excited'
        elif event in ['near_death', 'sudden_twist']:
            self.mood = 'tense'
        elif event in ['player_fail', 'missed_attack']:
            self.mood = 'disappointed'
        else:
            self.mood = 'neutral'

    def get_reaction(self, event):
        """
        Generates a descriptive text reaction based on the current event and crowd mood.
        - event: The specific action that occurred (e.g., 'critical_hit', 'dodge').
        """
        self.update_mood(event) # Mood shifts before they react

        reactions = {
            'excited': {
                'critical_hit': [
                    "A roar erupts from the stands as the blow connects with a sickening crunch!",
                    "The crowd is on its feet, screaming your name!",
                    "Flashes of light from the stands illuminate the arena as the crowd goes wild!"
                ],
                'flawless_victory': [
                    "The stadium is shaking! They can't believe what they just saw!",
                    "Chants of your name echo, a deafening wave of adoration!",
                    "A sea of holographic signs with your face on them floods the stands!"
                ]
            },
            'tense': {
                'near_death': [
                    "A collective gasp sucks the air out of the arena. Every eye is wide with shock.",
                    "The crowd is dead silent, leaning forward in their seats, knuckles white.",
                    "Whispers spread like wildfire... 'Is this the end?'"
                ],
                'sudden_twist': [
                    "A wave of murmurs washes over the crowd as they try to process the sudden turn of events.",
                    "You can feel thousands of eyes on you, a heavy weight of expectation and uncertainty.",
                    "The odds board flickers erratically, and the betting is suspended. No one knows what happens next."
                ]
            },
            'disappointed': {
                'player_fail': [
                    "A wave of groans washes over the arena. A few boos are audible.",
                    "Someone in the front row throws a holographic tomato that splatters harmlessly at your feet.",
                    "The energy in the stadium deflates, the roar replaced by a collective sigh."
                ],
                'missed_attack': [
                    "The crowd winces in unison as your attack hits nothing but air.",
                    "A few jeers echo from the upper decks.",
                    "Someone yells, 'My grandmother could fight better than that!'"
                ]
            },
            'neutral': {
                'default': [
                    "The crowd watches intently, their faces a mix of curiosity and bloodlust.",
                    "The low hum of thousands of conversations provides a constant backdrop to the fight.",
                    "Holographic advertisements flicker above the stands, momentarily distracting a few spectators."
                ]
            }
        }

        # Get a reaction from the appropriate mood and event, or a default one
        reaction_list = reactions.get(self.mood, {}).get(event)
        if not reaction_list:
            reaction_list = reactions['neutral']['default']

        return f"[CROWD] {random.choice(reaction_list)}"