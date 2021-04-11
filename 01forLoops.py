prices = range(10, 111, 10)

sum = float(0)

for i in prices:
    sum += float(i)
    print(f"Price: {i} Current sum: {sum}")

print(f"Total: {sum}")