print("Enter a word to see if it is palindrome!")

word = raw_input("")

# Slicing - reversing the entered word to see if it matches the entered word still.
if word != word[::-1]:
    print("This is not palindrome!")
elif word == word[::-1]:
    print("This is palindrome!")
