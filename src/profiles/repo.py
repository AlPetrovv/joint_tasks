from typing import Any, Sequence

from core.repo import BaseRepo
from .models import Profile
from .schemas import ProfileCreate


class ProfileRepo(BaseRepo):
    model = Profile

    async def get(self, profile_id: int) -> Profile | None:
        return await self._get_model(self.model, model_id=profile_id)

    async def get_all(self, conditions: list[Any] = None) -> Sequence[Profile]:
        return await self._get_model_all(self.model, conditions)

    async def create(self, profile_in: ProfileCreate) -> Profile:
        return await self._create_model(self.model, profile_in)

    async def update(self, profile_in) -> Profile:
        return await self._update_model(self.model, profile_in)

    async def update_partial(self, profile_in) -> Profile:
        return await self._update_partial_model(self.model, profile_in)

    async def delete(self, profile_id: int) -> None:
        user = await self._get_model(self.model, model_id=profile_id)
        return await self._delete_model(user)
