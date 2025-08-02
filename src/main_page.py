from urllib.parse import urlencode

from fastapi import APIRouter, Depends, Request
from fastui import FastUI
from fastui import components as c

from announcements import schemas as announcement_schemas
from core.components import get_announcement, get_heading, get_navbar
from core.repo import RequestRepo
from core.utils import get_repo

router = APIRouter(
    tags=["main"],
)


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
async def main_page(
    request: Request, repo: RequestRepo = Depends(get_repo)
) -> list[c.AnyComponent]:
    if request.query_params.get("_method") == "DELETE":
        if announcement := await repo.announcements.get(
            int(request.query_params.get("announcement_id"))
        ):
            await repo.announcements.delete(announcement.id)  # fixme: type error
    request.scope["query_string"] = urlencode({}).encode("utf-8")

    announcements = await repo.announcements.get_all()
    announcements_in = [
        announcement_schemas.AnnouncementRead.model_validate(
            announcement, from_attributes=True
        )
        for announcement in announcements
    ]
    return [
        c.Page(
            components=[
                get_heading("Главная"),
                get_navbar(),
                get_announcement(announcements_in),
            ]
        )
    ]
