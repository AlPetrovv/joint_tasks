from typing import Type, Union

from db.all_models import AccessToken, Announcement, Folder, Task, User

MODEL = Union[Task, User, Folder, Announcement, AccessToken]
TYPE_MODEL = Type[MODEL]

__all__ = ["MODEL", "TYPE_MODEL"]
