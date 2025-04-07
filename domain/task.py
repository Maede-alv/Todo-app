from domain.enums.task_status import TaskStatus

class Task:
    def __init__(self, id: int, name: str, status: TaskStatus = TaskStatus.TODO):
        self.id = id
        self.name = name
        self.status = status if isinstance(status, TaskStatus) else TaskStatus(status)
        
    def change_status(self):
        """Move the task to the next status."""
        self.status = self.status.next_status()

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, status={self.status.value})"