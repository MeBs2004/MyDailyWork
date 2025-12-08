# To-Do App
def task():
    tasks = []  # Empty list
    print("Welcome to the Task Management App")

    try:
        total_tasks = int(input("Enter how many tasks you want to add = "))
    except ValueError:
        print("Invalid number! Starting with 0 tasks.")
        total_tasks = 0

    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks: {tasks}")

    while True:
        print("\nChoose an operation:")
        operation = input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\nEnter choice = ")

        # ADD TASK
        if operation == "1":
            add_task = input("Enter task you want to add = ")
            tasks.append(add_task)
            print(f"Task '{add_task}' successfully added!")

        # UPDATE TASK
        elif operation == "2":
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                index = tasks.index(updated_val)
                tasks[index] = new_task
                print(f"Task updated from '{updated_val}' to '{new_task}'")
            else:
                print("Task not found!")

        # DELETE TASK
        elif operation == "3":
            del_val = input("Which task do you want to delete = ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted!")
            else:
                print("Task not found!")

        # VIEW ALL TASKS
        elif operation == "4":
            print("\nYour current tasks:")
            if len(tasks) == 0:
                print("No tasks available!")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        # EXIT
        elif operation == "5":
            print("Closing the program... Goodbye!")
            break

        else:
            print("Invalid Input! Enter a number between 1–5.")

# Run the To-Do App
task()