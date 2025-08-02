from typing import Annotated

from fastapi import APIRouter, Depends
from fastui import FastUI
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.events import BackEvent, GoToEvent
from fastui.forms import SelectSearchResponse, fastui_form

from core.components import get_heading, get_navbar
from core.repo import RequestRepo
from core.utils import get_repo
from folders.schemas import FolderCreate, FolderRead, FolderTasksUser
from tasks.schemas import TaskRead

router = APIRouter(
    prefix="/folders",
    tags=["jt folders"],
)

form_router = APIRouter(
    prefix="/folders/forms",
    tags=["jt folders forms"],
)


@form_router.get("/search_folder", response_model=SelectSearchResponse)
async def get_folder_queries(
    repo: RequestRepo = Depends(get_repo),
) -> SelectSearchResponse:
    folders = await repo.folders.get_all()
    folders_in = [
        FolderRead.model_validate(folder, from_attributes=True) for folder in folders
    ]
    options = [{"label": folder.name, "value": str(folder.id)} for folder in folders_in]
    return SelectSearchResponse(options=options)


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
async def get_folders(repo: RequestRepo = Depends(get_repo)) -> list[c.AnyComponent]:
    folders = await repo.folders.get_all()
    folders_in = [
        FolderRead.model_validate(folder, from_attributes=True) for folder in folders
    ]
    return [
        c.Page(
            components=[
                get_heading("Папки"),
                get_navbar(),
                c.Div(
                    components=[
                        *[
                            c.Div(
                                components=[
                                    c.Link(
                                        components=[
                                            c.Div(
                                                components=[c.Text(text=folder.name)],
                                                class_name="card-body text-black",
                                            ),
                                        ],
                                        on_click=GoToEvent(
                                            url=f"/jt/folders/{folder.id}"
                                        ),
                                    ),
                                ],
                                class_name="card text-white m-2 w-25 text-center",
                            )
                            for folder in folders_in
                        ],
                    ],
                    class_name="row",
                ),
            ],
        ),
    ]


@router.get("/{folder_id}", response_model=FastUI, response_model_exclude_none=True)
async def get_folder(
    folder_id: int, repo: RequestRepo = Depends(get_repo)
) -> list[c.AnyComponent]:
    folder = await repo.folders.get_with_tasks_and_user(folder_id=folder_id)
    folder_in = FolderTasksUser.model_validate(folder, from_attributes=True)
    return [
        c.Page(
            components=[
                get_heading(f"Folder: {folder_in.name}"),
                get_navbar(),
                c.Link(
                    components=[c.Text(text="Add Task")],
                    on_click=GoToEvent(
                        url=f"/jt/tasks/forms/task_form?folder_id={folder_id}"
                    ),
                    class_name="btn btn-primary",
                ),
                c.Table(
                    data=folder_in.tasks,
                    data_model=TaskRead,
                    columns=[
                        DisplayLookup(field="title"),
                        DisplayLookup(
                            field="start_time",
                            table_width_percent=15,
                            mode=DisplayMode.date,
                        ),
                        DisplayLookup(
                            field="end_time",
                            table_width_percent=15,
                            mode=DisplayMode.date,
                        ),
                        DisplayLookup(field="user", table_width_percent=30),
                    ],
                ),
            ]
        )
    ]


@form_router.get(
    "/folder_form", response_model=FastUI, response_model_exclude_none=True
)
async def folder_form(repo: RequestRepo = Depends(get_repo)) -> list[c.AnyComponent]:
    return [
        c.Page(
            components=[
                get_heading("Добавить папку"),
                get_navbar(),
                c.ModelForm(
                    model=FolderCreate,
                    submit_url="/api/jt/folders/create_folder",
                    method="POST",
                    display_mode="page",
                ),
                c.Link(components=[c.Text(text="Назад")], on_click=BackEvent()),
            ]
        ),
    ]


@router.post("/create_folder", response_model=FastUI, response_model_exclude_none=True)
async def create_folder(
    form: Annotated[FolderCreate, fastui_form(FolderCreate)],
    repo: RequestRepo = Depends(get_repo),
) -> list[c.AnyComponent]:
    folder = await repo.folders.create(form)
    return [
        get_navbar(),
        c.Heading(
            text="Папка была создана успешно", level=6, class_name="text-success"
        ),
        c.Link(
            components=[c.Text(text="Перейти к папке")],
            on_click=GoToEvent(url=f"/jt/folders/{folder.id}"),
            class_name="btn btn-primary w-25",
        ),
    ]
