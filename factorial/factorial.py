downTheLine = [1, 2, 3, 4, 5, 6, 7, 8]
for reverse in reversed(range(len(downTheLine))):
    total = reverse * downTheLine[-1]
    print total

add = -1
multBack = [1, 2, 3, 4, 5, 6, 7, 8]
for back in range(len(multBack),0,-1):
    mult = back * multBack[-1]
    print mult



input_number = int(raw_input("Enter your number: "))
for index in range(1, input_number+1):
    mult_back = index * input_number
    print(mult_back)
