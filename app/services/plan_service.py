from __future__ import annotations

import logging
from datetime import date
from typing import Dict, Optional

from app.config import get_settings
from app.llm.gemini import GeminiPlanner
from app.llm.provider import LLMProvider, MockPlanner
from app.schemas import PlanMetadata, PlanRequest, PlanResponse, Task
from app.utils.timeline import backfill_dates
from app.utils.validation import validate_dependencies, validate_timeline

logger = logging.getLogger(__name__)


class PlanService:
    """Coordinates prompt construction, LLM calls, and post-processing."""

    def __init__(self, provider: Optional[LLMProvider] = None) -> None:
        self._settings = get_settings()
        if provider is not None:
            self._provider = provider
        else:
            self._provider = self._resolve_provider()

    def _resolve_provider(self) -> LLMProvider:
        if self._settings.gemini_api_key and not self._settings.enable_mock_mode:
            return GeminiPlanner(
                api_key=self._settings.gemini_api_key,
                model=self._settings.gemini_model,
            )
        return MockPlanner()

    async def generate(self, payload: PlanRequest) -> PlanResponse:
        logger.info(f"Generating plan for goal: {payload.goal[:50]}...")
        
        prompt = self._build_prompt(payload)
        schema = self._target_schema()
        
        try:
            raw = await self._provider.generate_plan(prompt, schema)
        except Exception as e:
            logger.error(f"LLM provider failed: {e}")
            raise ValueError(f"Failed to generate plan: {str(e)}")
        
        # Handle case where LLM might return unexpected format
        if isinstance(raw, list):
            logger.warning("LLM returned list instead of dict, wrapping in structure")
            raw = {"tasks": raw, "metadata": {}}
        
        tasks = [Task.model_validate(task) for task in raw.get("tasks", [])]
        logger.info(f"Generated {len(tasks)} tasks from LLM")

        today = date.today()
        fallback_start = today
        horizon = payload.horizon_days or self._settings.default_horizon_days
        if payload.target_date:
            horizon = max((payload.target_date - today).days, 1)
            fallback_start = today
        tasks = backfill_dates(tasks, fallback_start=fallback_start, horizon_days=horizon)
        
        # Validate task dependencies and timelines
        try:
            validate_dependencies(tasks)
            conflicts = validate_timeline(tasks)
            if conflicts:
                logger.warning(f"Timeline conflicts detected: {conflicts}")
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            # Continue with plan but log the issue

        metadata = PlanMetadata(
            goal=payload.goal,
            planning_strategy=raw.get("metadata", {}).get("planning_strategy"),
            assumptions=raw.get("metadata", {}).get("assumptions", []),
            horizon_days=horizon,
        )
        
        logger.info("Plan generation completed successfully")
        return PlanResponse(metadata=metadata, tasks=tasks)

    def provider_name(self) -> str:
        return self._provider.name()

    def _build_prompt(self, payload: PlanRequest) -> str:
        target_clause = (
            f"The user needs this done by {payload.target_date.isoformat()}."
            if payload.target_date
            else ""
        )
        horizon_clause = (
            f"Assume a planning horizon of {payload.horizon_days} days."
            if payload.horizon_days
            else f"Assume a planning horizon of {self._settings.default_horizon_days} days."
        )
        guidance_clause = (
            f"Additional context: {payload.guidance}." if payload.guidance else ""
        )

        return f"""You are an expert execution strategist AI. Break down the following goal into a realistic, dependency-aware action plan.

Goal: {payload.goal}
{target_clause}
{horizon_clause}
{guidance_clause}

Return ONLY valid JSON with this exact structure:
{{
  "metadata": {{
    "planning_strategy": "brief description of your planning approach",
    "assumptions": ["assumption 1", "assumption 2"]
  }},
  "tasks": [
    {{
      "id": "T1",
      "title": "Task title",
      "description": "Detailed description",
      "owner": "Role (optional)",
      "start_date": "2025-10-13",
      "due_date": "2025-10-15",
      "duration_days": 2,
      "depends_on": [],
      "confidence": 0.85,
      "reference_links": ["https://example.com/tutorial1", "https://example.com/docs"]
    }}
  ]
}}

Requirements:
- Use ISO format (YYYY-MM-DD) for all dates
- Task IDs must be unique (T1, T2, T3, etc.)
- Dependencies must reference valid task IDs that come before
- Confidence is a float between 0.0 and 1.0
- Ensure logical task ordering and realistic timelines
- Include 5-10 meaningful tasks that cover the complete goal
- For each task, provide 1-3 helpful reference_links to tutorials, documentation, guides, or tools that would help someone complete that task
- Reference links should be real, publicly accessible URLs (documentation sites, tutorial sites, tool websites, etc.)
- Prioritize official documentation, popular tutorials, and widely-used resources"""

    def _target_schema(self) -> Dict[str, str]:
        return {
            "metadata": "object",
            "tasks": "array",
        }
