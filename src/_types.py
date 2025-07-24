from typing import Type, Union

from db.all_models import Announcement, Task, User, Folder

MODEL = Union[Task, User, Folder, Announcement]
TYPE_MODEL = Type[MODEL]

__all__ = ['MODEL', 'TYPE_MODEL']