import datetime as dt
from sqlalchemy import Unicode, func, Date
from sqlalchemy.orm import Mapped, composite, mapped_column
from sqlalchemy_utils import PhoneNumber
from fastapi_users.db import SQLAlchemyBaseUserTable

from core.models import Base


class AuthUser(SQLAlchemyBaseUserTable, Base):
    phone_number: Mapped[str] = mapped_column(Unicode(17), unique=True)
    _phone_number = composite(PhoneNumber, phone_number)
    is_superuser: Mapped[bool] = mapped_column(default=False, server_default=func.false())
    registration_date: Mapped[dt.date] = mapped_column(Date, default=dt.date.today, server_default=func.current_date())

    def __str__(self):
        return f'{self.__class__.__name__}#{self.id} {self.phone_number}'


