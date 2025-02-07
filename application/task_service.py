from domain.task import Task, TaskStatus
from infrastructure.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, name: str):
        """Create a new task."""
        task = Task(name)
        self.repository.add_task(task)

    def delete_task(self, name: str):
        """Delete an existing task."""
        self.repository.delete_task(name)

    def change_task_status(self, name: str):
        """Move a task to the next status."""
        for task in self.repository.get_all_tasks():
            if task.name == name:
                task.change_status()
                return True
        return False

    def list_tasks(self, status: TaskStatus = None):
        """List tasks based on their status."""
        if status:
            return self.repository.get_tasks_by_status(status)
        return self.repository.get_all_tasks()
