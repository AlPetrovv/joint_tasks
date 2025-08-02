from typing import Literal

from fastui import components as c
from fastui.events import GoToEvent

from announcements.schemas import AnnouncementRead


def get_navbar() -> c.Navbar:
    return c.Navbar(
        title="JT",
        title_event=c.events.GoToEvent(url="/jt/"),
        start_links=[
            c.Link(
                components=[c.Text(text="Папки")],
                on_click=c.events.GoToEvent(url="/jt/jt/"),
            ),
        ],
        end_links=[
            c.Link(
                components=[c.Text(text="Назад")],
                on_click=c.events.BackEvent(),
                class_name="btn btn-primary",
            ),
            c.Link(
                components=[c.Text(text="Добавить папку")],
                on_click=c.events.GoToEvent(url="/jt/folders/forms/folder_form"),
                class_name="btn btn-primary",
            ),
            c.Link(
                components=[c.Text(text="Добавить задачу")],
                on_click=c.events.GoToEvent(url="/jt/tasks/forms/task_form"),
                class_name="btn btn-primary",
            ),
        ],
    )


def get_heading(
    additional_text: str = None,
    level: Literal[1, 2, 3, 4, 5, 6] = 1,
    class_name: str = None,
) -> c.Heading:
    return c.Heading(text=f"{additional_text}", level=level, class_name=class_name)


def get_announcement(announcements_in: list[AnnouncementRead]) -> c.Div:
    return c.Div(
        components=[
            c.Link(
                components=[c.Text(text="Добавить объявление")],
                on_click=GoToEvent(url="/jt/announcements/forms/announcement_form"),
                class_name="btn btn-primary",
            ),
            *[
                c.Div(
                    components=[
                        c.Div(
                            components=[
                                c.Text(text=announcement_in.title or "Без названия")
                            ],
                            class_name="card-header text-black",
                        ),
                        c.Div(
                            components=[
                                c.Heading(
                                    text=announcement_in.autor or "Без автора", level=5
                                ),
                                c.Paragraph(text=announcement_in.text),
                            ],
                            class_name="card-body text-black",
                        ),
                        c.Link(
                            components=[c.Text(text="Удалить")],
                            on_click=GoToEvent(
                                query={
                                    "_method": "DELETE",
                                    "announcement_id": announcement_in.id,
                                }
                            ),
                            class_name="btn",
                        ),
                    ],
                    class_name=f"card m-2 w-25 text-center card-danger {'bg-danger' if announcement_in.important else ''}",
                )
                for announcement_in in announcements_in
            ],
        ],
        class_name="row",
    )
