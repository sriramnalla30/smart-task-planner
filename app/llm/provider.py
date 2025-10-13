from __future__ import annotations

import abc
from typing import Any, Dict, List, Optional


class LLMProvider(abc.ABC):
    """Abstract base class for large language model integrations."""

    @abc.abstractmethod
    async def generate_plan(self, prompt: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Return structured plan data following the supplied schema."""

    @abc.abstractmethod
    def name(self) -> str:
        """Human-friendly provider label."""


class MockPlanner(LLMProvider):
    """Deterministic fallback planner used when no API key is available."""

    async def generate_plan(self, prompt: str, schema: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "metadata": {
                "planning_strategy": "rule-based prototype",
                "assumptions": [
                    "Using mock planner because LLM credentials were unavailable.",
                    "Timeline evenly distributed across requested horizon.",
                ],
            },
            "tasks": [
                {
                    "id": "T1",
                    "title": "Clarify goal success criteria",
                    "description": "Interview stakeholders to capture expectations and constraints.",
                    "duration_days": 2,
                },
                {
                    "id": "T2",
                    "title": "Draft milestone roadmap",
                    "description": "Translate success criteria into phased deliverables with checkpoints.",
                    "depends_on": ["T1"],
                    "duration_days": 3,
                },
                {
                    "id": "T3",
                    "title": "Assemble execution squad",
                    "description": "Assign accountable owners and confirm resource availability.",
                    "depends_on": ["T2"],
                    "duration_days": 2,
                },
            ],
        }

    def name(self) -> str:
        return "mock-planner"
