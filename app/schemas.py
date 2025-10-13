from __future__ import annotations

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    """Represents an individual task in the generated plan."""

    id: str = Field(..., description="Stable identifier used for dependencies")
    title: str = Field(..., description="Short, action-oriented summary")
    description: Optional[str] = Field(default=None, description="Supporting details")
    owner: Optional[str] = Field(default=None, description="Optional suggested owner role")
    start_date: Optional[date] = Field(default=None, description="Suggested start date")
    due_date: Optional[date] = Field(default=None, description="Suggested due date")
    duration_days: Optional[int] = Field(
        default=None,
        description="Planned duration in days if explicit dates unavailable.",
        ge=1,
    )
    depends_on: List[str] = Field(
        default_factory=list,
        description="List of task IDs that must be completed first.",
    )
    confidence: Optional[float] = Field(
        default=None, ge=0.0, le=1.0, description="Model confidence in task placement"
    )


class PlanMetadata(BaseModel):
    """Exposes reasoning metadata returned by the LLM."""

    goal: str
    planning_strategy: Optional[str] = None
    assumptions: List[str] = Field(default_factory=list)
    horizon_days: Optional[int] = None


class PlanRequest(BaseModel):
    """Incoming request payload."""

    goal: str = Field(..., description="High-level outcome the user wants to achieve")
    target_date: Optional[date] = Field(
        default=None, description="Absolute deadline. Overrides horizon_days when set."
    )
    horizon_days: Optional[int] = Field(
        default=None,
        ge=1,
        description="Relative planning window. Applied when target_date omitted.",
    )
    guidance: Optional[str] = Field(
        default=None,
        description="Additional context such as resources, constraints, or priorities.",
    )


class PlanResponse(BaseModel):
    """Structured response returned by the planner."""

    metadata: PlanMetadata
    tasks: List[Task]
