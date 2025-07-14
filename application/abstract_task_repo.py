from abc import ABC, abstractmethod
from domain.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> None:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Task]:
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        pass
