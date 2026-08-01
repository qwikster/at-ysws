import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from at.config import config

logger = logging.getLogger("uvicorn.error")

if config().devmode:
    BUILD_DIR = Path(__file__).resolve().parent.parent.parent.parent / "frontend" / "build"
else:
    BUILD_DIR = Path(__file__).resolve().parent.parent.parent / "build"

def api_routes(app: FastAPI):
    # app.include_router(bnuuy.router, prefix="/api/bnuuy")
    pass

def app_routes(app: FastAPI):
    @app.get("/projects/{id}")
    async def projects(id: int): # id detected by sveltekit
        return FileResponse(BUILD_DIR / "app.html")

    @app.get("/users/{id}")
    async def users(id: int):
        return FileResponse(BUILD_DIR / "app.html")

    app.mount("/", StaticFiles(directory=BUILD_DIR, html = True), name = "frontend")

def create_app() -> FastAPI:
    app = FastAPI()
    api_routes(app)
    if BUILD_DIR.exists():
        app_routes(app)
    else:
        logger.error(f"No build found at {BUILD_DIR}, / will not contain app")
    return app


def entry():
    if config().devmode:
        uvicorn.run(
            "at.main:create_app",
            host = config().host,
            port = config().port,
            reload = True,
            factory = True,
            log_level = "info"
        )
    else:
        uvicorn.run(
            "at.main:create_app",
            host = config().host,
            port = config().port,
            reload = False,
            factory = True,
            log_level = "info"
        )

if __name__ == "__main__":
    entry()
