def main():
    tasks = []
    
    while True:
        print("====To Do List====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark the task as done")
        print("4. Delete the task")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            task_num = int(input("Enter how many tasks would you like to add: "))
            for i in range(task_num):
                task_input = input("Enter the task: ")
                tasks.append({
                    "task": task_input,
                    "done": False
                })
            print("Task Added!!")

        elif choice == "2":
            print("Task")
            for index, tasks in enumerate(tasks):
                status = "Done" if tasks["done"] else "Not Done"
                print(f"{index + 1}.{tasks['task']} - {status}")

        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done")
            else:
                print("Invalid task number")
        
        elif choice == "4":
            task_index = int(input("Enter the task number to be deleted : "))
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Deleted task : {deleted_task['task']}")
            else:
                print("Invalid Task Number")

        elif choice == "5":
            print("Exiting the app")
            break
        
if __name__ == "__main__":
    main()
      


