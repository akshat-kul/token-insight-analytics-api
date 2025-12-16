import json
import httpx

from app.utils.config import settings
from app.schemas.ai_schema import AIInsightResponse


class AIClient:
    """
    Hugging Face Router - Chat Completions client
    (OpenAI-compatible)
    """

    def __init__(self):
        if settings.AI_PROVIDER != "huggingface":
            raise RuntimeError("Only Hugging Face provider is supported")

        if not settings.HF_API_TOKEN:
            raise RuntimeError("HF_API_TOKEN is not configured")

        self.provider = "huggingface"
        self.model = settings.HF_MODEL

        self._client = httpx.AsyncClient(
            base_url=settings.HF_BASE_URL,
            headers={
                "Authorization": f"Bearer {settings.HF_API_TOKEN}",
                "Content-Type": "application/json",
            },
            timeout=60,
        )

    async def generate_insight(self, prompt: str) -> dict:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a crypto market analyst. "
                        "Respond ONLY with valid JSON. No markdown. No extra text."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "temperature": 0.2,
        }

        resp = await self._client.post(
            "/v1/chat/completions",
            json=payload,
        )

        if resp.status_code != 200:
            raise RuntimeError(
                f"HuggingFace API error {resp.status_code}: {resp.text}"
            )

        data = resp.json()

        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            raise RuntimeError(
                f"Unexpected HF response format: {data}"
            )

        # STRICT JSON parsing
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            raise RuntimeError(
                f"AI returned non-JSON output: {content}"
            )

        validated = AIInsightResponse(**parsed)
        return validated.model_dump()
