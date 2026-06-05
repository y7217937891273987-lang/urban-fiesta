"""
ACE Orchestrator - Main coordination engine
"""

import asyncio
import uuid
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum
import json

logger = logging.getLogger(__name__)

class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"

class Task:
    """Represents a single unit of work."""
    
    def __init__(self, goal: str, task_type: str = "plan", parent_id: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.goal = goal
        self.task_type = task_type
        self.parent_id = parent_id
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.subtasks: List[Task] = []
        self.dependencies: List[str] = []
        self.results: Dict[str, Any] = {}
        self.error: Optional[str] = None
        self.retry_count = 0
        self.max_retries = 3
        self.assigned_agent: Optional[str] = None
        self.assigned_tools: List[str] = []
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary."""
        return {
            "id": self.id,
            "goal": self.goal,
            "task_type": self.task_type,
            "parent_id": self.parent_id,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "subtasks": len(self.subtasks),
            "error": self.error,
            "assigned_agent": self.assigned_agent,
        }

class Orchestrator:
    """Main orchestration engine for ACE."""
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.agents: Dict[str, Any] = {}
        self.tools: Dict[str, Any] = {}
        self.memory = {}
        logger.info("Orchestrator initialized")
    
    def create_task(self, goal: str, task_type: str = "plan") -> Task:
        """Create a new task."""
        task = Task(goal=goal, task_type=task_type)
        self.tasks[task.id] = task
        logger.info(f"Created task {task.id}: {goal}")
        return task
    
    def add_subtask(self, parent_id: str, goal: str, task_type: str = "code") -> Optional[Task]:
        """Add a subtask to an existing task."""
        if parent_id not in self.tasks:
            logger.error(f"Parent task {parent_id} not found")
            return None
        
        parent = self.tasks[parent_id]
        subtask = Task(goal=goal, task_type=task_type, parent_id=parent_id)
        parent.subtasks.append(subtask)
        self.tasks[subtask.id] = subtask
        logger.info(f"Added subtask {subtask.id} to {parent_id}")
        return subtask
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by ID."""
        return self.tasks.get(task_id)
    
    def update_task_status(self, task_id: str, status: TaskStatus) -> bool:
        """Update task status."""
        if task_id not in self.tasks:
            return False
        
        task = self.tasks[task_id]
        old_status = task.status
        task.status = status
        
        if status == TaskStatus.RUNNING:
            task.started_at = datetime.now()
        elif status == TaskStatus.COMPLETED:
            task.completed_at = datetime.now()
        elif status == TaskStatus.FAILED:
            task.completed_at = datetime.now()
        
        logger.info(f"Task {task_id} status changed: {old_status.value} -> {status.value}")
        return True
    
    async def execute_task(self, task_id: str) -> bool:
        """Execute a task."""
        task = self.get_task(task_id)
        if not task:
            logger.error(f"Task {task_id} not found")
            return False
        
        logger.info(f"Executing task {task_id}: {task.goal}")
        self.update_task_status(task_id, TaskStatus.RUNNING)
        
        try:
            # Simple execution logic - can be extended
            task.results["output"] = f"Task executed: {task.goal}"
            self.update_task_status(task_id, TaskStatus.COMPLETED)
            logger.info(f"Task {task_id} completed")
            return True
        except Exception as e:
            logger.error(f"Task {task_id} failed: {e}")
            task.error = str(e)
            task.retry_count += 1
            
            if task.retry_count < task.max_retries:
                logger.info(f"Retrying task {task_id} (attempt {task.retry_count})")
                await asyncio.sleep(2 ** task.retry_count)  # Exponential backoff
                return await self.execute_task(task_id)
            else:
                self.update_task_status(task_id, TaskStatus.FAILED)
                return False
    
    def get_all_tasks(self) -> List[Dict]:
        """Get all tasks."""
        return [task.to_dict() for task in self.tasks.values()]
    
    def get_task_tree(self, task_id: str) -> Dict:
        """Get task with all subtasks in tree format."""
        task = self.get_task(task_id)
        if not task:
            return {}
        
        return {
            **task.to_dict(),
            "subtasks": [self.get_task_tree(st.id) for st in task.subtasks]
        }
