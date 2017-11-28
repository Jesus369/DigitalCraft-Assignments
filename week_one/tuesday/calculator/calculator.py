import functions

print("""Welcome to your calculator
Here are your functions:
q = +
w = -
e = *
r = /""")

print("Enter your first number")
first = int(raw_input(""))

print("Enter your operand")
operand = raw_input("")

print("Enter your second number")
second = int(raw_input(""))

if operand == "q":
    print("Answer:")
    print(functions.add(first,second))
if operand == "w":
    print("Answer:")
    print(functions.subtract(first,second))
if operand == "e":
    print("Answer:")
    print(functions.multiply(first,second))
if operand == "r":
    print("Answer:")
    print(functions.divide(first,second))
