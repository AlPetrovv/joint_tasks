from typing import Optional

from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import Field
import datetime as dt

from users._types import UserIDType
from enums import UserRole

PhoneNumber.phone_format = "INTERNATIONAL"


class User(schemas.BaseUser[UserIDType]):
    # data
    phone_number: PhoneNumber
    # date
    registration_date: dt.datetime = Field(default=dt.datetime.now)
    last_login: dt.datetime = Field(default=dt.datetime.now)
    # statuses
    role: UserRole



class UserRead(User):
    pass


class UserCreate(schemas.BaseUserCreate):
    # data
    phone_number: PhoneNumber
    # date
    registration_date: dt.datetime = Field(default=dt.datetime.now)
    last_login: dt.datetime = Field(default=dt.datetime.now)
    # statuses
    role: UserRole


class UserUpdate(schemas.BaseUserUpdate):
    phone_number: Optional[PhoneNumber] = None
    registration_date: Optional[dt.datetime] = None
    last_login: Optional[dt.datetime] = None
    role: Optional[UserRole] = None
