from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.mixins.mixins import IDPKINTMixin
from core.models import Base

if TYPE_CHECKING:
    from tasks.models import Task


class Folder(IDPKINTMixin, Base):
    name: Mapped[str] = mapped_column(String(100))
    tasks: Mapped[list["Task"]] = relationship(
        back_populates="folder", single_parent=True, cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Folder#{self.__class__.__name__}, name:{self.name}"

    def __repr__(self):
        return str(self)
