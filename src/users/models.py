import datetime as dt
from typing import TYPE_CHECKING, Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import Date, DateTime, Enum, Unicode, func
from sqlalchemy.orm import Mapped, composite, mapped_column, relationship
from sqlalchemy_utils import PhoneNumber

from users._types import UserIDType
from core.mixins import IDPKINTMixin,ProfileRelationMixin, UserRelationMixin
from core.models import Base
from enums import UserRole

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IDPKINTMixin, ProfileRelationMixin, SQLAlchemyBaseUserTable[UserIDType]):
    _profile_options = {
        "back_populates": "user",
        "uselist": False,
    }

    # data
    phone_number: Mapped[Optional[str]] = mapped_column(Unicode(17), unique=True)
    _phone_number = composite(PhoneNumber, phone_number)
    # date
    registration_date: Mapped[dt.date] = mapped_column(
        Date, default=dt.date.today, server_default=func.current_date()
    )
    last_login: Mapped[dt.datetime] = mapped_column(
        DateTime, default=dt.datetime.now, server_default=func.now()
    )
    # statuses
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), default=UserRole.MEMBER, server_default=UserRole.MEMBER.value
    )

    access_tokens: Mapped[list["AccessToken"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.__class__.__name__}#{self.id} {self.email}"

    @classmethod
    def get_repo(cls, session: "AsyncSession"):
        """return database for access token model(repo)"""
        return SQLAlchemyUserDatabase(session, cls)


class AccessToken(Base, UserRelationMixin, SQLAlchemyBaseAccessTokenTable[UserIDType]):
    _user_options = {
        "back_populates": "access_tokens",
        "id_nullable": False,
    }

    @classmethod
    def get_repo(cls, session: "AsyncSession"):
        """:return database for access token model(repo)"""
        return SQLAlchemyAccessTokenDatabase(session, cls)
