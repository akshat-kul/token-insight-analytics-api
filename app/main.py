from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.token import router as token_router
from app.api.hyperliquid import router as hyperliquid_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Token Insight & Analytics API",
        description="AI-powered crypto insights and wallet PnL analytics",
        version="1.0.0",
    )

    # CORS (keep it open for now, tighten later)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(token_router, prefix="/api/token", tags=["Token Insight"])
    app.include_router(
        hyperliquid_router, prefix="/api/hyperliquid", tags=["HyperLiquid PnL"]
    )

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}

    return app


app = create_app()
