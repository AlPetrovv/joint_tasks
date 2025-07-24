from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import EmailType

from core.mixins import IDPKINTMixin
from tasks.models import Task
from core.models import Base


class User(Base, IDPKINTMixin):
    username: Mapped[str] = mapped_column(String(100))
    email: Mapped[EmailType] = mapped_column(EmailType, unique=True, nullable=True)

    tasks: Mapped[list["Task"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    def __str__(self):
        return f'{self.__class__.__name__}#{self.id}, username:{self.username}'
