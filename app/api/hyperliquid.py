from fastapi import APIRouter, Query
from datetime import date

from app.clients.hyperliquid_client import HyperLiquidClient
from app.services.hyperliquid_service import HyperLiquidPnLService

router = APIRouter()

client = HyperLiquidClient()
service = HyperLiquidPnLService(client)


@router.get("/{wallet}/pnl")
async def wallet_pnl(
    wallet: str,
    start: date = Query(...),
    end: date = Query(...),
):
    result = await service.calculate_pnl(wallet, start, end)

    return {
        "wallet": wallet,
        "start": start,
        "end": end,
        **result,
        "diagnostics": {
            "data_source": "hyperliquid_info_endpoint",
            "notes": "Unrealized PnL is a snapshot from current open positions",
        },
    }
