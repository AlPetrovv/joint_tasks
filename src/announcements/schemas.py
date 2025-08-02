import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Announcement(BaseModel):
    title: Optional[str] = Field(default="Объявление")
    text: str
    autor: Optional[str] = None
    date: datetime.date = Field(default_factory=datetime.date.today)
    important: Optional[bool] = Field(default=False)


class AnnouncementCreate(Announcement):
    pass


class AnnouncementRead(Announcement):
    id: int


class AnnouncementUpdate(Announcement):
    id: int


class AnnouncementUpdatePartial(Announcement):
    id: int
