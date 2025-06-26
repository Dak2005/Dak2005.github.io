# todo_list.py

# Initialize an empty list to store tasks
tasks = []
def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task['done'] else "❌"
            print(f"{i}. [{status}] {task['title']}")
def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    print("Task added successfully.")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()


