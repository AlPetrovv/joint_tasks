from fastapi import APIRouter

from config import settings
from users_auth.authentication.fastapi_users import fastapi_users_main_router
from users_auth.authentication.dependencies.backend import authentication_backend
from users_auth.schemas import AuthUserRead, AuthUserCreate

auth_router = APIRouter(prefix=settings.api.auth, tags=['Auth'])

# login and logout
auth_router.include_router(fastapi_users_main_router.get_auth_router(authentication_backend))
# register
auth_router.include_router(
    fastapi_users_main_router.get_register_router(AuthUserRead, AuthUserCreate),
)

