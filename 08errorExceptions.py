def inputAgeAndPrint(ageInput):
    try:
        zeroCheck = 20 / ageInput
        print(f"Your age is {ageInput}")
        return zeroCheck
    except ValueError:
        print("Invalid value - Try again")
    except ZeroDivisionError:
        print("Your age cannot be 0")


while True:
    userAgeInput = int(input("What is your age?: "))
    inputAgeAndPrint(userAgeInput)