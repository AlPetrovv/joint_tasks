from typing import Optional

from pydantic import BaseModel, ConfigDict,Field




class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(max_length=100)


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