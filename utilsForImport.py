import random

def findMax(x):
    try:
        highestNumber = float(x[0])
        for i in x:
            if i > highestNumber:
                highestNumber = i
        return highestNumber
    except ValueError:
        print("Input needs to be a list of numbers")


class Dice:
    def rollDice(self):
        return (random.randint(1, 6), random.randint(1, 6))