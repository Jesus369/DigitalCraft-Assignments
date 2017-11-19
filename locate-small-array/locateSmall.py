print("""Here is an array:
2
3
45
12
234
5
6
789
The smallest number in the array is....""")

numbers = [2, 3, 45, 12, 234, 5, 6, 789]    # The array of numbers.
largest = numbers[7]                        # The largest number starts at 7(789).
for smallest in numbers:                    # For the smallest number is numbers.
    if smallest < largest:                  # If the smallest number is less than the largest nuumber(789)
        smallest != largest                 # The smallest number does not equal the largest number.
    print(smallest)                         # Print the smallest number.
    break
