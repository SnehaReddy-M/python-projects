import os


class TodoList:
    FILE_NAME = "tasks.txt"

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    task, status = line.strip().split("|")
                    self.tasks.append(
                        {"task": task, "completed": status == "True"}
                    )

    def save_tasks(self):
        with open(self.FILE_NAME, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['completed']}\n")

    def add_task(self):
        task_name = input("Enter task: ")
        self.tasks.append(
            {"task": task_name, "completed": False}
        )
        self.save_tasks()
        print("✅ Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n===== TASKS =====")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

    def complete_task(self):
        self.view_tasks()

        try:
            num = int(input("Enter task number to mark completed: "))

            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1]["completed"] = True
                self.save_tasks()
                print("✅ Task marked as completed!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    def remove_task(self):
        self.view_tasks()

        try:
            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                self.save_tasks()
                print(f"🗑 Removed: {removed['task']}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n===== TO-DO LIST =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Remove Task")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.complete_task()

            elif choice == "4":
                self.remove_task()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")


todo = TodoList()
todo.run()
