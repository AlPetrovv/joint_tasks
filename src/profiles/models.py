from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.mixins import IDPKINTMixin
from core.models import Base

if TYPE_CHECKING:
    from tasks.models import Task
    from users.models import User


class Profile(Base, IDPKINTMixin):
    username: Mapped[str] = mapped_column(String(100))
    user: Mapped["User"] = relationship(back_populates="profile", uselist=False, cascade="all, delete-orphan")
    tasks: Mapped[list["Task"]] = relationship(back_populates="profile", cascade="all, delete-orphan")

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id}, username:{self.username}"
