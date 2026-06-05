"""
Base Agent class
"""

import logging
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Agent(ABC):
    """Base class for all agents."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.status = "idle"
        self.current_task: Optional[str] = None
        logger.info(f"Agent initialized: {name}")
    
    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task. Must be implemented by subclasses."""
        pass
    
    def set_status(self, status: str):
        """Update agent status."""
        self.status = status
        if status != "idle":
            logger.info(f"Agent {self.name} status: {status}")
    
    def get_status(self) -> Dict[str, str]:
        """Get agent status."""
        return {
            "name": self.name,
            "status": self.status,
            "current_task": self.current_task
        }
