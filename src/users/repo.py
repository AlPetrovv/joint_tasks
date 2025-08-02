from typing import Any, Sequence

from core.repo import BaseRepo
from users import User
from users.schemas import UserCreate


class UserRepo(BaseRepo):
    model = User

    async def get(self, user_id: int) -> User | None:
        return await self._get_model(self.model, model_id=user_id)

    async def get_all(self, conditions: list[Any] = None) -> Sequence[User]:
        return await self._get_model_all(self.model, conditions)

    async def create(self, user_in: UserCreate) -> User:
        return await self._create_model(self.model, user_in)

    async def update(self, user_in) -> User:
        return await self._update_model(self.model, user_in)

    async def update_partial(self, user_in) -> User:
        return await self._update_partial_model(self.model, user_in)

    async def delete(self, user_id: int) -> None:
        user = await self._get_model(self.model, model_id=user_id)
        return await self._delete_model(user)
