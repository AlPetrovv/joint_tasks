from typing import Sequence, Any

from core.repo import BaseRepo
from tasks.models import Task


class TaskRepo(BaseRepo):
    model = Task

    async def get(self, task_id: int) -> Task | None:
        return await self._get_model(self.model, model_id=task_id)

    async def get_all(self, conditions: list[Any] = None) -> Sequence[Task]:
        return await self._get_model_all(self.model, conditions)

    async def create(self, task_id) -> Task:
        return await self._create_model(self.model, task_id)

    async def update(self, task_in) -> Task:
        return await self._update_model(self.model, task_in)

    async def update_partial(self, task_in) -> Task:
        return await self._update_partial_model(self.model, task_in)

    async def delete(self, task_id: int) -> None:
        task = await self.get(task_id)
        return await self._delete_model(task)

    ### SPECIFIC ###
    async def get_by_folder(self, folder_id: int) -> Sequence[Task]:
        return await self._get_model_all(self.model, conditions=[self.model.folder_id == folder_id])

    async def get_by_user(self, user_id: int) -> Sequence[Task]:
        return await self._get_model_all(self.model, conditions=[self.model.user_id == user_id])

    async def get_with_folder_user(self, task_id: int) -> Task | None:
        return await self._get_model_with(
            model=self.model,
            options={'selectinload': [self.model.folder, self.model.user]},
            conditions=[self.model.id == task_id]
        )

    async def get_all_with_folder_user(self) -> Sequence[Task]:
        return await self._get_model_with(
            model=self.model,
            options={'selectinload': [self.model.folder, self.model.user]},
            _all=True
        )
