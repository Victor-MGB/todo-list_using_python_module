from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self,title,description,due_date):
        task = Task(title,description,due_date)
        self.tasks.append(task)
    
    def remove_task(self,index):
        if 0 <= index< len(self.tasks):
            del self.tasks[index]
            return True
        return False
    
    def update_task(self,index, title=None, description=None,due_date=None):
        if 0 < index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
                
            if description:
                task.description = description
            
            if  due_date:
                task.due_date = due_date
                
            return True
        return False
    
    def lsit_task(self):
        if not self.tasks:
            print("No task found")
            return
        
        for idx, task in enumerate(self.tasks):
            print(f"Task {idx + 1}:\n{task}")
            
    def mark_task_complete(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False