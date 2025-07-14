from domain.task import Task
from application.abstract_task_repo import TaskRepository


class MemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = []

    def create(self, task: Task):
        """Add a new task."""
        self.tasks.append(task)

    def delete(self, task_id: int):
        """Delete a task by ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def list(self):
        """Return all tasks."""
        return self.tasks

    def update(self, task: Task):
        """Update an existing task."""
        for i, existing_task in enumerate(self.tasks):
            if existing_task.id == task.id:
                self.tasks[i] = task
                break
