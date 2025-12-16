import httpx
from app.utils.config import settings

COINGECKO_BASE_URL = settings.COINGECKO_BASE_URL


class CoinGeckoService:
    def __init__(self):
        headers = {}
        if settings.COINGECKO_API_KEY:
            headers["x-cg-pro-api-key"] = settings.COINGECKO_API_KEY

        self.client = httpx.AsyncClient(
            base_url=COINGECKO_BASE_URL,
            headers=headers,
            timeout=10,
        )

    async def get_token_metadata(self, token_id: str):
        resp = await self.client.get(
            f"/coins/{token_id}",
            params={
                "localization": "false",
                "tickers": "false",
                "market_data": "true",
                "community_data": "false",
                "developer_data": "false",
                "sparkline": "false",
            },
        )

        if resp.status_code != 200:
            raise ValueError(f"CoinGecko error: {resp.text}")

        data = resp.json()
        market = data["market_data"]

        return {
            "id": data["id"],
            "symbol": data["symbol"],
            "name": data["name"],
            "market_data": {
                "current_price_usd": market["current_price"].get("usd"),
                "market_cap_usd": market["market_cap"].get("usd"),
                "total_volume_usd": market["total_volume"].get("usd"),
                "price_change_percentage_24h": market.get(
                    "price_change_percentage_24h"
                ),
            },
        }

    async def get_market_chart(
        self, token_id: str, vs_currency: str, days: int
    ):
        resp = await self.client.get(
            f"/coins/{token_id}/market_chart",
            params={
                "vs_currency": vs_currency,
                "days": days,
            },
        )

        if resp.status_code != 200:
            raise ValueError("Failed to fetch market chart")

        return resp.json()
