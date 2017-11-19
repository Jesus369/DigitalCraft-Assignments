word = raw_input("Is it palindrome?")
print("You input {0}".format(word))



rev_word = ""
for index in range(len(word)-1,-1,-1):
    rev_word += word[index]

print(rev_word)

if rev_word.lower == word.lower():
    print("{0} is a palindrome!".format(word.title))
else:
    print ()
