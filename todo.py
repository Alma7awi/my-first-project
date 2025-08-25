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
        if choice == "5":
            break

if __name__ == "__main__":
    main()
elif choice == "1":
            task = input("Enter a new task: ")
            tasks.append({"task": task, "done": False})
            print(f'Task "{task}" added!')


