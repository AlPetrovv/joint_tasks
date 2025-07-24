from fastapi import APIRouter

from fastapi_users import fastapi_users


from announcements.api.handlers import router as announcements_api_router
from announcements.handlers import form_router as announcements_form_router
from announcements.handlers import router as announcements_router
from tasks.api.handlers import router as tasks_api_router
from tasks.handlers import form_router as tasks_form_router
from tasks.handlers import router as tasks_router
from users.api.handlers import router as users_api_router
from users.handlers import form_router as users_form_router
from users.handlers import router as users_router
from folders.api.handlers import router as folders_api_router
from folders.handlers import form_router as folders_form_router
from folders.handlers import router as folders_router
from main_page import router as main_page_router

router = APIRouter(
    prefix="/api/jt",
)

form_router = APIRouter(
    prefix="/api/jt",
)
api_router = APIRouter(
    prefix="/api",
)

form_router.include_router(tasks_form_router)
form_router.include_router(users_form_router)
form_router.include_router(folders_form_router)
form_router.include_router(announcements_form_router)

router.include_router(main_page_router)
router.include_router(tasks_router)
router.include_router(users_router)
router.include_router(folders_router)
router.include_router(announcements_router)

api_router.include_router(tasks_api_router)
api_router.include_router(users_api_router)
api_router.include_router(folders_api_router)
api_router.include_router(announcements_api_router)
