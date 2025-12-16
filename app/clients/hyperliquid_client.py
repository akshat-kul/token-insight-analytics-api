import httpx
import json

BASE_URL = "https://api.hyperliquid.xyz"


class HyperLiquidClient:
    def __init__(self):
        self._client = httpx.AsyncClient(
            base_url=BASE_URL,
            timeout=15,
        )

    async def _post(self, payload: dict, label: str):
        resp = await self._client.post("/info", json=payload)

        if resp.status_code != 200:
            raise RuntimeError(
                f"""
                    [HyperLiquid ERROR]
                    Label: {label}
                    Payload:
                    {json.dumps(payload, indent=2)}

                    Status: {resp.status_code}
                    Response:
                    {resp.text}
                    """
                )

        return resp.json()

    async def user_fills(self, wallet: str):
        return await self._post(
            {
                "type": "userFills",
                "user": wallet.lower(),
            },
            label="userFills",
        )

    
    async def funding_history(
        self,
        wallet: str,
        coin: str,
        start_time_ms: int,
        end_time_ms: int,
    ):
        return await self._post(
            {
                "type": "fundingHistory",
                "user": wallet.lower(),
                "coin": coin,
                "startTime": start_time_ms,
                "endTime": end_time_ms,
            },
            label="fundingHistory",
        )

    async def user_state(self, wallet: str):
        return await self._post(
            {
                "type": "userState",
                "user": wallet.lower(),
            },
            label="userState",
        )
