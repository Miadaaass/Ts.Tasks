from typing import List
from .schemas import CreateTaskRequest, TaskResponse

class TaskService:
    def __init__(self):
        self.tasks: List[TaskResponse] = []
        self.current_id = 1

    def create(self, request: CreateTaskRequest) -> TaskResponse:
        task = TaskResponse(
            id=self.current_id,
            title=request.title,
            description=request.description,
            status=request.status
        )
        self.current_id += 1
        self.tasks.append(task)
        return task

    def find_all(self) -> List[TaskResponse]:
        return self.tasks

    def find_one(self, task_id: int) -> TaskResponse:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task with id {task_id} not found")
