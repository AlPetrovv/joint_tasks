from fastapi import APIRouter, Depends, status

from core.repo import RequestRepo
from core.utils import get_repo

from ..schemas import UserCreate, UserRead

router = APIRouter(
    prefix="/users",
    tags=["api users"],
)


@router.post("/", response_model=UserRead)
async def create_user(user_in: UserCreate, repo: RequestRepo = Depends(get_repo)):
    return await repo.users.create(user_in)


@router.get("/", response_model=list[UserRead])
async def get_users(repo: RequestRepo = Depends(get_repo)):
    return await repo.users.get_all()


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.users.get(user_id)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.users.delete(user_id)
