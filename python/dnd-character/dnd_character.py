import random
import math
def modifier(constitution):
    return math.floor((constitution-10)/2.0)

def dice_roll():
    dice = []
    for i in range(4):
        dice.append(random.randint(1,6))
    dice.remove(min(dice))
    return sum(dice)
        
class Character:
    def __init__(self):
        self.strength = dice_roll()
        self.dexterity = dice_roll()
        self.constitution = dice_roll()
        self.intelligence = dice_roll()
        self.wisdom = dice_roll()
        self.charisma = dice_roll()
        self.constitution_modifier = math.floor((self.constitution - 10) / 2.0)
        self.hitpoints = self.constitution_modifier + 10

    def ability(self):
        return random.choice([self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma])
