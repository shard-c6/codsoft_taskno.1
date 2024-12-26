class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def update_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            print("Task found. Leave fields blank to keep current values.")
            new_title = input(f"Enter new title (current: {task.title}): ") or task.title
            new_description = input(f"Enter new description (current: {task.description}): ") or task.description
            new_status = input(f"Enter new status (current: {task.status}): ") or task.status
            task.title, task.description, task.status = new_title, new_description, new_status
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.title}' deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to update: "))
                todo_list.update_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                task_index = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
