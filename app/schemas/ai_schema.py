from pydantic import BaseModel, Field


class AIInsightResponse(BaseModel):
    reasoning: str = Field(..., min_length=5)
    sentiment: str = Field(..., pattern="^(Bullish|Bearish|Neutral)$")
