secretNumber = 9
numberOfAttempts = 0
attemptLimit = 3

while numberOfAttempts < attemptLimit:
    guessedNumber = int(input("Guess a number between 0 and 10: "))
    numberOfAttempts += 1
    if guessedNumber == secretNumber:
        print("You won!")
        break
    else:
        print("Your guess was incorrect - You have " + str(attemptLimit - numberOfAttempts) + (" attempts left."))
else:
    print("You lost!")