from tabulate import tabulate

def main():
    print("\n--- Daily Grind - To-Do List ---")
    tasks, task_number = [], 0

    while True:
        action = get_user_action()

        if action == "V":
            view_tasks(tasks)
        elif action == "A":
            tasks, task_number = add_task(tasks, task_number)
        elif action == "E":
            tasks = edit_task(tasks)
        elif action == "R":
            tasks = remove_task(tasks)
        elif action == "Q":
            print("Alright, see you later!")
            break

def get_user_action():
    options = [
        {"Option": "V", "Description": "View my tasks"},
        {"Option": "A", "Description": "Add a task"},
        {"Option": "E", "Description": "Edit my tasks"},
        {"Option": "R", "Description": "Remove tasks"},
        {"Option": "Q", "Description": "Quit program"}
    ]

    while True:
        print(tabulate(options, headers="keys", tablefmt="fancy_grid"))  # Custom grid style
        choice = input("What do you wanna do?: ").upper()

        if choice in ["V", "A", "E", "R", "Q"]:
            return choice
        else:
            print("Oops! That's not a valid option. Try again!")

def view_tasks(tasks):
    if tasks:
        print(tabulate(tasks, headers="keys", tablefmt="fancy_grid"))  # Custom grid style
    else:
        print("Your task list is empty! Time to add some tasks.")

def add_task(tasks, task_number):
    task_description = input("What's the task?: ")
    task_number += 1
    tasks.append({"Task Number": task_number, "Task": task_description})
    print("Got it! Task added.")
    return tasks, task_number

def edit_task(tasks):
    if not tasks:
        print("Nothing to edit yet! Add some tasks first.")
        return tasks

    task_numbers = [task["Task Number"] for task in tasks]

    while True:
        view_tasks(tasks)
        try:
            task_number = int(input("Which task number do you want to edit?: "))
            if task_number in task_numbers:
                break
            else:
                print("Hmm... That task number doesn't exist. Give it another shot.")
        except ValueError:
            print("Uh-oh, that's not a number! Try again.")

    new_description = input("What's the new task description?: ")
    for task in tasks:
        if task["Task Number"] == task_number:
            task["Task"] = new_description
            print("All set! Task updated.")
            break

    return tasks

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove yet! Add some first.")
        return tasks

    task_numbers = [task["Task Number"] for task in tasks]

    while True:
        view_tasks(tasks)
        try:
            task_number = int(input("Which task number do you want to remove?: "))
            if task_number in task_numbers:
                break
            else:
                print("That task number doesn't exist. Try again.")
        except ValueError:
            print("That's not a number! Give it another go.")

    tasks = [task for task in tasks if task["Task Number"] != task_number]
    print("Poof! Task removed.")

    return tasks

if __name__ == "__main__":
    main()