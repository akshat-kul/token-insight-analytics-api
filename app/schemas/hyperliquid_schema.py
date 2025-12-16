from pydantic import BaseModel
from datetime import date
from typing import List


class DailyPnL(BaseModel):
    date: date
    realized_pnl_usd: float
    unrealized_pnl_usd: float
    fees_usd: float
    funding_usd: float
    net_pnl_usd: float
    equity_usd: float


class HyperLiquidPnLResponse(BaseModel):
    wallet: str
    start: date
    end: date
    daily: List[DailyPnL]
    summary: dict
    diagnostics: dict
