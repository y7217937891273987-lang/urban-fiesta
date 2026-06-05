"""
Tests for orchestrator
"""

import pytest
import asyncio
from core.orchestrator import Orchestrator, TaskStatus

def test_create_task():
    """Test task creation."""
    orchestrator = Orchestrator()
    task = orchestrator.create_task(goal="Test task")
    assert task.goal == "Test task"
    assert task.status == TaskStatus.PENDING

def test_add_subtask():
    """Test adding subtasks."""
    orchestrator = Orchestrator()
    parent = orchestrator.create_task(goal="Parent task")
    subtask = orchestrator.add_subtask(parent.id, goal="Subtask")
    assert subtask is not None
    assert subtask.parent_id == parent.id
    assert len(parent.subtasks) == 1

def test_update_task_status():
    """Test updating task status."""
    orchestrator = Orchestrator()
    task = orchestrator.create_task(goal="Test task")
    
    orchestrator.update_task_status(task.id, TaskStatus.RUNNING)
    assert orchestrator.get_task(task.id).status == TaskStatus.RUNNING
    
    orchestrator.update_task_status(task.id, TaskStatus.COMPLETED)
    assert orchestrator.get_task(task.id).status == TaskStatus.COMPLETED

@pytest.mark.asyncio
async def test_execute_task():
    """Test task execution."""
    orchestrator = Orchestrator()
    task = orchestrator.create_task(goal="Test task")
    result = await orchestrator.execute_task(task.id)
    assert result is True
    assert orchestrator.get_task(task.id).status == TaskStatus.COMPLETED
