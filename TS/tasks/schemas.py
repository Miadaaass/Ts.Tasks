from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class CreateTaskRequest(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus