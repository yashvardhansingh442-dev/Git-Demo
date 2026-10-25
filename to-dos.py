todos = []

while True:
    choice = input("1. Add  2. View  3. Exit: ")

    if choice == "1":
        todos.append(input("Enter task: "))

    elif choice == "2":
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

    elif choice == "3":
        break