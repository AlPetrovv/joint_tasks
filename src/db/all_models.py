from announcements.models import Announcement
from core.models import Base
from folders.models import Folder
from tasks.models import Task
from users.models import User
from users_auth.models import AccessToken, AuthUser

models = (Base, Task, User, Folder, Announcement, AuthUser, AccessToken)

__all__ = [model.__class__.__name__ for model in models].append("models")
