class Character():
    def __init__(self, name, position, speed=10, health=100, attack_power=5):
        self.name = name
        self.health = health
        self.speed = speed
        self.position = position
        self.attack_power = attack_power

    def attack(self, char):
        char.health -= self.attack_power

    def move(self, dir):
        if dir == "right":
            self.position["x"] += self.speed
        elif dir == "left":
            self.position["x"] -= self.speed
        elif dir == "up":
            self.position["y"] -= self.speed
        elif dir == "down":
            self.position["y"] += self.speed


class Player(Character):
    def heal(self):
        self.health += 25


class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 50
        self.speed = 4

    def roll(self):
        self.position["x"] -= 25


enemy1 = Enemy("Bad Guy", {"x": 20, "y": 100})
player1 = Player("Ally", {"x": 10, "y": 200}, 140, 1000, 35)
# print(player1.position)
# player1.heal()
# enemy1.roll()
# print(player1.attack())
# print(player1.health)
# print(enemy1.speed)
# print(enemy1.attack(player1))
# print(player1.health)

player1.attack(enemy1)
print(enemy1.health)
