from domain.task import Task
from application.abstract_task_repo import TaskRepository

class InMemoryStorage(TaskRepository):
    def __init__(self):
        self.tasks = []

    def add(self, task: Task):
        """Add a new task."""
        self.tasks.append(task)

    def delete(self, task_id: int):
        """Delete a task by ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def list(self):
        """Return all tasks."""
        return self.tasks