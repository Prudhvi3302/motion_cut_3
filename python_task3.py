class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\n--- Tasks ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. Description: {task.description}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Completed: {'Yes' if task.completed else 'No'}")
            print("--------------------")
    
    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task index.")

# Sample usage
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            new_task = Task(description, due_date, priority)
            todo_list.add_task(new_task)

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)

        elif choice == "4":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")
