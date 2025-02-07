import json

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print(f'Task "{title}" added!')

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{idx}. {task['title']} [{status}]")

# Update task status
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_idx = int(input("Enter task number to mark as complete: ")) - 1
        tasks[task_idx]["completed"] = True
        print(f'Task "{tasks[task_idx]["title"]}" marked as complete!')
    except (IndexError, ValueError):
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_idx = int(input("Enter task number to delete: ")) - 1
        removed_task = tasks.pop(task_idx)
        print(f'Task "{removed_task["title"]}" deleted!')
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
