tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

while True:
    print("\nTo-Do List:")
    view_tasks()
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        index = int(input("Enter task number to mark as completed: ")) - 1
        mark_completed(index)
    elif choice == "3":
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")
