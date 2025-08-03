import logging
from typing import TYPE_CHECKING, Optional

from fastapi_users import BaseUserManager, IntegerIDMixin

from users._types import UserIDType
from config import settings

from users.models import User

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserAuthRepo(
    IntegerIDMixin, BaseUserManager[User, UserIDType]
):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self, user: User, request: Optional["Request"] = None
    ):
        log.warning(f"User {user.id} has registered.")

    # async def on_after_forgot_password(
    #     self, user: AuthUser, token: str, request: Optional["Request"] = None
    # ):
    #     log.warning(f"User {user.id} has forgot their password. Reset token: {token}")
    #
    # async def on_after_request_verify(
    #     self, user: AuthUser, token: str, request: Optional["Request"] = None
    # ):
    #     log.warning(
    #         f"Verification requested for user {user.id}. Verification token: {token}"
    #     )
