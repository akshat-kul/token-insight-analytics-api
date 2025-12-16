import httpx
from app.utils.config import settings

class CoinGeckoClient:
    def __init__(self):
        headers = {}

        # if settings.COINGECKO_API_KEY:
        #     headers["x-cg-pro-api-key"] = settings.COINGECKO_API_KEY

        self._client = httpx.AsyncClient(
            base_url=settings.COINGECKO_BASE_URL,
            headers=headers,
            timeout=10,
        )

    async def fetch_token(self, token_id: str) -> dict:
        resp = await self._client.get(
            f"/coins/{token_id}",
            params={
                "localization": "false",
                "tickers": "false",
                "market_data": "true",
                "community_data": "false",
                "developer_data": "false",
            },
        )

        if resp.status_code != 200:
            raise RuntimeError("CoinGecko token fetch failed")

        return resp.json()

    async def fetch_market_chart(
        self, token_id: str, vs_currency: str, days: int
    ) -> dict:
        resp = await self._client.get(
            f"/coins/{token_id}/market_chart",
            params={
                "vs_currency": vs_currency.lower(),
                "days": days,
            },
        )

        if resp.status_code != 200:
            raise RuntimeError(
                f"CoinGecko market_chart failed "
                f"(status={resp.status_code}): {resp.text}"
            )

        return resp.json()
