from typing import Annotated, TYPE_CHECKING

from fastapi import Depends
from users_auth.authentication.dependencies import get_auth_user_repo
from users_auth.authentication.manager import AuthUserManager

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


def get_auth_user_manager(users_db: Annotated["SQLAlchemyUserDatabase", Depends(get_auth_user_repo)]):
    """Get user manager dependency repo with logic for register, login, reset password etc"""
    yield AuthUserManager(users_db)
