class Player:
    def __init__(self, name="Hero"):
        self.name = name
        self.hp = 100
        self.speed = 10
        self.xp_rate = 1.0  # 1.0 is normal, 1.1 is a 10% bonus
        self.has_learned_colors = False

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        return f"{self.name} takes {amount} damage! HP is now {self.hp}."

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
        return f"{self.name} heals for {amount} HP! HP is now {self.hp}."

    def increase_speed(self, amount):
        self.speed += amount
        return f"{self.name}'s speed increases by {amount}! Speed is now {self.speed}."

    def decrease_speed(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        return f"{self.name}'s speed decreases by {amount}! Speed is now {self.speed}."

    def increase_xp_rate(self, rate_increase):
        self.xp_rate += rate_increase
        return f"{self.name}'s XP rate increased to {self.xp_rate:.2f}x."

    def decrease_xp_rate(self, rate_decrease):
        self.xp_rate -= rate_decrease
        return f"{self.name}'s XP rate decreased to {self.xp_rate:.2f}x."