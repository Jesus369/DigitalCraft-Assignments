phonebookDict ={"Alice": "703-493-1834",
                "Bob": "857-384-1234",
                "Elizabeth": "857-384-1234"}

# Printing Key name - Elizabeth's value
print("This is Elizabeth's phone number: " + phonebookDict["Elizabeth"])

# Appending to a dictionary
# dictionary    Key         Value
phonebookDict["Kareem"] = "938-489-1234"

# Deleting a key from the dictionary using the "del" function.
del(phonebookDict["Alice"])

# Changing a key's value to a new one
phonebookDict["Bob"] = "968-345-2345"

# Printint all phone entries
print(phonebookDict)
