def multiply(x,y):
    return(x * y)

print("How much did you pay for your services?:")
first = (int(raw_input("")))
print("Enter percent of amount you'd wish to tip:")
second = (int(raw_input("")))

# Converting the users second number into a decimal
percent = float(second) / 100

tip = multiply(first,percent)
print("Your tip amount is:  " + str(tip)) +"0."

tot_pay = first + tip
print("Your total amount to pay for the serving plus tip will be:   " + str(tot_pay) + "0.")
