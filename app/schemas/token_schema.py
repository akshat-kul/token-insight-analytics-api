from pydantic import BaseModel
from typing import Optional

# ----------------------------
# Request Schema
# ----------------------------
class TokenInsightRequest(BaseModel):
    vs_currency: Optional[str] = "usd"
    history_days: Optional[int] = 30