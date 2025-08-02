from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from db.helper import db_helper
from users_auth.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_repo(
        session: Annotated["AsyncSession", Depends(db_helper.session_dependency)],
):
    """Get access token repo dependency"""
    yield AccessToken.get_repo(session)