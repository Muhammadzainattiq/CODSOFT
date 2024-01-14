import json
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['date']}")

def add_task():
    title = input("Enter task title: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {'title': title, 'date': date}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task():
    tasks = load_tasks()
    display_tasks(tasks)
    
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter the new task title: ")
            tasks[index]['title'] = new_title
            tasks[index]['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
