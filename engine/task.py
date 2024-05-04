import uuid
from datetime import datetime

class Task:
    task_registry = {}

    def __init__(self, objective, assigned_user):
        """
        Initialize a new task with the specified attributes.
        
        :param objective: A string describing what the task is meant to achieve.
        :param assigned_user: The user ID of the user to whom the task is assigned.
        """
        self.task_id = str(uuid.uuid4())  # Generate a unique task identifier.
        self.objective = objective
        self.assigned_user = assigned_user
        self.time_assigned = datetime.now()
        self.status = 'pending'  # Default status is 'pending'
        self.result = None
        Task.task_registry[self.task_id] = self  # Register the task by its ID.

    def update_status(self, new_status):
        """
        Update the status of the task.
        
        :param new_status: A string indicating the new status of the task ('pending', 'active', 'completed').
        """
        self.status = new_status

    def set_result(self, result):
        """
        Set the result of the task once it is completed.
        
        :param result: The result of the task, format should match self.result_format.
        """
        if self.status == 'completed':
            self.result = result
        else:
            raise ValueError("Cannot set result unless task is completed.")

    @staticmethod
    def get_task_by_id(task_id):
        """
        Fetch a task object by its ID.
        
        :param task_id: The unique identifier of the task.
        :return: Task object if found, None otherwise.
        """
        return Task.task_registry.get(task_id)

    def __str__(self):
        """
        Return a string representation of the task, for easy debugging and logging.
        """
        return (f"Task ID: {self.task_id}, Objective: {self.objective}, Assigned to: {self.assigned_user}, "
                f"Status: {self.status}, Time Assigned: {self.time_assigned.strftime('%Y-%m-%d %H:%M:%S')}")

