from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastui import prebuilt_html
from starlette.responses import RedirectResponse

from routers import api_router, form_router, router

app = FastAPI(
    title="Joint Task API",
    description="Welcome to the Joint Task API"
)


@app.middleware("http")
async def redirect_to_main_page(request: Request, call_next):
    path = request.url.path
    if path == '/':
        return RedirectResponse(url='/jt/', status_code=302, headers=request.headers)
    return await call_next(request)


app.include_router(router)
app.include_router(form_router)
app.include_router(api_router)


@app.get('/jt/{path:path}')
async def html_landing_jt() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='TOC'))


#
@app.get('/api/jt/{path:path}')
async def html_landing_jt_api() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='TOC'))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
