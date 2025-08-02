from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from core.repo import RequestRepo
from db.helper import db_helper


async def get_repo() -> RequestRepo:
    session: AsyncSession = await db_helper.session_dependency()
    yield RequestRepo(session=session)


def set_decorator(decorator: Callable, *dec_args, **dec_kwargs) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def wrapped(*args, **kwargs):
            nonlocal decorator, dec_args, dec_kwargs
            return decorator(func, *dec_args, **dec_kwargs)(*args, **kwargs)

        return wrapped

    return wrapper
