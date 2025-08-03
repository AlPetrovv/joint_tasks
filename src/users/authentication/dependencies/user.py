from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from db.helper import db_helper
from users.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_repo(session: Annotated["AsyncSession", Depends(db_helper.session_dependency)]):
    """Get user repo dependency"""
    yield User.get_repo(session)
