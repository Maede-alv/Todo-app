from infrastructure.task_repository import InMemoryStorage
from application.task_service import TaskService
from presentation.task_ui import start_app

if __name__ == "__main__":
    # Initialize Infrastructure Layer
    task_repo = InMemoryStorage()

    # Initialize Application Layer
    task_service = TaskService(task_repo)

    # Start the app (Presentation Layer)
    start_app(task_repo, task_service)