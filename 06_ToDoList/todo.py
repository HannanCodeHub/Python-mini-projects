tasks = []

def add_task():
    task = input("Enter a task: ")
    priority = int(input("Priority of your task (1-5): "))

    new_task = {
        "task": task,
        "priority": priority,
        "completed": False
    }

    tasks.append(new_task)

    print("\nYour task:", task, "has been successfully added!")
    print("Priority:", priority)


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            index,
            task["task"],
            "| Priority:",
            task["priority"],
            "| Status:",
            status
        )


def complete_task():
    show_tasks()

    if not tasks:
        return

    task_number = int(input("\nEnter task number to complete: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    task_number = int(input("\nEnter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print("Deleted:", deleted_task["task"])
    else:
        print("Invalid task number.")


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")