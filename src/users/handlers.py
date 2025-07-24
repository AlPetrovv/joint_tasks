from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastui import AnyComponent, FastUI
from fastui import components as c
from fastui.events import GoToEvent
from fastui.forms import SelectSearchResponse, fastui_form

from core.components import get_heading, get_navbar
from core.repo import RequestRepo
from core.utils import get_repo
from users.forms import UserFormCreate, UserFormUpdatePartial
from users.schemas import UserRead

form_router = APIRouter(
    prefix="/users/forms",
    tags=["jt users forms"],
)

router = APIRouter(
    prefix="/users",
    tags=["jt users"],
)


@form_router.get("/search_user", response_model=SelectSearchResponse)
async def get_user_queries(repo: RequestRepo = Depends(get_repo)) -> SelectSearchResponse:
    users = await repo.users.get_all()
    users_in = [UserRead.model_validate(user, from_attributes=True) for user in users]
    options = [{"label": user_in.username, "value": str(user_in.id)} for user_in in users_in]
    return SelectSearchResponse(options=options)


@form_router.get("/user_form", response_model=FastUI, response_model_exclude_none=True)
async def user_form() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                get_navbar(),
                get_heading('User Form'),
                c.ModelForm(
                    model=UserFormCreate,
                    submit_url='/api/jt/users/create_user',
                    method="POST",
                    display_mode='page',
                    initial={
                        'phone_number': '+7'
                    }
                ),
            ])
    ]


@router.post("/create_user", response_model=FastUI, response_model_exclude_none=True)
async def create_user(form: Annotated[UserFormCreate, fastui_form(UserFormCreate)],
                      repo: RequestRepo = Depends(get_repo)) -> list[AnyComponent]:
    await repo.users.create(form)
    return [
        c.Link(components=[c.Text(text='Back to me')], on_click=GoToEvent(url=f'/jt/users/{form.id}'),
               class_name='btn btn-primary w-25'),
        c.Text(text='Сотрудник был создан успешно'),
    ]


@router.get("/{user_id}", response_model=FastUI, response_model_exclude_none=True)
async def get_user(user_id: int, repo: RequestRepo = Depends(get_repo)) -> list[
    AnyComponent]:
    user = await repo.users.get(user_id)
    if user is None:
        return [
            get_navbar(),
            get_heading('User not found'),
        ]
    user_in = UserRead.model_validate(user, from_attributes=True)

    return [
        get_navbar(),
        get_heading('User'),
        c.ModelForm(
            model=UserFormUpdatePartial,
            submit_url='/api/jt/users/update_user',
            method="POST",
            display_mode='page',
            initial=user_in.model_dump(),
        )
    ]


@router.post("/update_user", response_model=FastUI, response_model_exclude_none=True)
async def update_user(
        form: Annotated[UserFormUpdatePartial, fastui_form(UserFormUpdatePartial)],
        repo: RequestRepo = Depends(get_repo),
) -> list[AnyComponent]:
    await repo.users.update_partial(form)
    return [
        c.Text(text='Data was updated successfully'),
    ]
