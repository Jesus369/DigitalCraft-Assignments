print("Enter a number to see the factorial")
number = int(raw_input(""))
factorial = 1


if number < 0:
  print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The number " + str(number) + " has a factorial of:")
    for i in reversed(range(number + 1)):
        factorial = factorial * i
        i = i - 1
        print(factorial)


    # print("The factorial of " + str(number) + " is " + str(factorial))
