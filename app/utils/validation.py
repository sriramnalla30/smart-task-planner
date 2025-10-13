"""
Validation utilities for task plans to ensure logical consistency.
"""
from typing import List, Set, Tuple
from app.schemas import Task


class ValidationError(Exception):
    """Raised when task plan validation fails."""
    pass


def validate_dependencies(tasks: List[Task]) -> None:
    """
    Ensure all dependencies reference valid task IDs and contain no cycles.
    
    Raises:
        ValidationError: If invalid dependencies or cycles detected.
    """
    task_ids = {task.id for task in tasks}
    
    # Check all dependencies reference valid IDs
    for task in tasks:
        for dep_id in task.depends_on:
            if dep_id not in task_ids:
                raise ValidationError(
                    f"Task '{task.id}' depends on non-existent task '{dep_id}'"
                )
    
    # Check for cycles using DFS
    def has_cycle(node: str, visited: Set[str], rec_stack: Set[str]) -> bool:
        visited.add(node)
        rec_stack.add(node)
        
        task = next((t for t in tasks if t.id == node), None)
        if task:
            for dep in task.depends_on:
                if dep not in visited:
                    if has_cycle(dep, visited, rec_stack):
                        return True
                elif dep in rec_stack:
                    return True
        
        rec_stack.remove(node)
        return False
    
    visited: Set[str] = set()
    for task in tasks:
        if task.id not in visited:
            if has_cycle(task.id, visited, set()):
                raise ValidationError(
                    f"Circular dependency detected involving task '{task.id}'"
                )


def validate_timeline(tasks: List[Task]) -> List[Tuple[str, str]]:
    """
    Check for timeline conflicts where dependent tasks start before prerequisites finish.
    
    Returns:
        List of (task_id, conflict_description) tuples for any issues found.
    """
    conflicts = []
    task_map = {task.id: task for task in tasks}
    
    for task in tasks:
        if not task.start_date or not task.due_date:
            continue
            
        # Check each dependency
        for dep_id in task.depends_on:
            dep_task = task_map.get(dep_id)
            if not dep_task or not dep_task.due_date:
                continue
            
            if task.start_date < dep_task.due_date:
                conflicts.append((
                    task.id,
                    f"Task '{task.id}' starts on {task.start_date} but depends on "
                    f"'{dep_id}' which finishes on {dep_task.due_date}"
                ))
    
    return conflicts
