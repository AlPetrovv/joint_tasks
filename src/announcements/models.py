import datetime as dt
from typing import Optional

from sqlalchemy import Date, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.mixins import IDPKINTMixin
from core.models import Base


class Announcement(IDPKINTMixin, Base):
    title: Mapped[Optional[str]] = mapped_column(String(100), default="Объявление")
    text: Mapped[str] = mapped_column(String(1000))
    autor: Mapped[Optional[str]] = mapped_column(String(100))
    date: Mapped[dt.datetime.date] = mapped_column(
        Date, default=dt.date.today, server_default=func.current_date()
    )
    important: Mapped[bool] = mapped_column(default=False, server_default=func.false())

    def __str__(self):
        return (
            f"{self.__class__.__name__}#{self.id}, "
            f"autor:{self.autor}, date:{self.date}, title:{self.title}, text:{self.text}"
        )

    def __repr__(self):
        return str(self)
