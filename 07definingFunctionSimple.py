def greet_user(firstName, lastName): #placeholder/variable called parameter
    print(f"""
    Hi, {firstName} {lastName}
    Welcome aboard!
    """)


def square(number):
    return number * number


def emojiConverter(message):
    words = message.split(" ")
    emojis = {
    ":)": "*smileyface*",
    ":(": "*sadface*",
    ";...;": "*batface*"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


inputName = input("What's your first and last name?: ")
userName = inputName.split(" ")
print("Start")
print(inputName)
print(userName)
greet_user(lastName=userName[1], firstName=userName[0]) #variable called argument - positional argument pre-defined into keyword arguments, also showing what the arguments represent to other readers of the code
print("Finish")


inputNumber = float(input("Enter a number: "))
resultOfOperation = square(inputNumber)
print(f"The square of {inputNumber} is {resultOfOperation}")


print(emojiConverter(input("Write a message: ")))