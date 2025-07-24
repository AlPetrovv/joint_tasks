from fastapi import APIRouter, Depends

from core.repo import RequestRepo
from core.utils import get_repo


from .. import schemas

router = APIRouter(
    prefix="/tasks",
    tags=["api tasks"],
)


@router.post('/', response_model=schemas.TaskRead)
async def create_task(task_in: schemas.TaskCreate, repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.create(task_in)


@router.get('/', response_model=list[schemas.TaskRead])
async def get_tasks(repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.get_all()


@router.get('/{task_id}', response_model=schemas.TaskRead)
async def get_task(task_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.get(task_id)


@router.put('/', response_model=schemas.TaskRead) # todo task_id
async def update_task(task_in: schemas.TaskUpdate, repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.update(task_in)


@router.patch('/{task_id}', response_model=schemas.TaskRead)
async def update_partial_task(task_in: schemas.TaskUpdate, repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.update_partial(task_in)


@router.delete('/{task_id}', response_model=schemas.TaskRead)
async def delete_task(task_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.tasks.delete(task_id)


