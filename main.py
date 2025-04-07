from core.config import AppConfig
from infrastructure.repository_factory import RepositoryFactory
from application.task_service import TaskService
from presentation.task_ui import start_app

if __name__ == "__main__":
    # Load configuration
    config = AppConfig.load()
    
    # Initialize infrastructure
    task_repo = RepositoryFactory.create(config)
    
    # Initialize application layer
    task_service = TaskService(task_repo)
    
    # Start presentation layer
    start_app(task_repo, task_service)