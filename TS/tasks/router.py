from fastapi import APIRouter, HTTPException, status
from .service import TaskService
from .schemas import CreateTaskRequest, TaskResponse

router = APIRouter(prefix="/tasks", tags=["tasks"])
service = TaskService()

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(request: CreateTaskRequest):
    return service.create(request)

@router.get("", response_model=list[TaskResponse])
def get_all_tasks():
    return service.find_all()

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    try:
        return service.find_one(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")