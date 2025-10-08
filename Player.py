class Player:
    def __init__(self, name="Hero"):
        self.name = name
        self.hp = 100
        self.speed = 10

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