from Modes_manager import ModesManager
from Aichaosbrain import AIChaosBrain
from Beast_bestiary import BeastBestiary
from characters import Kate, Amya, Holly

# --- FORK EXTENSION: Add a new character ---
class Zeus:
    """
    Represents Zeus, a new guest character.
    His abilities are based on lightning and cosmic authority.
    """
    def __init__(self):
        self.name = "Zeus"
        self.trait = "Authoritative and Electric"

    def special_ability(self):
        """
        Zeus's special ability: a powerful lightning strike.
        """
        return "Zeus raises his hand! A bolt of pure lightning crashes down, electrifying the arena floor."

def run_forked_game_scenario():
    """
    Runs an extended scenario to demonstrate new forked features,
    including a new character and a new game mode.
    """
    print("--- Initializing FORKED Game ---")
    modes_manager = ModesManager()
    ai_brain = AIChaosBrain(modes_manager)
    bestiary = BeastBestiary(modes_manager, coins=30)

    # --- Start with the new character ---
    player = Zeus()

    print(f"Welcome, {player.name}! Your trait: {player.trait}")
    print(f"Initial mode: {modes_manager.current_mode}")
    print(f"Initial coins: {bestiary.coins}")
    print("-" * 20)

    # --- SCENARIO 1: DEMONSTRATE NEW CHARACTER ABILITY ---
    print("\n--- Scenario: Zeus's Special Ability ---")
    print(player.special_ability())
    print("-" * 20)

    # --- SCENARIO 2: DEMONSTRATE NEW 'DUEL' MODE ---
    print("\n--- Scenario: New 'Duel' Game Mode ---")
    # --- FORK EXTENSION: Add and switch to a new 'duel' mode ---
    modes_manager.modes.append('duel') # Add the new mode
    print(modes_manager.switch_mode('duel'))
    print(f"Current mode: {modes_manager.current_mode}")

    # Demonstrate an action within the new mode
    print("\nSimulating a parry action in duel mode...")
    # In a real implementation, you would add logic to handle 'parry'
    print("You parry the opponent's strike, creating an opening!")
    print("-" * 20)

    # --- SCENARIO 3: DEMONSTRATE EXISTING FUNCTIONALITY WITH NEW CHARACTER ---
    print("\n--- Scenario: Buying a beast as Zeus ---")
    print(f"Current coins: {bestiary.coins}")
    print("Attempting to buy a fire_serpent (base cost 14)...")
    # On medium difficulty, cost is 14
    print(bestiary.buy_beast('fire_serpent'))
    print(f"Coins remaining: {bestiary.coins}")
    print("\nAttempting to ride the new beast...")
    print(bestiary.ride_beast('fire_serpent'))


if __name__ == "__main__":
    run_forked_game_scenario()