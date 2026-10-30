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

