class Quest:
    """
    Defines a multi-stage quest that players can undertake.
    """
    def __init__(self, name, stages, reward):
        self.name = name
        self.stages = stages
        self.reward = reward
        self.current_stage_index = 0
        self.is_complete = False

    def get_current_stage_description(self):
        """Returns the description of the current quest stage."""
        if not self.is_complete:
            return self.stages[self.current_stage_index]['description']
        return "You have already completed this quest."

    def attempt_to_advance(self, activity):
        """
        Checks if the performed activity completes the current stage and advances the quest.
        Returns a message indicating the result.
        """
        if self.is_complete:
            return None # No message if quest is already done

        required_activity = self.stages[self.current_stage_index]['activity']
        if activity == required_activity:
            self.current_stage_index += 1
            if self.current_stage_index >= len(self.stages):
                self.is_complete = True
                return f"Quest Complete! {self.reward}"
            else:
                next_stage_description = self.get_current_stage_description()
                return f"You have advanced the quest! Your next task: {next_stage_description}"
        return None


# --- Sample Quest Definitions ---

celestial_armor_quest = Quest(
    name="The Quest for the Celestial Armor",
    stages=[
        {
            'description': "A symbol has appeared in your mind's eye. Meditate to decipher its meaning.",
            'activity': 'meditate'
        },
        {
            'description': "The symbol resonates with a specific frequency. Use sound therapy to attune to it.",
            'activity': 'sound_therapy'
        },
        {
            'description': "The frequency has revealed a hidden inscription. Cleanse yourself to read the ancient text.",
            'activity': 'cleanse'
        }
    ],
    reward="The stars bestow upon you the Celestial Armor! It shimmers with cosmic light, protecting you from the chaos."
)

# A dictionary to hold all available quests in the game.
available_quests = {
    "celestial_armor": celestial_armor_quest,
}