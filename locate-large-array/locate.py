print("""Here is an array:
2
3
45
12
234
5
6
789
and the largest number in the array is....""")


numbers = [2,3,45,12,234,5,6,789]       # The Array
start = numbers[0]                      # Like a building with 789 floors there must be a starting floor. 2 in numbers is the starting floor of the array.
for largest in numbers:                 # We are reffering to largest within "numbers"
    if largest > start:                 # If largest is greater than the starting floor(2)
        start=largest                   # Then the starting floor(2) will equal the largest(789)
print(start)                            # We are now printing "start(s)" new assigned number(789)
