print("""If a number is divisible by 3 then it's Fizz
If divisible by 5 then it's Buzz
If by both 3 and 5 then it's FizzBuzz!""")
print("Enter a number:")
number = int(raw_input(""))

if number % 5 == 0 and number % 3 == 0:
    print("Fizz-Buzz!")
elif number % 3 == 0:
     print("Fizz!")
elif number % 5 == 0:
     print("Buzz!")
