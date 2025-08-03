from typing import Optional

from pydantic import BaseModel, ConfigDict,Field




class Profile(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(max_length=100)


class ProfileRead(Profile):
    id: int = Field(frozen=True)


class ProfileCreate(Profile):
    pass


class ProfileUpdate(Profile):
    id: int = Field(frozen=True)


class ProfileUpdatePartial(BaseModel):
    id: int = Field(frozen=True)
    model_config = ConfigDict(from_attributes=True)
    username: Optional[str] = Field(max_length=100)