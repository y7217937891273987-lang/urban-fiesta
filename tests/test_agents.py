"""
Tests for agents
"""

import pytest
import asyncio
from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.researcher import ResearcherAgent

@pytest.mark.asyncio
async def test_planner_agent():
    """Test planner agent."""
    agent = PlannerAgent()
    task = {"goal": "Build a web app"}
    result = await agent.execute(task)
    assert result["status"] == "success"
    assert "plan" in result

@pytest.mark.asyncio
async def test_coder_agent():
    """Test coder agent."""
    agent = CoderAgent()
    task = {"goal": "Create a function", "language": "python"}
    result = await agent.execute(task)
    assert result["status"] == "success"
    assert "code" in result
    assert result["language"] == "python"

@pytest.mark.asyncio
async def test_researcher_agent():
    """Test researcher agent."""
    agent = ResearcherAgent()
    task = {"topic": "AI", "depth": "deep"}
    result = await agent.execute(task)
    assert result["status"] == "success"
    assert "findings" in result
