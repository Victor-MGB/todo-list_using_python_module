from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. List Tasks")
        print("5. Mark Task as Complete")
        print("6. Exit")
        
        choice = input("choose an option :")
        
        if choice == '1':
            title = input("Enter task title : ")
            description = input("Enter task descritpion :")
            due_date = input("Enter due date (YYYY-MM-DD) :")
            manager.add_task(title, description,due_date)
            print("Task added successfully!")
        
        elif choice == '2':
            index = int(input("Enter taks number to remove :"))
            if manager.remove_task(index):
                print("Task removed successfully.")
            else:
                print("Invalid task number")
                
        elif choice == "3":
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new task title (leave blank to keep current): ")
            description = input("Enter new task description (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            if manager.update_task(index, title, description, due_date):
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
                
        elif choice == '4':
            manager.lsit_task()
        
        elif choice == '5':
            index = int(input("Enter task number to mark as complete:"))
            if manager.mark_task_complete(index):
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
                
        elif choice == '6':
            print("Exiting todo-list manager")
            break
        
        else:
            print("Invalid choice.please try again.")
            
if __name__ == "__main__":
    main()