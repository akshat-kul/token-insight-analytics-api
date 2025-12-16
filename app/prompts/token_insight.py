def build_token_insight_prompt(
    name: str,
    symbol: str,
    market_data: dict,
    recent_prices: list,
) -> str:
    return f"""
You are a professional crypto market analyst.

Analyze the following token and return ONLY a valid JSON object.
DO NOT add explanations or markdown.
DO NOT add extra text.

Token: {name} ({symbol})
Price (USD): {market_data['current_price_usd']}
Market Cap (USD): {market_data['market_cap_usd']}
24h Change (%): {market_data['price_change_percentage_24h']}

Recent price samples:
{recent_prices}

Required JSON format:
{{
  "reasoning": "short market insight",
  "sentiment": "Bullish | Bearish | Neutral"
}}
"""
