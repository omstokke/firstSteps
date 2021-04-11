#Modules - files where you store your re-usable code
#Packages - directories/folders of several modules that belong together
#Start all packages with one module named __init__.py - This file let's your IDE know the folder is a Python package
#Then you can add modules with thematically ordered re-usable code
# Example of importing
# from package.module import function1, function2, function3 - this will import specific function that can be called directly as function1()
# from package import module1, module2 - this will import all the functions of the modules to be called as module1.function1()
# import package - this will import everything in the package, to be called as package.module1.function1()

#Modules already built-in, standard library: Python 3 module index
#Check the importet module to see which built-in module allows RNG

import utilsForImport as utils

listOfNumbers = [2, 5, 4, 6, 5, 9, 11, 2]
listOfNames = ["Jon", "Ole", "Ida", "Maggi"]

print(utils.findMax(listOfNumbers))
print(utils.findMax(listOfNames))

while True:
    command = input("Would you like to roll the dice (y/n)?: ").lower()
    if command == "y":
        diceToss = utils.Dice()
        print(diceToss.rollDice()) 
    else:
        break

#Search for open source packages at https://pypi.org