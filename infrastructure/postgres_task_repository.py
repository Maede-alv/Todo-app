import psycopg2
from typing import List
from contextlib import contextmanager
from domain.task import Task
from domain.enums.task_status import TaskStatus
from application.abstract_task_repo import TaskRepository
from psycopg2 import OperationalError, DatabaseError

class PostgresTaskRepository(TaskRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self._ensure_table_exists()

    @contextmanager
    def _get_connection(self):
        """Context manager for database connections"""
        conn = None
        try:
            conn = psycopg2.connect(self.connection_string)
            yield conn
        except OperationalError as e:
            raise ConnectionError(f"Database connection failed: {e}")
        finally:
            if conn:
                conn.close()

    @contextmanager
    def _get_cursor(self):
        """Context manager for database cursors"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except DatabaseError as e:
                conn.rollback()
                raise RuntimeError(f"Database operation failed: {e}")
            finally:
                cursor.close()

    def _ensure_table_exists(self):
        """Create tasks table if it doesn't exist"""
        try:
            with self._get_cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        status TEXT NOT NULL
                    )
                """)
        except Exception as e:
            raise RuntimeError(f"Failed to create tasks table: {e}")

    def create(self, task: Task) -> None:
        """Add a task to the database"""
        try:
            with self._get_cursor() as cur:
                cur.execute(
                    "INSERT INTO tasks (id, name, status) VALUES (%s, %s, %s)",
                    (task.id, task.name, task.status.value)  # Store the enum value
                )
        except Exception as e:
            raise RuntimeError(f"Failed to add task: {e}")

    def delete(self, task_id: int) -> None:
        """Delete a task by ID"""
        try:
            with self._get_cursor() as cur:
                cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        except Exception as e:
            raise RuntimeError(f"Failed to delete task: {e}")

    def list(self) -> List[Task]:
        """List all tasks"""
        try:
            with self._get_cursor() as cur:
                cur.execute("SELECT id, name, status FROM tasks")
                return [
                    Task(
                        id=row[0],
                        name=row[1],
                        status=TaskStatus(row[2])  # Convert string back to enum
                    ) for row in cur.fetchall()
                ]
        except Exception as e:
            raise RuntimeError(f"Failed to list tasks: {e}")
    
    def update(self, task: Task) -> None:
        try:
            with self._get_cursor() as cur:
                cur.execute(
                    "UPDATE tasks SET name = %s, status = %s WHERE id = %s",
                    (task.name, task.status.value, task.id)
                )
        except Exception as e:
            raise RuntimeError(f"Failed to update task: {e}")
