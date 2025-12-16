# 🚀 Token Insight & Analytics API

A backend service that combines real-time crypto market data, AI-generated insights, and wallet-level PnL analytics into clean, production-ready APIs.
Built with FastAPI, PostgreSQL, and modern async Python — because blocking code is for cavemen 🪨.

## ✨ Features
### Token Insight API
- Fetches live token data from CoinGecko
- Builds a structured prompt from market metrics
- Uses an AI model to generate sentiment & reasoning
- Validates AI output (strict JSON only, no hallucinated bullshit)
- Returns a clean, combined response

### HyperLiquid Wallet PnL API
- Fetches wallet activity from HyperLiquid
- Computes daily realized & unrealized PnL
- Includes fees, funding, net PnL, and equity
- Handles missing data, invalid wallets, and API failures gracefully

### 🛠 Tech Stack
- Layer	Tech: Backend	Python 3.11, FastAPI
- Database:	PostgreSQL
- ORM:	SQLAlchemy (async)
- HTTP Client: httpx
- AI Models: HuggingFace
- DevOps:	Docker, Docker Compose
- Testing:	Pytest
- API Client: Postman (optional bonus)

### 📁 Project Structure
```text
token-insight-analytics-api/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── token.py
│   │   └── hyperliquid.py
│   ├── services/
│   │   ├── coingecko.py
│   │   ├── hyperliquid.py
│   │   └── ai_client.py
│   ├── models/
│   ├── schemas/
│   ├── db/
│   └── utils/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

### ⚙️ Setup & Installation
1. Clone the repo
```bash
git clone https://github.com/<your-username>/token-insight-analytics-api.git
cd token-insight-analytics-api
```

2. Environment Variables
Create a .env file using the env.example file given

3. Run with Docker (Recommended)
```bash
docker-compose up --build
```
- API will be available at:
```bash
http://localhost:8000
```
- Swagger docs:
```bash
http://localhost:8000/docs
```

4. Run Locally (Without Docker)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### API Endpoints
#### Token Insight API
- POST /api/token/{id}/insight
Request (optional body)
```bash
{
  "vs_currency": "usd",
  "history_days": 30
}
```
Response
```bash
{
  "source": "coingecko",
  "token": {
    "id": "chainlink",
    "symbol": "link",
    "name": "Chainlink",
    "market_data": {
      "current_price_usd": 7.23,
      "market_cap_usd": 3500000000,
      "total_volume_usd": 120000000,
      "price_change_percentage_24h": -1.2
    }
  },
  "insight": {
    "reasoning": "Generic market comment",
    "sentiment": "Neutral"
  },
  "model": {
    "provider": "openai",
    "model": "gpt-4o-mini"
  }
}
```
🔹 HyperLiquid Wallet Daily PnL API

GET /api/hyperliquid/{wallet}/pnl?start=YYYY-MM-DD&end=YYYY-MM-DD

Response
{
  "wallet": "0xabc123...",
  "start": "2025-08-01",
  "end": "2025-08-03",
  "daily": [
    {
      "date": "2025-08-01",
      "realized_pnl_usd": 120.5,
      "unrealized_pnl_usd": -15.3,
      "fees_usd": 2.1,
      "funding_usd": -0.5,
      "net_pnl_usd": 102.6,
      "equity_usd": 10102.6
    }
  ],
  "summary": {
    "net_pnl_usd": 91.1
  },
  "diagnostics": {
    "data_source": "hyperliquid_api",
    "notes": "PnL calculated using daily close prices"
  }
}

🤖 AI Integration

Supports OpenAI, HuggingFace, or local LLMs

AI responses are strictly validated JSON

If AI returns garbage → request fails cleanly (no silent bullshit)

To switch providers, update .env:

AI_PROVIDER=huggingface

🧪 Tests
pytest


Includes:

API response validation

AI response parsing

PnL calculation logic

🧠 Design Decisions

Async-first architecture for performance

Service-layer abstraction (easy to swap APIs/models)

Defensive error handling

Interview-friendly but production-minded

🧾 Notes

CoinGecko API is rate-limited (free tier)

No API keys are committed

Designed to be extended with auth, caching, or persistence

🏁 Final Words

This project demonstrates:

Backend system design

External API orchestration

AI integration

Financial data computation

Clean, scalable FastAPI architecture
