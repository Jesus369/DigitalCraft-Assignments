group = ["Alex", "Mary", "Steve", "John", "Seinfield", "Alan", "Jane"]
right1 = "Steve"
right2 = "Alan"
takeAway = -1

print("Here is a list of names")
print("Alex")
print("Mary")
print("Steve")
print("John")
print("Seinfield")
print("Alan")
print("Jane")
print("Can you guess which two people spoiled Thanksgiving Potluck last year? The name will be removed by guessing correctly!\n\n")

while True:

    while True:
        while True:
            choice1 = raw_input("First name:\t")
            if choice1.lower() == right1.lower():                 # If choice1 equals right1.
                del group[2]                                      # Then option(2) from group will be deleted.
                print(group)
                break                                             # If the "if" statement is true then the loop will break.
                pass                                              # This information will be stored and pass along.

            elif choice1.lower() == right2.lower():               # But if choice1 happens to equal right2.
                del group[5]                                      # option(5) from the group will be deleted.
                print(group)
                break                                             # If the "if" statement is true then the look will break.
                pass                                              # This information will store and pass along.

            elif choice1.lower() != right1.lower():                # If choice1 does not equal right1 then the following will print. The loop will not break if the statement is not true.
                print("Wrong person! Here's the list one more time. Feel free to try again!")
            elif choice1.lower() != right2.lower():                # If choice1 does not equal right2 then the following will print. The loop will not break if the statement is not true
                print("Wrong person! Here's the list one more time. Feel free to try again!")
            print group

        break
    pass

    print("\nGreat now the next choice!\n")
    pass
    while True:
        pass
        while True:
            choice2 = raw_input("Second name: \t")
            if choice2.lower() == choice1.lower():
                print("This name has already been selected! Try again. Here's the list! \t")
                print(group)
                
            elif choice2.lower() == right1.lower():
                del group[2]
                print(group)
                break
                pass

            elif choice2.lower() == right2.lower():
                del group[4]
                print(group)
                break

            elif choice2.lower() != right1.lower():
                print("Wrong person! Here's the list one more time! Feel free to try again!")
                print(group)
            elif choice2.lower() != right2.lower():
                print("Wrong person! Heres the list one more time! Feel free to try again!")
                print(group)
            pass
        break
    break


print("\n\nPerfect! Now we'll know not to invite them to this years potluck!")


#        elif choice1.lower() == right2.lower():
#            print("Great! Now onto the next choice!")
#            break
#        else:
#            print("Try again!")
#            break
#
#choice1 = takeAway
#
#choice2 = raw_input("Awesome! Can you guess the second person?")
#if choice2.lower() == right2.lower():
#    print("Great Job! Lets erase there names!")
#else:
#    print("Try again!")
