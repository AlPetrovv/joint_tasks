from fastapi_users import FastAPIUsers

from users_auth.authentication.dependencies.backend import authentication_backend
from users_auth.authentication.dependencies.manager import get_auth_user_manager
from users_auth.models import AuthUser

fastapi_users_main_router = FastAPIUsers[AuthUser, int](
    get_auth_user_manager,
    [authentication_backend],
)
