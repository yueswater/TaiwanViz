"""
FastAPI application entrypoint for TaiwanViz.

This app exposes endpoints to:
- Render choropleth maps as images (PNG)
- Inspect available color palettes
- List packaged fonts and health status
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import maps, meta
from .startup import on_shutdown, on_startup


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    on_startup()
    yield
    # Shutdown
    on_shutdown()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns
    -------
    FastAPI
        Configured FastAPI instance.
    """
    app = FastAPI(
        title="TaiwanViz API",
        version="0.1.0",
        description="REST API for rendering Taiwan choropleth maps.",
        lifespan=lifespan,
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(meta.router, prefix="/meta", tags=["meta"])
    app.include_router(maps.router, prefix="/render", tags=["render"])

    return app


app = create_app()
