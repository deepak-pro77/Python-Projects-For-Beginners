# ----------------------------------------
# ToDo App

# storing tasks
# ------------------------------------------
tasks = []

# user input of task to add
# -----------------------------------------


def add_task():

    task = input("\n🟢 Enter your task: ")

    if task != "":
        print("-"*50)
        print(f"✅ Task Added Successfully: ({task}).")
        tasks.append(task)
        return tasks
    else:
        print("❌ Please Write down your task to add!")

# View Tasks
# ------------------------------------------------------


def view_task(tasks):

    print("These are your Tasks So Far:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

    print("-"*50)


# Delete Task
# ------------------------------------------------------
def delete_task(tasks):

    user_task = input("🗑 Enter your task to Delete: ").lower()

    if user_task in tasks:
        print(f"✅ Task Removed Successfully. Task: ({user_task}).")
        tasks.remove(user_task)
    else:
        print("❌Task Does not Exit!")

    return tasks


# Marks Tasks Completed
# ---------------------------------------------------
def mark_task(tasks):

    ask_user = input("\n Enter Task to Mark as Completed: ").lower()

    if ask_user in tasks:
        print(f"✅ ({ask_user}) Marked as completed.")
    else:
        print("❌ Task Does not exist")

    return tasks


# Exporing to txt
# ------------------------------------------------------
def export_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("✅ Tasks exported successfully to tasks.txt")


# main Function
# ----------------------------------------------------


def main():
    # Declaring Global Variable
    global tasks

    # Print Statements and Choices
    print("-"*50)
    print("----- 📄 ToDo App -----")

    # Asking user until he quits
    while True:

        print("\n\n")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Marks Tasks Completed")
        print("5. Export to txt file")
        print("6. Quit")

        choice = int(input("\n😊 Enter you Choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            mark_task(tasks)
        elif choice == 5:
            export_tasks(tasks)
        elif choice == 6:
            print("Quitting the App 😉")
            break

    return "❌ Invalid Choice"


if __name__ == "__main__":
    main()
