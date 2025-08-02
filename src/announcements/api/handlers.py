from fastapi import APIRouter, Depends, Request, Response

from announcements.schemas import AnnouncementCreate, AnnouncementRead
from core.repo import RequestRepo
from core.utils import get_repo

router = APIRouter(
    prefix="/announcements",
    tags=["api announcements"],
)


@router.get("/", response_model=list[AnnouncementRead])
async def get_announcements(repo: RequestRepo = Depends(get_repo)):
    return await repo.announcements.get_all()


@router.post("/", response_model=AnnouncementRead)
async def create_announcement(
    announcement_in: AnnouncementCreate,
    repo: RequestRepo = Depends(get_repo),
):
    return await repo.announcements.create(announcement_in)


@router.get("/{announcement_id}", response_model=AnnouncementRead | None)
async def get_announcement(
    request: Request,
    announcement_id: int,
    repo: RequestRepo = Depends(get_repo),
):
    if request.query_params.get("_method") == "DELETE":
        await repo.announcements.delete(announcement_id)
        return Response(status_code=204)
    return await repo.announcements.get(announcement_id)
