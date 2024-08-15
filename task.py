from datetime import datetime

class Task:
    def __init__(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False
        
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\nCreated At: {self.created_at}\n"
