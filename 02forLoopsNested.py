xCount = 4
yCount = 4
for x in range (xCount):
    for y in range (yCount):
        print(f"({x}, {y})")

fNumbers = [5, 2, 5, 2, 5]
for n in fNumbers:
    printRow = ""
    for i in range (n):
        printRow += "x"
    print(printRow)