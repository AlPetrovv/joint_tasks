from fastapi import APIRouter, Depends

from core.repo import RequestRepo
from core.utils import get_repo
from ..schemas import FolderCreate, FolderRead

router = APIRouter(
    prefix="/folders",
    tags=["api folders"],
)


@router.get("/", response_model=list[FolderRead])
async def get_folders(repo: RequestRepo = Depends(get_repo)):
    return await repo.folders.get_all()


@router.post("/")
async def create_folder(folder_in: FolderCreate, repo: RequestRepo = Depends(get_repo)):
    return repo.folders.create(folder_in)


@router.get("/{folder_id}", response_model=FolderRead)
async def get_folder(folder_id: int, repo: RequestRepo = Depends(get_repo)) -> FolderRead:
    folder = await repo.folders.get(folder_id)
    return FolderRead.model_validate(folder, from_attributes=True)

