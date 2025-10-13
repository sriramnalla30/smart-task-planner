from __future__ import annotations

from datetime import date, timedelta
from typing import Iterable, List

from app.schemas import Task


def backfill_dates(tasks: Iterable[Task], fallback_start: date, horizon_days: int) -> List[Task]:
    """Ensure every task has dates within the planning horizon.

    When the language model omits scheduling data, we distribute remaining tasks evenly
    across the available timeline while respecting declared dependencies.
    """

    scheduled: List[Task] = []
    remaining_days = max(horizon_days, 1)
    tasks_list = list(tasks)
    unscheduled = [task for task in tasks_list if not task.start_date or not task.due_date]

    if not unscheduled:
        return tasks_list

    slot = max(1, remaining_days // max(len(unscheduled), 1))
    current_start = fallback_start

    for task in tasks_list:
        if task in unscheduled:
            start = task.start_date or current_start
            duration = task.duration_days or slot
            due = task.due_date or start + timedelta(days=duration)
            if due < start:
                due = start + timedelta(days=max(duration, 1))
            scheduled.append(task.copy(update={"start_date": start, "due_date": due}))
            current_start = due + timedelta(days=1)
        else:
            scheduled.append(task)

    return scheduled
