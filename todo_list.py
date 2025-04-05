tasks = []

while True:
    print("\n📋 To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == '3':
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")
