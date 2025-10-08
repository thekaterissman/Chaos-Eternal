import random

class ReputationEngine:
    def __init__(self):
        self.honor_points = 0
        self.chaos_points = 0
        self.deeds_log = []

    def record_deed(self, deed_type, amount, description):
        """
        Records a deed, affecting the player's reputation.
        deed_type: 'honorable' or 'chaotic'
        amount: The number of points to add.
        description: A string describing the deed.
        """
        if deed_type == 'honorable':
            self.honor_points += amount
        elif deed_type == 'chaotic':
            self.chaos_points += amount
        else:
            return "Invalid deed type. Your actions are meaningless."

        self.deeds_log.append(f"{deed_type.capitalize()} deed: {description} (+{amount} points)")
        return f"Your reputation shifts... You performed a(n) {deed_type} deed."

    def get_reputation(self):
        """
        Calculates and returns a reputation title based on honor and chaos points.
        """
        total_deeds = self.honor_points + self.chaos_points

        if total_deeds == 0:
            return "Unknown (A blank slate)"

        honor_ratio = self.honor_points / total_deeds

        if honor_ratio > 0.8 and self.honor_points > 10:
            return "Noble Hero (A beacon of light)"
        elif honor_ratio > 0.6:
            return "Valiant Knight (Respected and honorable)"
        elif honor_ratio > 0.4:
            return "Chaotic Good (An unpredictable savior)"
        elif honor_ratio > 0.2:
            return "Chaotic Mercenary (Your only allegiance is to coin)"
        elif self.chaos_points > 10:
            return "Dreaded Tyrant (A scourge upon the land)"
        else:
            return "Wandering Soul (Your path is yet undecided)"

    def get_status(self):
        title = self.get_reputation()
        return f"Reputation: {title}\nHonor Points: {self.honor_points}\nChaos Points: {self.chaos_points}"

# --- Example Usage ---
# reputation = ReputationEngine()
# print(reputation.get_status())
# print(reputation.record_deed('honorable', 10, "Defeated the Shadow Beast"))
# print(reputation.record_deed('honorable', 15, "Saved the village from a raid"))
# print(reputation.record_deed('chaotic', 5, "Looted the ancient tomb for personal gain"))
# print(reputation.get_status())