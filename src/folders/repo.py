from typing import Sequence, Any

from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import selectinload

from core.repo import BaseRepo
from folders.models import Folder
from tasks.models import Task


class FolderRepo(BaseRepo):
    model = Folder

    async def get(self, folder_id: int) -> Folder | None:
        return await self._get_model(self.model, model_id=folder_id)

    async def get_all(self, conditions: list[Any] = None) -> Sequence[Folder]:
        return await self._get_model_all(self.model, conditions)

    async def create(self, folder_in) -> Folder:
        return await self._create_model(self.model, folder_in)

    async def get_with_tasks_and_user(self, folder_id: int) -> Folder | None:
        smtp = select(self.model).options(
            selectinload(self.model.tasks).options(
                selectinload(Task.user)
            )
        ).where(self.model.id == folder_id)

        scalar_result: ScalarResult[FolderRepo.model] = await self.session.scalars(smtp)
        return scalar_result.one_or_none()
