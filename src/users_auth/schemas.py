from typing import Optional

from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import Field
import datetime as dt

from enums import UserRole

PhoneNumber.phone_format = "INTERNATIONAL"


class AuthUser(schemas.BaseUser[int]):
    # data
    phone_number: PhoneNumber
    # date
    registration_date: dt.datetime = Field(default=dt.datetime.now)
    last_login: dt.datetime = Field(default=dt.datetime.now)
    # statuses
    role: UserRole



class AuthUserRead(AuthUser):
    pass


class AuthUserCreate(schemas.BaseUserCreate):
    # data
    phone_number: PhoneNumber
    # date
    registration_date: dt.datetime = Field(default=dt.datetime.now)
    last_login: dt.datetime = Field(default=dt.datetime.now)
    # statuses
    role: UserRole


class AuthUserUpdate(schemas.BaseUserUpdate):
    phone_number: Optional[PhoneNumber] = None
    registration_date: Optional[dt.datetime] = None
    last_login: Optional[dt.datetime] = None
    role: Optional[UserRole] = None
