from typing import Type, Union

from db.all_models import AccessToken, Announcement, Folder, Task, Profile, Profile

MODEL = Union[Task, Profile, Folder, Announcement, AccessToken, User]
TYPE_MODEL = Type[MODEL]

__all__ = ["MODEL", "TYPE_MODEL"]
