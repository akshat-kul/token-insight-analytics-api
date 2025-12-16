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
- Clone the repo
```bash
git clone https://github.com/<your-username>/token-insight-analytics-api.git
cd token-insight-analytics-api
```
