import symCalc

print("""Start your calculations!
Functions:
z = +
x = -
c = *
v = /""")

functions = ["q", "w", "e", "r"]
#userInput
while True:
    try:
        num1 = int(raw_input("Enter a number: \t"))
    except ValueError:
        print("This is not a number.")
        pass

    while True:
        while True:
            symbol = raw_input("What is your symbol:\t")
            if symbol in functions:
                break
            if symbol != functions:
                print("ERROR: Enter a valid operation function!")
                pass
        break

    while True:
        try:
            num2 = int(raw_input("Enter a number: \t"))
        except ValueError:
            print("This is not a number.")
            pass
        break


    # Definition Operations. The result of the user's operation will print
    x = num1
    y = num2

    if symbol == "q":
        print(symCalc.add(x,y))
    elif symbol == "w":
        print(symCalc.sub(x,y))
    elif symbol == "e":
        print(symCalc.mult(x,y))
    elif symbol == "r":
        print(symCalc.div(x,y))
    else:
        print("Can not process operation due to invalid function! Try again!")

    exit = raw_input('Continue your operation: Press any key for yes. Press "N" for no \t')
    if exit.lower() == "n":
        break
