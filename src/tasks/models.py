import datetime as dt
from typing import Optional

from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.mixins import IDPKINTMixin
from core.mixins.relations import (
    FolderRelationMixin,
    TaskRelationMixin,
    ProfileRelationMixin,
)
from core.models import Base
from enums import TaskPriorityEnum, TaskWhereEnum


class Task(Base, IDPKINTMixin, ProfileRelationMixin, FolderRelationMixin, TaskRelationMixin):
    _profile_options = {
        "back_populates": "tasks",
        "id_nullable": False,
    }
    _folder_options = {
        "back_populates": "tasks",
        "id_nullable": False,
    }
    _task_options = {
        "on_delete": "SET NULL",
    }
    # data
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    text: Mapped[str] = mapped_column(String(1000), nullable=False)
    note: Mapped[Optional[str]] = mapped_column(String(1000))

    # date
    start_time: Mapped[dt.date] = mapped_column(Date)
    end_time: Mapped[dt.date] = mapped_column(Date)
    completed_time: Mapped[Optional[dt.datetime]] = mapped_column(DateTime)

    # status
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    priority: Mapped[TaskPriorityEnum] = mapped_column(
        Enum(TaskPriorityEnum),
        default=TaskPriorityEnum.low,
        server_default=TaskPriorityEnum.low.value,
    )
    where: Mapped[TaskWhereEnum] = mapped_column(
        Enum(TaskWhereEnum),
        default=TaskWhereEnum.home,
        server_default=TaskWhereEnum.home.value,
    )

    __table_args__ = (
        CheckConstraint(
            "start_time <= end_time",
            name="check_start_end_ttime",
        ),
    )

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id}, title: {self.title}"
