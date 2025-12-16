from app.clients.coingecko_client import CoinGeckoClient
from app.clients.ai_client import AIClient
from app.prompts.token_insight import build_token_insight_prompt

class TokenInsightService:
    def __init__(
        self,
        coingecko: CoinGeckoClient,
        ai_client: AIClient,
    ):
        self.coingecko = coingecko
        self.ai_client = ai_client

    async def generate_insight(
        self,
        token_id: str,
        vs_currency: str,
        history_days: int,
    ) -> dict:
        token_raw = await self.coingecko.fetch_token(token_id)
        chart = await self.coingecko.fetch_market_chart(
            token_id, vs_currency, history_days
        )

        market = token_raw["market_data"]

        token_data = {
            "id": token_raw["id"],
            "symbol": token_raw["symbol"],
            "name": token_raw["name"],
            "market_data": {
                "current_price_usd": market["current_price"].get("usd"),
                "market_cap_usd": market["market_cap"].get("usd"),
                "total_volume_usd": market["total_volume"].get("usd"),
                "price_change_percentage_24h": market.get(
                    "price_change_percentage_24h"
                ),
            },
        }

        prompt = build_token_insight_prompt(
            token_data["name"],
            token_data["symbol"],
            token_data["market_data"],
            chart["prices"][:10],
        )

        insight = await self.ai_client.generate_insight(prompt)

        return {
            "source": "coingecko",
            "token": token_data,
            "insight": insight,
            "model": {
                "provider": self.ai_client.provider,
                "model": self.ai_client.model,
            },
        }
