"""
Task execution engine
"""

import asyncio
import logging
from typing import Dict, Any, Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class TaskRunner:
    """Executes tasks with error handling and retries."""
    
    def __init__(self):
        self.running_tasks: Dict[str, bool] = {}
        self.task_results: Dict[str, Any] = {}
    
    async def run_task(self, task_id: str, task_func, max_retries: int = 3) -> Dict[str, Any]:
        """Run a task with retry logic."""
        logger.info(f"Starting task execution: {task_id}")
        self.running_tasks[task_id] = True
        
        retries = 0
        while retries < max_retries:
            try:
                result = await task_func()
                self.task_results[task_id] = result
                self.running_tasks[task_id] = False
                logger.info(f"Task completed: {task_id}")
                return {"status": "success", "result": result}
            except Exception as e:
                retries += 1
                logger.error(f"Task {task_id} failed (attempt {retries}): {e}")
                
                if retries < max_retries:
                    await asyncio.sleep(2 ** retries)  # Exponential backoff
                else:
                    self.running_tasks[task_id] = False
                    logger.error(f"Task {task_id} failed after {max_retries} attempts")
                    return {"status": "error", "error": str(e)}
    
    def get_task_status(self, task_id: str) -> str:
        """Get task status."""
        if task_id in self.running_tasks:
            return "running" if self.running_tasks[task_id] else "completed"
        return "not_found"
    
    def get_task_result(self, task_id: str) -> Optional[Any]:
        """Get task result."""
        return self.task_results.get(task_id)
