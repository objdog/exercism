# Score categories
# Change the values as you see fit
def is_full_house(dice):
    result = True
    for i in dice:
        if dice.count(i) == 4:
            return 0
    if len(set(dice)) == 1:
        return 0
    elif len(set(dice)) == 2:
        return sum(dice)
    else:
        return 0

def is_four_of_kind(dice):
    for i in dice:
        if dice.count(i) >= 4:
            return i * 4
        else:
            return 0
def is_little_straight(dice):
    if sorted(dice) == [1,2,3,4,5]:
        return 30
    else: 
        return 0
        
def is_big_straight(dice):
    if sorted(dice) == [2,3,4,5,6]:
        return 30
    else:
        return 0
        
def sum_dice(dice, value):
    return sum(i for i in dice if i == value)
    
def score(dice, category):
    return category(dice)    
    
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum_dice(dice, 1)
TWOS = lambda dice: sum_dice(dice, 2)
THREES = lambda dice: sum_dice(dice, 3)
FOURS = lambda dice: sum_dice(dice, 4)
FIVES = lambda dice: sum_dice(dice, 5)
SIXES = lambda dice: sum_dice(dice, 6)
FULL_HOUSE = is_full_house
FOUR_OF_A_KIND = is_four_of_kind
LITTLE_STRAIGHT = is_little_straight
BIG_STRAIGHT = is_big_straight
CHOICE = lambda dice: sum(dice)


    

