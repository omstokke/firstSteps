carState = 0

while True:
    userInput = input("Enter command (or enter 'help' for list of commands): ").lower() #calling the .lower-method removing the need to repeat it on every userInput variable
    if userInput == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the car
        """)
    elif userInput == "start" and carState == 0:
        print("The car starts.")
        carState = 1
    elif userInput == "start" and carState == 1:
        print ("The car is already running.")
    elif userInput == "stop" and carState == 0:
        print ("The engines are already off.")
    elif userInput == "stop" and carState == 1:
        print ("The car stops and the engines are turned off.")
        carState = 0
    elif userInput == "quit":
        break
    else:
        print("Please enter one of the commands listed under 'help'")