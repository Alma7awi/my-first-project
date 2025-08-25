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
elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "Done" if t["done"] else "Pending"
                    print(f"{i}. {t['task']} [{status}]")



