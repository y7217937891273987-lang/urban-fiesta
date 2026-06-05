"""
ACE Web Backend - Flask API
"""

import os
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
from core.orchestrator import Orchestrator, TaskStatus
from memory.store import MemoryStore
from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.researcher import ResearcherAgent

logger = logging.getLogger(__name__)

def create_app():
    """Create and configure Flask app."""
    app = Flask(__name__)
    CORS(app)
    
    # Initialize core components
    orchestrator = Orchestrator()
    memory_store = MemoryStore()
    
    # Initialize agents
    planner_agent = PlannerAgent()
    coder_agent = CoderAgent()
    researcher_agent = ResearcherAgent()
    
    # Health check
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({"status": "healthy", "service": "ace-backend"})
    
    # Create task
    @app.route('/api/tasks', methods=['POST'])
    def create_task():
        data = request.json
        goal = data.get('goal')
        task_type = data.get('type', 'plan')
        
        task = orchestrator.create_task(goal=goal, task_type=task_type)
        return jsonify(task.to_dict()), 201
    
    # Get task
    @app.route('/api/tasks/<task_id>', methods=['GET'])
    def get_task(task_id):
        task = orchestrator.get_task(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(task.to_dict())
    
    # Get all tasks
    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        return jsonify(orchestrator.get_all_tasks())
    
    # Execute task
    @app.route('/api/tasks/<task_id>/execute', methods=['POST'])
    def execute_task(task_id):
        task = orchestrator.get_task(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        
        import asyncio
        success = asyncio.run(orchestrator.execute_task(task_id))
        
        return jsonify({
            "status": "success" if success else "failed",
            "task": task.to_dict()
        })
    
    # Search memory
    @app.route('/api/memory/search', methods=['GET'])
    def search_memory():
        query = request.args.get('q', '')
        category = request.args.get('category', 'conversations')
        results = memory_store.search(query, category)
        return jsonify({"results": results, "count": len(results)})
    
    # Get agent status
    @app.route('/api/agents/status', methods=['GET'])
    def get_agents_status():
        return jsonify({
            "agents": [
                planner_agent.get_status(),
                coder_agent.get_status(),
                researcher_agent.get_status()
            ]
        })
    
    # List artifacts
    @app.route('/api/artifacts', methods=['GET'])
    def list_artifacts():
        artifacts_dir = Path('artifacts')
        artifacts = []
        for item in artifacts_dir.rglob('*'):
            if item.is_file():
                artifacts.append({
                    "path": str(item.relative_to(artifacts_dir)),
                    "size": item.stat().st_size
                })
        return jsonify({"artifacts": artifacts})
    
    # Get artifact
    @app.route('/api/artifacts/<path:artifact_path>', methods=['GET'])
    def get_artifact(artifact_path):
        file_path = Path('artifacts') / artifact_path
        if not file_path.exists():
            return jsonify({"error": "Artifact not found"}), 404
        
        return jsonify({
            "path": artifact_path,
            "content": file_path.read_text() if file_path.suffix in ['.txt', '.py', '.js', '.json', '.md'] else None
        })
    
    return app
