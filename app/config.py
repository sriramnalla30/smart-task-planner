from __future__ import annotations

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = Field(default="Smart Task Planner API")
    gemini_api_key: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
    gemini_model: str = Field(
        default="gemini-2.0-flash-exp",
        description="Gemini model to use. Options: gemini-2.0-flash-exp, gemini-1.5-pro, gemini-1.5-flash",
    )
    default_horizon_days: int = Field(default=21, ge=1, description="Fallback planning horizon")
    enable_mock_mode: bool = Field(
        default=False,
        alias="SMART_TASK_PLANNER_MOCK",
        description="Use mock planner when true or when API key missing.",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
