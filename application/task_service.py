from domain.task import Task, TaskStatus
from application.abstract_task_repo import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository
        self.next_id = 1  # Auto-incrementing ID counter

    def add_task(self, name: str):
        """Create a new task with an auto-incremented ID."""
        task = Task(self.next_id, name)
        self.repository.create(task)
        self.next_id += 1  # Increment ID for the next task

    def delete_task(self, task_id: int):
        """Delete an existing task by ID."""
        self.repository.delete(task_id)

    def change_task_status(self, task_id: int):
        """Move a task to the next status."""
        for task in self.repository.list():
            if task.id == task_id:
                task.change_status()
                self.repository.update(task)  # Persist the change
                return True
        return False

    def list_tasks(self, status: TaskStatus = None):
        """List tasks based on their status."""
        if status:
            return [task for task in self.repository.list() if task.status == status]
        return self.repository.list()