from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.token import router as token_router
from app.api.hyperliquid import router as hyperliquid_router
from app.utils.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(token_router, prefix="/api/token", tags=["Token Insight"])
    app.include_router(
        hyperliquid_router, prefix="/api/hyperliquid", tags=["HyperLiquid PnL"]
    )

    @app.get("/health")
    async def health():
        return {
            "status": "ok",
            "env": settings.APP_ENV,
        }

    return app


app = create_app()
