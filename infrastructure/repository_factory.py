from typing import Union
from application.abstract_task_repo import TaskRepository
from infrastructure.memory_task_repository import MemoryTaskRepository
from infrastructure.postgres_task_repository import PostgresTaskRepository

class RepositoryFactory:
    """Creates repository instances without exposing implementations"""
    
    @staticmethod
    def create(config: dict) -> TaskRepository:
        storage_type = config['storage']['type']
        
        if storage_type == 'memory':
            return MemoryTaskRepository()
            
        elif storage_type == 'database':
            db_config = config['storage']['database']
            connection_string = (
                f"{db_config['dialect']}://"
                f"{db_config['user']}:{db_config['password']}@"
                f"{db_config['host']}:{db_config['port']}/"
                f"{db_config['name']}"
            )
            return PostgresTaskRepository(connection_string)
            
        raise ValueError(f"Unknown storage type: {storage_type}")