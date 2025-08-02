from typing import Any, Sequence

from announcements.models import Announcement
from core.repo import BaseRepo


class AnnouncementRepo(BaseRepo):
    model = Announcement

    async def get(self, announcement_id: int) -> Announcement | None:
        return await self._get_model(self.model, model_id=announcement_id)

    async def get_all(self, conditions: list[Any] = None) -> Sequence[Announcement]:
        return await self._get_model_all(self.model, conditions)

    async def create(self, announcement_in) -> Announcement:
        return await self._create_model(self.model, announcement_in)

    async def delete(self, announcement_id: int) -> None:  # fixme
        instance = await self._get_model(self.model, announcement_id)
        return await self._delete_model(instance)
