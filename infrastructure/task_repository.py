from domain.task import Task, TaskStatus


class TaskRepository:
    def __init__(self):
        self.tasks = []  # In-memory storage

    def add_task(self, task: Task):
        """Add a new task."""
        self.tasks.append(task)

    def delete_task(self, task_name: str):
        """Delete a task by name."""
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    def get_tasks_by_status(self, status: TaskStatus):
        """Return tasks filtered by status."""
        return [task for task in self.tasks if task.status == status]
