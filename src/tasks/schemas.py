import datetime
from datetime import date
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field

from enums import TaskPriorityEnum, TaskWhereEnum
from profiles.schemas import ProfileRead


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # data
    title: Annotated[str, Field(max_length=100)]
    text: Annotated[str, Field(max_length=1000)]
    note: Optional[Annotated[str, Field(max_length=1000)]] = None
    # time
    start_time: date
    end_time: date
    completed_time: Optional[datetime.datetime] = None
    # status
    completed: Optional[bool] = False
    priority: TaskPriorityEnum
    where: TaskWhereEnum


class TaskCreate(Task):
    user_id: int
    folder_id: int


class TaskUpdate(Task):
    id: int
    user_id: int
    folder_id: int


class TaskRead(Task):
    user_id: int
    folder_id: int
    id: int


class TaskUpdatePartial(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    # data
    title: Optional[Annotated[str, Field(max_length=100)]] = None
    text: Optional[Annotated[str, Field(max_length=1000)]] = None
    note: Optional[Annotated[str, Field(max_length=1000)]] = None
    # time
    start_time: Optional[date] = None
    end_time: Optional[date] = None
    completed_time: Optional[datetime.datetime] = None
    # status
    completed: Optional[bool] = None
    priority: Optional[TaskPriorityEnum] = None
    where: Optional[TaskWhereEnum] = None
    # relations
    user_id: Optional[int] = None
    folder_id: Optional[int] = None


class TaskUser(TaskRead):
    user: ProfileRead
