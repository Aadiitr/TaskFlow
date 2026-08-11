from task_manager import TaskManager


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TASKS ==========")

    for task in tasks:
        status = "✓ Completed" if task["completed"] else "○ Pending"
        print(f'{task["id"]}. {task["title"]} [{status}]')

    print("===========================\n")


def main():
    manager = TaskManager()

    while True:
        print("\n====== PERSONAOS TASK MANAGER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue

            task = manager.add_task(title)
            print(f'Task added successfully: "{task["title"]}"')

        elif choice == "2":
            display_tasks(manager.get_tasks())

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                if manager.complete_task(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                if manager.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "5":
            keyword = input("Enter search keyword: ").strip()
            results = manager.search_tasks(keyword)
            display_tasks(results)

        elif choice == "6":
            print("Thank you for using PersonaOS Task Manager.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()