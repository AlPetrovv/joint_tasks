from announcements.models import Announcement
from tasks.models import Task
from core.models import Base
from users.models import User
from users_auth.models import AuthUser
from folders.models import Folder

models = (Base, Task, User, Folder, Announcement, AuthUser)

__all__ = [model.__class__.__name__ for model in models].append("models")