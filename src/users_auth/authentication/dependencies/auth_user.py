from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from db.helper import db_helper
from users_auth.models import AuthUser

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_auth_user_repo(session: Annotated["AsyncSession", Depends(db_helper.session_dependency)]):
    """Get user repo dependency"""
    yield AuthUser.get_repo(session)
