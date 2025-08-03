from fastapi_users import FastAPIUsers

from users._types import UserIDType
from users.authentication.dependencies.backend import authentication_backend
from users.authentication.dependencies.user_auth_repo import get_auth_user_repo
from users.models import User

fastapi_users_main_router = FastAPIUsers[User, UserIDType](
    get_auth_user_repo,
    [authentication_backend],
)
