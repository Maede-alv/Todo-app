from enum import Enum

class TaskStatus(Enum):
    TODO = "To-Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

    def next_status(self):
        """Move task to the next logical status."""
        if self == TaskStatus.TODO:
            return TaskStatus.IN_PROGRESS
        elif self == TaskStatus.IN_PROGRESS:
            return TaskStatus.DONE
        return self