from __future__ import annotations

import asyncio
from datetime import date

from app.schemas import PlanRequest
from app.services.plan_service import PlanService


def test_mock_plan_contains_tasks(monkeypatch):
    monkeypatch.setenv("SMART_TASK_PLANNER_MOCK", "true")
    service = PlanService()
    payload = PlanRequest(goal="Ship a demo", horizon_days=7)
    response = asyncio.run(service.generate(payload))

    assert response.metadata.goal == "Ship a demo"
    assert len(response.tasks) >= 1
    assert all(task.id for task in response.tasks)
    assert all(task.due_date is not None for task in response.tasks)
