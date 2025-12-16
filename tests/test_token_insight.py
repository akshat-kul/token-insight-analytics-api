from unittest.mock import AsyncMock, patch
import pytest


@pytest.mark.asyncio
async def test_token_insight_success(async_client):
    payload = {
        "vs_currency": "usd",
        "history_days": 7,
    }

    mocked_response = {
        "source": "coingecko",
        "token": {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "market_data": {
                "current_price_usd": 50000,
                "market_cap_usd": 1000000000,
                "total_volume_usd": 50000000,
                "price_change_percentage_24h": 1.2,
            },
        },
        "insight": {
            "reasoning": "Market looks stable",
            "sentiment": "Neutral",
        },
        "model": {
            "provider": "huggingface",
            "model": "mistral",
        },
    }

    with patch(
        "app.services.token_insight_service.TokenInsightService.generate_insight",
        new_callable=AsyncMock,
    ) as mock_generate:
        mock_generate.return_value = mocked_response

        resp = await async_client.post(
            "/api/token/bitcoin/insight",
            json=payload,
        )

    assert resp.status_code == 200
    assert resp.json()["insight"]["sentiment"] == "Neutral"
