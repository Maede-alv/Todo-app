import pytest
from application.task_service import TaskService
from infrastructure.memory_task_repository import MemoryTaskRepository
from domain.task import TaskStatus

class TestTaskService:
    def setup_method(self):
        """Set up a fresh repository and service for each test."""
        self.repo = MemoryTaskRepository()
        self.service = TaskService(self.repo)

    def test_add_task(self):
        """Test adding a new task."""
        self.service.add_task("Test Task")
        tasks = self.service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].name == "Test Task"
        assert tasks[0].status == TaskStatus.TODO
        assert tasks[0].id == 1

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with auto-incrementing IDs."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")
        
        tasks = self.service.list_tasks()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[1].id == 2
        assert tasks[2].id == 3

    def test_delete_task(self):
        """Test deleting a task."""
        self.service.add_task("Task to delete")
        self.service.add_task("Task to keep")
        
        # Delete the first task
        self.service.delete_task(1)
        
        tasks = self.service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].name == "Task to keep"
        assert tasks[0].id == 2

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        self.service.add_task("Test Task")
        
        # Try to delete a non-existent task
        self.service.delete_task(999)
        
        # Should not affect existing tasks
        tasks = self.service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].name == "Test Task"

    def test_change_task_status(self):
        """Test changing task status through the workflow."""
        self.service.add_task("Test Task")
        
        # Initial status should be TODO
        tasks = self.service.list_tasks()
        assert tasks[0].status == TaskStatus.TODO
        
        # Change status to IN_PROGRESS
        result = self.service.change_task_status(1)
        assert result == True
        
        tasks = self.service.list_tasks()
        assert tasks[0].status == TaskStatus.IN_PROGRESS
        
        # Change status to DONE
        result = self.service.change_task_status(1)
        assert result == True
        
        tasks = self.service.list_tasks()
        assert tasks[0].status == TaskStatus.DONE
        
        # Status should not change after DONE
        result = self.service.change_task_status(1)
        assert result == True
        
        tasks = self.service.list_tasks()
        assert tasks[0].status == TaskStatus.DONE

    def test_change_nonexistent_task_status(self):
        """Test changing status of a task that doesn't exist."""
        self.service.add_task("Test Task")
        
        # Try to change status of non-existent task
        result = self.service.change_task_status(999)
        assert result == False
        
        # Should not affect existing task
        tasks = self.service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].status == TaskStatus.TODO

    def test_list_tasks_all(self):
        """Test listing all tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")
        
        tasks = self.service.list_tasks()
        assert len(tasks) == 3
        assert all(task.status == TaskStatus.TODO for task in tasks)

    def test_list_tasks_by_status(self):
        """Test listing tasks filtered by status."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")
        
        # Change status of first task
        self.service.change_task_status(1)
        
        # List only TODO tasks
        todo_tasks = self.service.list_tasks(TaskStatus.TODO)
        assert len(todo_tasks) == 2
        assert all(task.status == TaskStatus.TODO for task in todo_tasks)
        
        # List only IN_PROGRESS tasks
        in_progress_tasks = self.service.list_tasks(TaskStatus.IN_PROGRESS)
        assert len(in_progress_tasks) == 1
        assert in_progress_tasks[0].status == TaskStatus.IN_PROGRESS
        
        # List only DONE tasks
        done_tasks = self.service.list_tasks(TaskStatus.DONE)
        assert len(done_tasks) == 0

    def test_list_tasks_empty(self):
        """Test listing tasks when repository is empty."""
        tasks = self.service.list_tasks()
        assert len(tasks) == 0
        
        # Test with status filter
        todo_tasks = self.service.list_tasks(TaskStatus.TODO)
        assert len(todo_tasks) == 0 