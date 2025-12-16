from fastapi import APIRouter

from app.schemas.token_schema import TokenInsightRequest
from app.services.token_insight_service import TokenInsightService
from app.clients.coingecko_client import CoinGeckoClient
from app.clients.ai_client import AIClient

router = APIRouter()

# ---- Create dependencies ONCE ----
coingecko_client = CoinGeckoClient()
ai_client = AIClient()

token_insight_service = TokenInsightService(
    coingecko=coingecko_client,
    ai_client=ai_client,
)

@router.post("/{token_id}/insight")
async def token_insight(
    token_id: str,
    payload: TokenInsightRequest,
):
    return await token_insight_service.generate_insight(
        token_id,
        payload.vs_currency,
        payload.history_days,
    )
