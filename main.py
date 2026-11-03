import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    show_tasks(tasks)
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Task number does not exist.")
    except ValueError:
        print("Please enter a valid number.")
