from fastapi import APIRouter, Path, Query
from datetime import date

router = APIRouter()


@router.get("/{wallet}/pnl")
async def get_wallet_pnl(
    wallet: str = Path(..., description="Wallet address"),
    start: date = Query(..., description="Start date (YYYY-MM-DD)"),
    end: date = Query(..., description="End date (YYYY-MM-DD)"),
):
    """
    Fetch HyperLiquid wallet activity and calculate daily PnL.
    """

    # TEMP dummy response
    return {
        "wallet": wallet,
        "start": start,
        "end": end,
        "daily": [
            {
                "date": str(start),
                "realized_pnl_usd": 0.0,
                "unrealized_pnl_usd": 0.0,
                "fees_usd": 0.0,
                "funding_usd": 0.0,
                "net_pnl_usd": 0.0,
                "equity_usd": 0.0,
            }
        ],
        "summary": {
            "total_realized_usd": 0.0,
            "total_unrealized_usd": 0.0,
            "total_fees_usd": 0.0,
            "total_funding_usd": 0.0,
            "net_pnl_usd": 0.0,
        },
        "diagnostics": {
            "data_source": "mock",
            "notes": "Dummy response: logic not implemented yet",
        },
    }
