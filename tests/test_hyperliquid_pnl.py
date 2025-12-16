from unittest.mock import AsyncMock, patch
import pytest


@pytest.mark.asyncio
async def test_wallet_pnl_success(async_client):
    mocked_response = {
        "daily": [
            {
                "date": "2025-08-01",
                "realized_pnl_usd": 100,
                "unrealized_pnl_usd": 10,
                "fees_usd": 1.5,
                "funding_usd": -0.5,
                "net_pnl_usd": 108,
                "equity_usd": 10100,
            }
        ],
        "summary": {
            "total_realized_usd": 100,
            "total_unrealized_usd": 10,
            "total_fees_usd": 1.5,
            "total_funding_usd": -0.5,
            "net_pnl_usd": 108,
        },
    }

    with patch(
        "app.services.hyperliquid_service.HyperLiquidPnLService.calculate_pnl",
        new_callable=AsyncMock,
    ) as mock_calc:
        mock_calc.return_value = mocked_response

        resp = await async_client.get(
            "/api/hyperliquid/0xabc/pnl?start=2025-08-01&end=2025-08-01"
        )

    assert resp.status_code == 200
    assert "daily" in resp.json()
