from typing import Any, Sequence

from sqlalchemy import ScalarResult, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from _types import MODEL, TYPE_MODEL


class BaseRepo:
    model: TYPE_MODEL

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_model(
        self, model: TYPE_MODEL, model_id: int, conditions: list[Any] = None
    ) -> MODEL | None:
        smtp = select(model).where(model.id == model_id)
        if conditions is not None:
            smtp = smtp.where(*conditions)
        return await self.session.scalar(smtp)

    async def _get_model_all(
        self, model: TYPE_MODEL, conditions: list[Any] = None
    ) -> Sequence[MODEL]:
        smtp = select(model)
        if conditions is not None:
            smtp = smtp.where(*conditions)
        result: ScalarResult[MODEL] = await self.session.scalars(smtp)
        return result.all()

    async def _create_model(self, model: TYPE_MODEL, model_in) -> MODEL:
        instance = model(**model_in.model_dump(exclude_unset=True))
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def _update_partial_model(self, model: TYPE_MODEL, model_in) -> MODEL:
        instance = await self._get_model(model, model_in.id)
        for field, value in model_in.model_dump(exclude_unset=True).items():
            setattr(instance, field, value)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def _update_model(self, model: TYPE_MODEL, model_in) -> MODEL:
        instance = model(**model_in.model_dump())
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def _delete_model(self, instance) -> None:
        await self.session.delete(instance)
        await self.session.commit()

    async def _get_model_with(
        self,
        model: TYPE_MODEL,
        options: dict[str, list[Any]],
        conditions: list[Any] = None,
        _all: bool = None,
    ) -> Sequence[MODEL] | MODEL | None:
        smtp = select(model).options(
            *[selectinload(rel_model) for rel_model in options.get("selectinload", [])],
            *[joinedload(rel_model) for rel_model in options.get("joinedload", [])],
        )
        if conditions is not None:
            smtp = smtp.where(*conditions)
        if _all:
            scalar_result: ScalarResult[MODEL] = await self.session.scalars(smtp)
            return scalar_result.all()

        return await self.session.scalar(smtp)
