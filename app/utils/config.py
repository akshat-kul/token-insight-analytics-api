from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ------------------
    # App
    # ------------------
    APP_NAME: str = Field(default="token-insight-analytics-api")
    APP_ENV: str = Field(default="development")
    DEBUG: bool = Field(default=False)

    # ------------------
    # AI
    # ------------------
    AI_PROVIDER: str = Field(default="mock")
    HF_API_TOKEN: str | None = None
    HF_MODEL: str = Field(default="mistralai/Mistral-7B-Instruct-v0.2")
    HF_BASE_URL: str

    COINGECKO_BASE_URL: str
    COINGECKO_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# Singleton settings object
settings = Settings()
