from fastapi import Depends, HTTPException
from starlette import status

from core.repo import RequestRepo
from core.utils import get_repo
from tasks.models import Task


async def get_task(task_id: int, repo: RequestRepo = Depends(get_repo)) -> Task:
    task = await repo.tasks.get_with_folder_user(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found",
        )
    return task
