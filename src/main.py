import inspect
from contextlib import asynccontextmanager

from sqlalchemy import select, func

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html
from sqlalchemy.orm import relationship
from starlette.responses import RedirectResponse

from db.helper import db_helper
from routers import api_router, form_router, router, auth_router
from users.models import User




@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


main_app = FastAPI(title="Joint Task API", description="Welcome to the Joint Task API", lifespan=lifespan)

@main_app.middleware("http")
async def redirect_to_main_page(request: Request, call_next):
    path = request.url.path
    if path == "/":
        return RedirectResponse(url="/jt/", status_code=302, headers=request.headers)
    return await call_next(request)


main_app.include_router(router)
main_app.include_router(form_router)
main_app.include_router(api_router)
main_app.include_router(auth_router)

@main_app.get("/jt/{path:path}")
async def html_landing_jt() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="TOC"))


#
@main_app.get("/api/jt/{path:path}")
async def html_landing_jt_api() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="TOC"))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
