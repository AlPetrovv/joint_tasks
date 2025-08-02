from typing import Optional

from pydantic import BaseModel, ConfigDict

from tasks.schemas import TaskUser


class Folder(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)


class FolderRead(Folder):
    id: int


class FolderCreate(Folder):
    pass


class FolderUpdate(Folder):
    id: int


class FolderUpdatePartial(BaseModel):
    id: int
    name: Optional[str] = None


class FolderTasksUser(FolderRead):
    tasks: Optional[list["TaskUser"]] = None
