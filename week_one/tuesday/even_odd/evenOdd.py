even = range(0,101,2)
odd = range(1,100,2)

print("""Enter a number from 1 - 100.
You will be notified if the number entered is even or odd.""")

number = int(raw_input(""))

 if number in even:
     print("This is an even numer!")
 if number in odd:
     print("This is an odd number!")
 else:
     print("This isn't a number from 1 - 100!")

# Or the following can be used to determine for ANY number if even or odd. If the number when divided by 2 has a remainder of 0 then it is an even number
# Otherwise it is an off number

if number % 2 == 0:
    print("This is even")
else:
    print("This is odd!")
