# Player_account.py - Manages player account data, including premium status.

class PlayerAccount:
    """
    Manages the player's account details, such as their premium status.
    This class will hold data that is specific to the player's account
    rather than their in-game character state.
    """
    def __init__(self, username="Player1"):
        """
        Initializes the player account.

        Args:
            username (str): The player's username.
        """
        self.username = username
        self.premium_status = False
        print(f"Player account '{self.username}' created with standard access.")

    def upgrade_to_premium(self):
        """
        Upgrades the player's account to premium status.
        """
        if not self.premium_status:
            self.premium_status = True
            print(f"Account '{self.username}' has been upgraded to PREMIUM status!")
            return "Welcome to the elite. The underground awaits."
        else:
            return "You are already a premium member."

    def has_premium(self):
        """
        Checks if the player has premium status.

        Returns:
            bool: True if the player has premium, False otherwise.
        """
        return self.premium_status