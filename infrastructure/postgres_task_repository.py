from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List
from domain.task import Task
from domain.enums.task_status import TaskStatus
from application.abstract_task_repo import TaskRepository

Base = declarative_base()


class TaskORM(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)


class PostgresTaskRepository(TaskRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        Task.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self._init_next_id()

    def _init_next_id(self):
        with self.Session() as session:
            max_id = session.query(Task.id).order_by(Task.id.desc()).first()
            self.next_id = (max_id[0] + 1) if max_id and max_id[0] is not None else 1

    def create(self, task: Task) -> None:
        with self.Session() as session:
            if task.id is None:
                task.id = self.next_id
                self.next_id += 1
            orm_task = Task()
            orm_task.id = int(task.id)
            orm_task.name = str(task.name)
            orm_task.status = str(task.status.value)
            session.add(orm_task)
            session.commit()

    def delete(self, task_id: int) -> None:
        with self.Session() as session:
            task = session.query(Task).filter_by(id=task_id).first()
            if task:
                session.delete(task)
                session.commit()

    def list(self) -> List[Task]:
        with self.Session() as session:
            orm_tasks = session.query(Task).all()
            return [
                Task(
                    id=orm_task.id,
                    name=orm_task.name,
                    status=TaskStatus(orm_task.status),
                )
                for orm_task in orm_tasks
            ]

    def update(self, task: Task) -> None:
        with self.Session() as session:
            orm_task = session.query(Task).filter_by(id=task.id).first()
            if orm_task:
                setattr(orm_task, "name", task.name)
                setattr(orm_task, "status", task.status.value)
                session.commit()
