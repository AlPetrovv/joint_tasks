from announcements.models import Announcement
from core.models import Base
from folders.models import Folder
from tasks.models import Task
from profiles.models import Profile
from users.models import AccessToken, User

models = (Base, Task, User, Folder, Announcement, Profile, AccessToken)

__all__ = [model.__class__.__name__ for model in models].append("models")
