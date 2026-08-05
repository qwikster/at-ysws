import logging
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import at.db.models  # noqa: F401
from at.api import auth
from at.config import config
from at.db import Base, engine

logger = logging.getLogger("uvicorn.error")

if config().devmode:
    BUILD_DIR = Path(__file__).resolve().parent.parent.parent.parent / "frontend" / "build"
else:
    BUILD_DIR = Path(__file__).resolve().parent.parent.parent / "build"

@asynccontextmanager
async def lifespan(app: FastAPI):
    if config().devmode:
        async with engine.begin() as db:
            logger.info("Creating tables in database")
            await db.run_sync(Base.metadata.create_all)
    yield

def api_routes(app: FastAPI):
    # app.include_router(bnuuy.router, prefix="/api/bnuuy")
    app.include_router(auth.router, prefix="/api/auth")

def app_routes(app: FastAPI):
    @app.get("/projects/{id}")
    async def projects(id: int): # id detected by sveltekit
        return FileResponse(BUILD_DIR / "app.html")

    @app.get("/users/{id}")
    async def users(id: int):
        return FileResponse(BUILD_DIR / "app.html")

    app.mount("/", StaticFiles(directory=BUILD_DIR, html = True), name = "frontend")

def create_app() -> FastAPI:
    app = FastAPI(lifespan = lifespan)
    api_routes(app)
    if BUILD_DIR.exists():
        app_routes(app)
    else:
        logger.warning(f"No build found at {BUILD_DIR}, / will not contain app")
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
