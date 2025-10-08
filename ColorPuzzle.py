from Player import Player

class ColorPuzzle:
    def __init__(self, player: Player):
        self.player = player
        self.puzzle_description = "You stand before three pedestals, each glowing with a faint, colorless light. To perceive the world in its true form, you must arrange the primary essences in the correct order. The essences are of Red, Green, and Blue."
        self.solution = ["Red", "Green", "Blue"]
        self.is_solved = False

    def get_description(self):
        return self.puzzle_description

    def attempt_solution(self, sequence):
        if self.is_solved:
            return "The puzzle is already solved. You can see the colors of the world."

        if sequence == self.solution:
            self.is_solved = True
            self.player.has_learned_colors = True
            return "As you place the essences in order, a wave of vibrant color washes over you. You have unlocked the perception of color!"
        else:
            return "The essences dim, the order is incorrect. The world remains in shades of gray."