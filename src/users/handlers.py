from fastapi import APIRouter

from config import settings
from users.authentication.fastapi_users import fastapi_users_main_router
from users.authentication.dependencies.backend import authentication_backend
from users.schemas import UserRead, UserCreate

auth_router = APIRouter(prefix=settings.api.auth, tags=['Auth'])

# login and logout
auth_router.include_router(fastapi_users_main_router.get_auth_router(authentication_backend))
# register
auth_router.include_router(
    fastapi_users_main_router.get_register_router(UserRead, UserCreate),
)

