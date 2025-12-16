# 🚀 Token Insight Analytics API
- A FastAPI-based analytics service that delivers:
- Crypto token insights using CoinGecko + Hugging Face LLMs
- Hyperliquid wallet PnL analytics (realized, unrealized, fees, funding)
- Fully tested with pytest + asyncio
- Dockerized for painless local & CI usage
- This project is intentionally stateless, lightweight, and designed for analytics-first workloads.

### ✨ Features
#### Token Insight API
- Fetches live token data from CoinGecko (free tier)
- Generates AI-driven market insight using Hugging Face Inference API
- Strict schema validation (Pydantic)
- Deterministic + testable AI output

#### Hyperliquid Wallet Analytics
- Daily PnL breakdown
- Realized vs unrealized PnL
- Fees & funding impact
- Snapshot equity values

⚠️ Uses public Hyperliquid APIs only — no wallet signing, no auth, no custody

#### Engineering Highlights
- Async-first (FastAPI + httpx)
- Clean separation: api / services / clients
- External APIs fully mockable
- Zero database dependency

### 🧱 Project Structure
```text
app/
├── api/                # FastAPI routes
├── clients/            # External API clients
├── services/           # Business logic
├── schemas/            # Pydantic models
├── prompts/            # LLM prompts
├── utils/              # Config & helpers
└── main.py             # App entrypoint


tests/
├── conftest.py
├── test_health.py
├── test_hyperliquid_pnl.py
└── test_token_insight.py
```

### 🐳 Running with Docker
```bash
docker compose up --build
```
App will be available at:
```bash
http://localhost:8000
```
Swagger UI:
```bash
http://localhost:8000/docs
```
### ⚙️ Environment Variables
Create a .env file (see .env.example):

### 🧪 Running Tests
```bash
pytest -v
```
- Async mode is auto-configured via pytest.ini:

### 🔍 Example APIs
#### Token Insight
```bash
POST /api/token/{token_id}/insight
```
Payload:
```bash
{
  "vs_currency": "usd",
  "history_days": 7
}
```
#### Hyperliquid Wallet PnL
```bash
GET /api/hyperliquid/{wallet}/pnl?start=YYYY-MM-DD&end=YYYY-MM-DD
```

### 🧠 Design Philosophy
- ❌ No hidden state
- ❌ No magic globals
- ❌ No database coupling
- ✅ Testable by default
- ✅ External APIs isolated
- ✅ Ready for CI/CD

### 🛠️ Tech Stack
- Python 3.11
- FastAPI
- httpx
- Pydantic v2
- pytest + pytest-asyncio
- Docker

### 📌 Notes
1. CoinGecko free tier only (no pro key required)
2. Hugging Face used instead of OpenAI
3. Hyperliquid endpoints are read-only
