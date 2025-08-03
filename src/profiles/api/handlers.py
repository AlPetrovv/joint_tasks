from fastapi import APIRouter, Depends, status

from core.repo import RequestRepo
from core.utils import get_repo

from profiles.schemas import ProfileCreate, ProfileRead

router = APIRouter(
    prefix="/profiles",
    tags=["api profiles"],
)


@router.post("/", response_model=ProfileRead)
async def create_user(user_in: ProfileCreate, repo: RequestRepo = Depends(get_repo)):
    return await repo.profiles.create(user_in)


@router.get("/", response_model=list[ProfileRead])
async def get_users(repo: RequestRepo = Depends(get_repo)):
    return await repo.profiles.get_all()


@router.get("/{user_id}", response_model=ProfileRead)
async def get_user(user_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.profiles.get(user_id)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, repo: RequestRepo = Depends(get_repo)):
    return await repo.profiles.delete(user_id)
