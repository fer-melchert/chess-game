def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter the task you want to add: ")
    task_list.append(task)
    print(f'Task "{task}" added to the list.')

def view_tasks(task_list):
    if not task_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(task_list):
                removed_task = task_list.pop(task_number - 1)
                print(f'Task "{removed_task}" removed from the list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            remove_task(task_list)
        elif choice == '4':
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the program
if __name__ == "__main__":
    main()
