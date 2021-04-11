numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phoneNumber = input("Enter your phone no.: ")
phoneConverted = ""
for i in phoneNumber:
    phoneConverted += numbers.get(i, "*pause*") + " "
print(phoneConverted)

message = input(">")
words = message.split(" ")

emojis = {
    ":)": "*smileyface*",
    ":(": "*sadface*",
    ";..;": "*batface"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " " #skips conversion from dictionary by returning input if not a key/value-pair
print(output)