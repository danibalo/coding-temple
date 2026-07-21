from collections import deque
class TaskProcessor:
    def __init__(self):
        self.tasks = deque()
    def add_task(self, name):
        self.tasks.append(name)
        return self.tasks
    def process_next(self):
        if self.tasks:
            return self.tasks.popleft()
        return None  
processor = TaskProcessor()

processor.add_task("Python")
processor.add_task("Java")
processor.add_task("SQL")
print(processor.process_next())