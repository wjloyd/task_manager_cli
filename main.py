print("Welcome to the Task Manager CLI!")

while True:
	print("\nMenu:")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Exit")

	choice = input("Enter your choice 1-3: ")

	if choice == "1":
		print("You choose to add a task.")
	elif choice == "2":
		print("You choose to view tasks.")
	elif choice == "3":
		print("Goodbye")
		break
	else:
	 	print("Invalid input. Please enter 1, 2, or 3") 		 