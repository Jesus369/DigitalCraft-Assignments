print("""Start entering tasks!
If you ever get lost just use the following functions:
View List: "1"
Continue: "2"
Exit Notepad: "3"
""")

class ToDoList(object):
	def __init__(self):
		self.list = []														# An empty array to hold the To-Do list.
		self.insert = raw_input("Enter a task:\t")							# .insert will hold a user input function. Can come in handy to accessing it while in the loop.			

enlisted = ToDoList()														# enlisted will equal to ToDoList and hold all of its contents
forSure = enlisted.insert													# forSure will carry the function "insert" which is accessible through enlisted

numb_func = ["1", "2", "3"]													# number functions for the user.
view_list = "1"
cont_list = "2"
exit_notes = "3"

while True:																	# A while loop to start the loop of the 3 questions we'll be asking the user
	enlisted.list.append(forSure)											# forSure which carries the function/method within "enlisted.insert" will ask the user to enter a task and will append(add) the entered task to enlisted.list
	pass																	# Information will be carried onto the next while loop.

	while True:																# A last while loop.
		user_input2 = raw_input("VIEW LIST(1) CONTINIUE(2) EXIT(3)\t")		# Provide the user there function options.	
		if user_input2.lower() == numb_func[0]:								# if the "user_input2" equals to the first value of our "numb_func"
			print(enlisted.list)											# Then "enlisted.list" will print which will contain our list of ToDo's.

		elif user_input2.lower() == numb_func[1]:							# But if "user_input2" equal to the second value of "numb_func"
			user_input3 = raw_input("Enter a task:\t")						# Then "user_input3", which prompts the user to enter another task will appear.
			enlisted.list.append(user_input3)								# We will then append what the user types onto "enlisted.list"

		elif user_input2.lower() == numb_func[2]:							# But if "user_input2" is equal to the third value of "numb_func2"
			break															# The loop will break. Very important since we need to give the user the option end the app.
		else:																# But if neither of the "numb_func's" have been selected.....
			print("Not a valid answer")										# The user will recieve an error message
			pass															# This is a loop so since we are still within the second "while True" statement then we must allow the user entered information to be stored and passed again. After this point the loop restarts itself

	if user_input2.lower() == numb_func[2]:									# We are now outside the second stated "while True" loop and back into the first one. For assurance we are telling python that if
		break																# "user_input2" does equal to the third value of "numb_func" then loop as a whole will end, which will break the first stated "while True" loop


