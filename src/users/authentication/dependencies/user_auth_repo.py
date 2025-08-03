from typing import Annotated, TYPE_CHECKING

from fastapi import Depends
from users.authentication.dependencies import get_user_repo
from users.authentication.repo import UserAuthRepo

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


def get_auth_user_repo(users_db: Annotated["SQLAlchemyUserDatabase", Depends(get_user_repo)]):
    """Get user manager dependency repo with logic for register, login, reset password etc"""
    yield UserAuthRepo(users_db)
