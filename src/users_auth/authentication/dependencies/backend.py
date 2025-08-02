from fastapi_users.authentication import AuthenticationBackend

from users_auth.authentication.dependencies import get_database_strategy
from users_auth.authentication.transport import bearer_transport

authentication_backend = AuthenticationBackend(
    name="access-tokens-db", transport=bearer_transport, get_strategy=get_database_strategy
)
