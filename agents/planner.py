"""
Planner Agent - Converts goals into structured plans
"""

import json
import logging
from typing import Dict, Any, List
from agents.base import Agent

logger = logging.getLogger(__name__)

class PlannerAgent(Agent):
    """Agent that creates project plans from goals."""
    
    def __init__(self):
        super().__init__(
            name="Planner",
            description="Converts natural language goals into structured project plans"
        )
    
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Create a plan from a goal."""
        self.set_status("planning")
        goal = task.get("goal", "")
        
        logger.info(f"Planning task: {goal}")
        
        # Parse goal and create plan structure
        plan = {
            "goal": goal,
            "phases": self._create_phases(goal),
            "milestones": self._create_milestones(goal),
            "estimated_effort": self._estimate_effort(goal),
            "risks": self._identify_risks(goal)
        }
        
        self.set_status("idle")
        return {
            "status": "success",
            "plan": plan
        }
    
    def _create_phases(self, goal: str) -> List[Dict]:
        """Create project phases."""
        return [
            {"id": 1, "name": "Requirements", "description": "Define requirements"},
            {"id": 2, "name": "Design", "description": "Design architecture"},
            {"id": 3, "name": "Implementation", "description": "Write code"},
            {"id": 4, "name": "Testing", "description": "Test and debug"},
            {"id": 5, "name": "Deployment", "description": "Package and deploy"}
        ]
    
    def _create_milestones(self, goal: str) -> List[Dict]:
        """Create milestones."""
        return [
            {"name": "Requirements Complete", "phase": 1},
            {"name": "Design Approved", "phase": 2},
            {"name": "MVP Ready", "phase": 3},
            {"name": "Tests Passing", "phase": 4},
            {"name": "Released", "phase": 5}
        ]
    
    def _estimate_effort(self, goal: str) -> Dict:
        """Estimate project effort."""
        return {
            "hours": 40,
            "days": 5,
            "confidence": "medium"
        }
    
    def _identify_risks(self, goal: str) -> List[str]:
        """Identify project risks."""
        return [
            "Unclear requirements",
            "Scope creep",
            "Technical complexity"
        ]
