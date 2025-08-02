import logging
from typing import TYPE_CHECKING, Optional

from fastapi_users import BaseUserManager, IntegerIDMixin

from config import settings

from ..models import AuthUser

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class AuthUserManager(
    IntegerIDMixin, BaseUserManager[AuthUser, int]
):  # todo : int as type (UserIdType)
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self, user: AuthUser, request: Optional["Request"] = None
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
