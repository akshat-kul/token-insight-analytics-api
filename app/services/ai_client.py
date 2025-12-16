import json


class AIClient:
    async def generate_insight(self, prompt: str) -> dict:
        """
        Mock AI response.
        Replace with OpenAI / HF later.
        """

        # This MUST be valid JSON (simulate real AI discipline)
        response = {
            "reasoning": "Based on recent market data, the asset shows moderate volatility with stable volume.",
            "sentiment": "Neutral",
        }

        # Simulate strict JSON validation
        json.dumps(response)

        return response
