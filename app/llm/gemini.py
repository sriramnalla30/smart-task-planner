from __future__ import annotations

import asyncio
import json
from typing import Any, Dict, Optional

import google.generativeai as genai

from app.llm.provider import LLMProvider


class GeminiPlanner(LLMProvider):
    """Gemini implementation that asks the model for structured task plans."""

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-2.0-flash-exp",
        temperature: float = 0.4,
    ) -> None:
        genai.configure(api_key=api_key)
        self._model_name = model
        self._temperature = temperature
        self._model = genai.GenerativeModel(model)

    async def generate_plan(self, prompt: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        generation_config = {
            "temperature": self._temperature,
            "response_mime_type": "application/json",
            "max_output_tokens": 2048,
        }

        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self._model.generate_content(prompt, generation_config=generation_config),
        )

        try:
            return json.loads(response.text)
        except (json.JSONDecodeError, AttributeError) as exc:
            raise ValueError("Gemini response was not valid JSON.") from exc

    def name(self) -> str:
        return self._model_name
