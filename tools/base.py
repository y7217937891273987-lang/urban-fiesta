"""
Base Tool class
"""

import logging
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Tool(ABC):
    """Base class for all tools."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        logger.info(f"Tool registered: {name}")
    
    @abstractmethod
    def execute(self, **params) -> Dict[str, Any]:
        """Execute the tool. Must be implemented by subclasses."""
        pass
    
    def validate_params(self, required: list, **params) -> bool:
        """Validate required parameters."""
        for param in required:
            if param not in params:
                logger.error(f"Missing required parameter: {param}")
                return False
        return True
