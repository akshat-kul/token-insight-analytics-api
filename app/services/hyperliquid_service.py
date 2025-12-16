from collections import defaultdict
from datetime import datetime, timedelta, date, timezone

from app.clients.hyperliquid_client import HyperLiquidClient


class HyperLiquidPnLService:
    def __init__(self, client: HyperLiquidClient):
        self.client = client

    @staticmethod
    def date_to_ms(d: date) -> int:
        return int(
            datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp() * 1000
        )

    async def calculate_pnl(
        self,
        wallet: str,
        start: date,
        end: date,
        coin: str = "ETH",
    ):
        fills = await self.client.user_fills(wallet)
        start_ms = self.date_to_ms(start)
        end_ms = self.date_to_ms(end)

        try:
            funding = await self.client.funding_history(
                wallet=wallet,
                coin=coin,
                start_time_ms=start_ms,
                end_time_ms=end_ms,
            )
        except Exception:
            # fundingHistory is unreliable; treat missing funding as zero
            funding = []
            
        try:
            state = await self.client.user_state(wallet)
        except Exception:
            # Wallet has no active state (no positions / margin account)
            state = {
                "positions": [],
                "marginSummary": {
                    "accountValue": 0.0
                }
            }

        daily = defaultdict(lambda: {
            "realized": 0.0,
            "fees": 0.0,
            "funding": 0.0,
        })

        # ---- Fills → realized + fees ----
        for f in fills:
            d = datetime.utcfromtimestamp(f["time"] / 1000).date()
            if start <= d <= end:
                daily[d]["realized"] += float(f.get("pnl", 0))
                daily[d]["fees"] += abs(float(f.get("fee", 0)))

        # ---- Funding ----
        for f in funding:
            d = datetime.utcfromtimestamp(f["time"] / 1000).date()
            if start <= d <= end:
                daily[d]["funding"] += float(f.get("payment", 0))

        # ---- Snapshot values ----
        unrealized = sum(
            float(p.get("unrealizedPnl", 0))
            for p in state.get("positions", [])
        )

        equity = float(
            state.get("marginSummary", {}).get("accountValue", 0)
        )

        results = []
        cur = start

        while cur <= end:
            r = daily[cur]["realized"]
            f = daily[cur]["fees"]
            fu = daily[cur]["funding"]

            net = r + unrealized - f + fu

            results.append({
                "date": cur,
                "realized_pnl_usd": round(r, 4),
                "unrealized_pnl_usd": round(unrealized, 4),
                "fees_usd": round(f, 4),
                "funding_usd": round(fu, 4),
                "net_pnl_usd": round(net, 4),
                "equity_usd": round(equity, 4),
            })

            cur += timedelta(days=1)

        summary = {
            "total_realized_usd": sum(d["realized_pnl_usd"] for d in results),
            "total_unrealized_usd": unrealized,
            "total_fees_usd": sum(d["fees_usd"] for d in results),
            "total_funding_usd": sum(d["funding_usd"] for d in results),
            "net_pnl_usd": sum(d["net_pnl_usd"] for d in results),
        }

        return {
            "daily": results,
            "summary": summary,
        }
