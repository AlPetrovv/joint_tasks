import uuid
from typing import Annotated, Optional

from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict, Field, UUID4
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import EmailStr

PhoneNumber.phone_format = 'INTERNATIONAL'


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(max_length=100)
    phone_number: PhoneNumber = Field(max_length=17)
    email: Optional[EmailStr] = Field(title='Email')

class UserRead(User):
    id: int = Field(frozen=True)

class UserCreate(User):
    pass


class UserUpdate(User):
    id: int = Field(frozen=True)

class UserUpdatePartial(BaseModel):
    id: int = Field(frozen=True)
    model_config = ConfigDict(from_attributes=True)
    username: Optional[str] = Field(max_length=100)
    email: Optional[EmailStr] = None
    phone_number: Optional[Annotated[str, Field(max_length=17)]] = None





