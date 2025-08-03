from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from announcements.repo import AnnouncementRepo
from folders.repo import FolderRepo
from tasks.repo import TaskRepo
from profiles.repo import ProfileRepo


@dataclass
class RequestRepo:
    session: AsyncSession

    @property
    def announcements(self) -> AnnouncementRepo:
        return AnnouncementRepo(session=self.session)

    @property
    def tasks(self) -> TaskRepo:
        return TaskRepo(session=self.session)

    @property
    def folders(self) -> FolderRepo:
        return FolderRepo(session=self.session)

    @property
    def profiles(self) -> ProfileRepo:
        return ProfileRepo(session=self.session)
