#!/usr/env/python
tasks = ['1. Buy groceries', '2. Finish homework', '3. Call the dentist']
print('=' * 35) 
print(' ' * 10, 'My To-Do List')
print('=' * 35)

for task in tasks:
    print(task)

print(f"\nTotal tasks: {len(tasks)}\n")

print("What would you like to do?")
print("1. Add a task \n2. Remove a task")
choice = input("Enter your choice: ")

print(f"Choice: {choice}")
if choice == "1":
    new_task = input('Enter new task: ')
    tasks.append(str(len(tasks) + 1) + ". " + new_task)
    print("Updated list: ")
    for task in tasks:
        print(f"{task}")
    print(f"\nTotal Tasks: {len(tasks)}")
elif choice == "2":
    try:
        remove = input("Which task you wanna remove? enter a number: ")
        remove = int(remove)
    except ValueError:
        print("Wrong input...Numbers only")
        exit()
    if remove <= len(tasks):
        tasks.pop(int(remove) - 1)
        print(f"Updated list: ")
        for task in tasks:
            print(task)

        print(f"Total Tasks: {len(tasks)}")
    else:
        print("Wrong input..")
        exit()
else:
    print("Wrong input..")
    exit()




