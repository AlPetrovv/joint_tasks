from typing import Annotated

from fastapi import APIRouter, Depends
from fastui import FastUI
from fastui import components as c
from fastui.components.display import Display, DisplayLookup, DisplayMode
from fastui.events import BackEvent, GoToEvent
from fastui.forms import SelectSearchResponse, fastui_form

from core.components import get_heading, get_navbar
from core.repo import RequestRepo
from core.utils import get_repo

from .forms import TaskCreateForm
from .schemas import TaskCreate, TaskRead, TaskUser

router = APIRouter(
    prefix="/tasks",
    tags=["jt tasks"],
)

form_router = APIRouter(
    prefix="/tasks/forms",
    tags=["task forms"],
)


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
async def get_tasks(repo: RequestRepo = Depends(get_repo)):
    c.Link.model_rebuild()
    tasks = await repo.tasks.get_all_with_folder_user()
    tasks_in = [TaskUser.model_validate(task, from_attributes=True) for task in tasks]
    return [
        c.Page(
            components=[
                c.Heading(text="Tasks", level=2),
                c.Link(
                    components=[c.Text(text="Add Task")],
                    on_click=GoToEvent(url="/jt/tasks/forms/task_form"),
                    class_name="btn btn-primary",
                ),
                c.Table(
                    data=tasks_in,
                    data_model=TaskUser,
                    columns=[
                        DisplayLookup(field="title"),
                        DisplayLookup(field="text"),
                        Display(
                            value="user.username",
                            title="User",
                            on_click=GoToEvent(url="/jt/profiles/{user.id}"),
                        ),
                        DisplayLookup(
                            field="start_time",
                            title="Дата начала",
                            mode=DisplayMode.date,
                        ),
                        DisplayLookup(
                            field="end_time",
                            title="Дата завершения",
                            mode=DisplayMode.date,
                        ),
                    ],
                ),
            ]
        ),
    ]


@form_router.get("/task_form", response_model=FastUI, response_model_exclude_none=True)
async def task_form(
    repo: RequestRepo = Depends(get_repo), folder_id: int | None = None
):
    initial = {}
    if folder_id:
        folder = await repo.folders.get(folder_id)
        initial["folder"] = {"label": folder.name, "value": folder_id}
    return [
        get_heading("Task Form"),
        get_navbar(),
        c.ModelForm(
            model=TaskCreateForm,
            submit_url="/api/jt/tasks/create_task",
            method="POST",
            display_mode="page",
            initial=initial,
        ),
        c.Link(components=[c.Text(text="Back")], on_click=BackEvent()),
    ]


@form_router.get("/search_task", response_model=SelectSearchResponse)
async def get_tasks_queries(
    repo: RequestRepo = Depends(get_repo),
) -> SelectSearchResponse:
    tasks = await repo.tasks.get_all()
    tasks_in = [TaskRead.model_validate(task, from_attributes=True) for task in tasks]
    options = [{"label": task.title, "value": str(task.id)} for task in tasks_in]
    return SelectSearchResponse(options=options)


@router.post("/create_task", response_model=FastUI, response_model_exclude_none=True)
async def create_task(
    form: Annotated[TaskCreateForm, fastui_form(TaskCreateForm)],
    repo: RequestRepo = Depends(get_repo),
) -> list[c.AnyComponent]:
    task_in: TaskCreate = TaskCreate(
        **form.model_dump(exclude={"folder", "user"}),
        folder_id=int(form.folder),
        user_id=int(form.user),
    )
    task = await repo.tasks.create(task_in)
    return [
        get_heading("Карта была создана успешно"),
        get_navbar(),
        c.Link(
            components=[c.Text(text="Вернуться к карте")],
            on_click=GoToEvent(url=f"/jt/tasks/{task.id}"),
        ),
    ]


@router.get("/{task_id}", response_model=FastUI, response_model_exclude_none=True)
async def get_task(
    task_id: int, repo: RequestRepo = Depends(get_repo)
) -> list[c.AnyComponent]:
    task = await repo.tasks.get_with_folder_user(task_id)
    task_in = TaskUser.model_validate(task, from_attributes=True)
    return [
        c.Page(
            components=[
                get_heading(f"Task #{task_in.id}"),
                get_navbar(),
                c.Link(
                    components=[c.Text(text="Add task")],
                    on_click=GoToEvent(
                        url=f"/jt/tasks/forms/row_form?task_id={task_in.id}"
                    ),
                    class_name="btn btn-primary",
                ),
                c.Details(
                    data=task_in,
                    fields=[
                        DisplayLookup(field="title"),
                        DisplayLookup(field="text"),
                        Display(
                            value=task_in.user.username,
                            title="User",
                            on_click=GoToEvent(url=f"/jt/profiles/{task_in.user.id}"),
                        ),
                        DisplayLookup(
                            field="start_time",
                            title="Дата начала",
                            mode=DisplayMode.date,
                        ),
                        DisplayLookup(
                            field="end_time",
                            title="Дата завершения",
                            mode=DisplayMode.date,
                        ),
                    ],
                ),
            ]
        ),
    ]
