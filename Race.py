from Player import Player

class Race:
    def __init__(self, player: Player):
        self.player = player
        self.obstacles = [
            {"description": "A wide chasm blocks your path! You need at least 12 speed to jump it.", "type": "stat_check", "stat": "speed", "value": 12},
            {"description": "A series of sharp turns ahead! You must choose the right path: 'left' or 'right'.", "type": "choice", "correct_choice": "right"},
            {"description": "A final straightaway to the finish line! A speed boost would be helpful here.", "type": "open"}
        ]
        self.current_obstacle_index = 0
        self.is_complete = False

    def start_race(self):
        self.current_obstacle_index = 0
        self.is_complete = False
        return "The race has begun! " + self.get_current_obstacle()

    def get_current_obstacle(self):
        if self.is_complete or self.current_obstacle_index >= len(self.obstacles):
            return "You have finished the race!"
        return self.obstacles[self.current_obstacle_index]["description"]

    def navigate_obstacle(self, action=None):
        if self.is_complete:
            return "The race is already over."

        obstacle = self.obstacles[self.current_obstacle_index]

        success = False
        if obstacle["type"] == "stat_check":
            if getattr(self.player, obstacle["stat"]) >= obstacle["value"]:
                success = True
        elif obstacle["type"] == "choice":
            if action == obstacle["correct_choice"]:
                success = True
        elif obstacle["type"] == "open":
            success = True

        if success:
            self.current_obstacle_index += 1
            if self.current_obstacle_index >= len(self.obstacles):
                self.is_complete = True
                return "You've passed the final obstacle and won the race! Congratulations!"
            return "You've successfully passed the obstacle! " + self.get_current_obstacle()
        else:
            # For simplicity, failing an obstacle just ends the race in this version.
            self.is_complete = True
            return "You failed to overcome the obstacle and lost the race."

    def get_reward(self):
        if self.is_complete and self.current_obstacle_index >= len(self.obstacles):
            reward_amount = 100
            return f"You receive {reward_amount} XP as a reward for winning the race!", reward_amount
        return "No reward to give.", 0