import random


class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.rolls = []

    def roll(self):
        roll = random.randint(1, self.sides)
        print("You rolled a: %s" % roll)
        self.rolls.append(roll)

    def get_average(self):
        length = len(self.rolls)
        avg = (sum(self.rolls) / length)
        print("the average roll is: %s across %s rolls" % (avg, length))
        input("Press Enter to Continue\n")


dice = {
    "d6- six sides": Dice(6),
    "d12- twelve sides": Dice(12),
    "d20- twenty sides": Dice(20)
}


def choose_dice():
    for d in dice:
        print(f"{d}")
    choice = input(
        "Please select a dice game to roll. Or enter a 0 to exit program!\n")
    return choice


def start():
    playing = True
    while playing:
        dice_name = choose_dice()
        if dice_name == "0":
            playing = False
        elif dice_name not in dice:
            print("Please select a dice from the list.")
        else:
            selected_dice = dice[dice_name]
            print("You have selected %s" % dice_name)
            selected_dice.roll()
            selected_dice.get_average()


start()
