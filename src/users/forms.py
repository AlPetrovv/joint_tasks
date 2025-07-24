from typing import Annotated, Optional

from pydantic import Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber

from users.schemas import User, UserCreate, UserUpdatePartial

PhoneNumber.phone_format = 'INTERNATIONAL'


class UserSelectForm(User):
    user: str = Field(json_schema_extra={'search_url': '/api/jt/users/search_user'})


class UserFormCreate(UserCreate):
    phone_number: Annotated[str, Field(max_length=17)]

    @field_validator('phone_number', mode='before')
    def check_phone_number(cls, phone_number: str) -> str:
        if not phone_number.startswith('+'):
            raise ValueError("Phone number must start with +")
        if len(phone_number) > 17:
            raise ValueError("Phone number must be less than 17")
        phone_number = PhoneNumber(phone_number)
        return phone_number


class UserFormUpdatePartial(UserUpdatePartial):
    phone_number: Optional[Annotated[str, Field(max_length=17, title='Номер телефона +7...')]]

    @field_validator('phone_number', mode='before')
    def check_phone_number(cls, phone_number: str) -> str | None:
        if phone_number is None:
            return None
        if not phone_number.startswith('+'):
            raise ValueError("Phone number must start with +")
        if len(phone_number) > 17:
            raise ValueError("Phone number must be less than 17")
        phone_number = PhoneNumber(phone_number)
        return phone_number