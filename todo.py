tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Invalid choice! Please enter a number 1-5.")
            continue
        choice = int(choice)

        # Add Task
        if choice == 1:
            task = input("Enter a new task: ").strip()
            if not task:
                print("Task cannot be empty!")
                continue
            tasks.append({"task": task, "done": False})
            print(f'Task "{task}" added!')

        # View Tasks
        elif choice == 2:
            if not tasks:
                print("No tasks yet!")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "Done" if t["done"] else "Pending"
                    print(f"{i}. {t['task']} [{status}]")

        # Mark Task as Done
        elif choice == 3:
            if not tasks:
                print("No tasks to mark!")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "Done" if t["done"] else "Pending"
                    print(f"{i}. {t['task']} [{status}]")
                num_input = input("Enter task number to mark done: ")
                if not num_input.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue
                num = int(num_input)
                if num < 1 or num > len(tasks):
                    print("Invalid task number!")
                    continue
                tasks[num-1]["done"] = True
                print(f'Task "{tasks[num-1]["task"]}" marked as done!')

        # Delete Task
        elif choice == 4:
            if not tasks:
                print("No tasks to delete!")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "Done" if t["done"] else "Pending"
                    print(f"{i}. {t['task']} [{status}]")
                num_input = input("Enter task number to delete: ")
                if not num_input.isdigit():
                    print("Invalid input! Please enter a number.")
                    continue
                num = int(num_input)
                if num < 1 or num > len(tasks):
                    print("Invalid task number!")
                    continue
                removed = tasks.pop(num-1)
                print(f'Task "{removed["task"]}" deleted!')

        # Exit
        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
