from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(tokenUrl="v1/auth/login")
