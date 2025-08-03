import secrets
from datetime import datetime, timezone, timedelta
from typing import Annotated, TYPE_CHECKING, Any, Optional

from fastapi import Depends
from fastapi_users import models, BaseUserManager, exceptions
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from config import settings
from users.authentication.dependencies import get_access_token_repo

if TYPE_CHECKING:
    from users.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase



def get_database_strategy(
        access_token_db: Annotated["AccessTokenDatabase[AccessToken]", Depends(get_access_token_repo)]
) -> DatabaseStrategy:
    """
    Get database strategy dependency
    Database strategy - logic for working with tokens(create, destroy)
    """
    return DatabaseStrategy(
        access_token_db, lifetime_seconds=settings.access_token.lifetime_seconds
    )
