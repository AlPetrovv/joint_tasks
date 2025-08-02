import datetime as dt
from typing import Annotated

from fastapi import APIRouter, Depends
from fastui import FastUI
from fastui import components as c
from fastui.forms import fastui_form

from announcements.schemas import AnnouncementCreate
from core.components import get_heading, get_navbar
from core.repo import RequestRepo
from core.utils import get_repo

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"],
)

form_router = APIRouter(
    prefix="/announcements/forms",
    tags=["announcements forms"],
)


@form_router.get(
    "/announcement_form", response_model=FastUI, response_model_exclude_none=True
)
async def announcement_form() -> list[c.AnyComponent]:
    return [
        get_heading("Форма объявления"),
        get_navbar(),
        c.Link(components=[c.Text(text="Назад")], on_click=c.events.BackEvent()),
        c.ModelForm(
            model=AnnouncementCreate,
            submit_url="/api/jt/announcements/create_announcement",
            method="POST",
            display_mode="page",
            initial={"date": dt.date.today()},
        ),
    ]


@router.post(
    "/create_announcement", response_model=FastUI, response_model_exclude_none=True
)
async def create_announcement(
    form: Annotated[AnnouncementCreate, fastui_form(AnnouncementCreate)],
    repo: RequestRepo = Depends(get_repo),
) -> list[c.AnyComponent]:
    await repo.announcements.create(form)
    return [
        get_heading("Объявление было создано"),
        get_navbar(),
        c.Link(
            components=[c.Text(text="Назад")],
            on_click=c.events.BackEvent(),
            class_name="btn btn-primary w-25",
        ),
    ]
