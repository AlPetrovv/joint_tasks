from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from announcements.api.handlers import router as announcements_api_router
from announcements.handlers import form_router as announcements_form_router
from announcements.handlers import router as announcements_router
from config import settings

from folders.api.handlers import router as folders_api_router
from folders.handlers import form_router as folders_form_router
from folders.handlers import router as folders_router

from main_page import router as main_page_router

from tasks.api.handlers import router as tasks_api_router
from tasks.handlers import form_router as tasks_form_router
from tasks.handlers import router as tasks_router

from profiles.api.handlers import router as profiles_api_router
from profiles.handlers import form_router as profiles_form_router
from profiles.handlers import router as profiles_router

from users.handlers import auth_router as fastapi_users_auth_router
from users.handlers import router as api_users_router

http_error = HTTPBearer(auto_error=False)

router = APIRouter(prefix="/api/jt")
form_router = APIRouter(prefix="/api/jt")
api_router = APIRouter(prefix="/api", dependencies=[Depends(http_error)])
auth_router = APIRouter(prefix=settings.api.prefix)

auth_router.include_router(fastapi_users_auth_router)

form_router.include_router(tasks_form_router)
form_router.include_router(profiles_form_router)
form_router.include_router(folders_form_router)
form_router.include_router(announcements_form_router)

router.include_router(main_page_router)
router.include_router(tasks_router)
router.include_router(profiles_router)
router.include_router(folders_router)
router.include_router(announcements_router)

api_router.include_router(tasks_api_router)
api_router.include_router(profiles_api_router)
api_router.include_router(folders_api_router)
api_router.include_router(announcements_api_router)
api_router.include_router(api_users_router)
