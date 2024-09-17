To_do_list = []

def Display():
    print("\n------TO-DO LIST-----")
    for index, task in enumerate(To_do_list, start=1):
        print(f"{index}. {task}")

def add_task(task):
    To_do_list.append(task)
    print(f"'{task}' has been added to the list.")

def remove_task(task_number):
    if 0 < task_number <= len(To_do_list):
        removed_task = To_do_list.pop(task_number - 1)
        print(f"'{removed_task}' has been removed from the list.")
    else:
        print("Invalid task number.")

while True:
    print("\n-----WELCOME TO THE TO-DO LIST MANAGER----- ")
    print("\nYou can perform the following operations : ")
    print("\nOptions:")
    print("\t1. View To-Do List")
    print("\t2. Add Task")
    print("\t3. Remove Task")
    print("\t4. Exit")

    choice = input("Choose an option : ")

    if choice == '1':
        Display()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        Display()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '4':
        print("Exiting the to-do list manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
