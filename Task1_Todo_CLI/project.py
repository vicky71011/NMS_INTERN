import sys 
from datetime import datetime

class Task:
    def __init__(self, name):
        self.name = name
        self.status = "Not yet completed"
        self.time = datetime.now().strftime("%d-%m-%Y %H:%M")

    def toggle_status(self):
        if self.status == "Not yet completed":
            self.status = "Completed"
        else:
            self.status = "Not yet completed"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        user_task = input("Enter a task to add: ").strip()

        if not user_task:
            print("Task cannot be empty.")
            return

        task = Task(user_task)
        self.tasks.append(task)
        print("Task added successfully.!")
        
    def remove_task(self):
        if self.check_available():
            try:
                print("Tasks available to remove.")
                self.display_task()
                print()
                
                index = int(input("Enter the index of task to remove: ")) - 1

                if index < 0 or index >= len(self.tasks):
                    print("Invalid index")
                    return
                
                removed_task = self.tasks.pop(index)
                print(f"Task removed : {removed_task.name}")
            except ValueError:
                print("Please enter a valid number")
            
        else:
            print("No element to remove")
            
    def update_status(self):
        if self.check_available(): 
            try:
                self.display_task()
                print()
                
                update_task = int(input("Enter the index of task to update the status: ")) - 1

                if update_task < 0:
                    print("Enter valid index to update.")
                    return
                
                self.tasks[update_task].toggle_status()
                print("Task updated successfully")
            except (ValueError, IndexError):
                print("Enter a valid index to update the status")
        else:
            print("No task to update status.")
    
    def display_task(self):
        if self.check_available():
            print(f"{'ID':<5} {'Task_Name':<17} {'Task_Status':<20} {'Time'}")
            for index, work in enumerate(self.tasks, 1):
                print(f"{index:<5} {work.name:<17} {work.status:<20} {work.time}")
        else:
            print("No tasks created yet.")
            
    def check_available(self):
        return bool(self.tasks)
        

def main():
    todo = ToDoList()

    while True:
        print("Menu")
        print("1.Add a task.")
        print("2.Remove a task.")
        print("3.Update status of the task.")
        print("4.Display the tasks.")
        print("5.Exit.")
        
        try:
            opt = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        
        print()
        
        match opt:
            case 1:
                todo.add_task()
                
            case 2:
                todo.remove_task()
            
            case 3:
                todo.update_status()

            case 4:
                todo.display_task()
                    
            case 5:
                print("Thank You for using me.!!")
                sys.exit()
                
            case _: 
                print("Enter a valid function to execute.\n")
        
        print()
 
if __name__ == "__main__":
    main()