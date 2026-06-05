#!/usr/bin/env python3
"""
ACE - Autonomous Cognitive Engine
Production Backend
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import uuid

# Load environment
load_dotenv()

# Setup logging
Path('logs').mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs/ace.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
CORS(app)

# In-memory task storage
tasks = {}


class Task:
    """Simple task class"""
    def __init__(self, goal, task_type='plan'):
        self.id = str(uuid.uuid4())
        self.goal = goal
        self.task_type = task_type
        self.status = 'pending'
        self.created_at = datetime.now().isoformat()
        self.result = None
    
    def to_dict(self):
        return {
            'id': self.id,
            'goal': self.goal,
            'task_type': self.task_type,
            'status': self.status,
            'created_at': self.created_at,
            'result': self.result
        }


# Routes
@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'healthy', 'service': 'ace'})


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.json or {}
    goal = data.get('goal', 'Unnamed task')
    task_type = data.get('type', 'plan')
    
    task = Task(goal, task_type)
    tasks[task.id] = task
    logger.info(f"Task created: {task.id} - {goal}")
    
    return jsonify(task.to_dict()), 201


@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    """List all tasks"""
    return jsonify([t.to_dict() for t in tasks.values()])


@app.route('/api/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(tasks[task_id].to_dict())


@app.route('/api/tasks/<task_id>/execute', methods=['POST'])
def execute_task(task_id):
    """Execute a task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    task = tasks[task_id]
    task.status = 'running'
    logger.info(f"Executing task: {task_id}")
    
    # Simple execution logic
    if task.task_type == 'plan':
        task.result = {'plan': f'Plan for: {task.goal}', 'steps': ['Step 1', 'Step 2', 'Step 3']}
    elif task.task_type == 'code':
        task.result = {'code': f'# Generated code for {task.goal}\nprint("Hello from ACE")'}
    else:
        task.result = {'output': f'Processed: {task.goal}'}
    
    task.status = 'completed'
    logger.info(f"Task completed: {task_id}")
    
    return jsonify(task.to_dict())


@app.route('/api/info', methods=['GET'])
def info():
    """Get system info"""
    return jsonify({
        'name': 'ACE - Autonomous Cognitive Engine',
        'version': '0.1.0',
        'status': 'running',
        'tasks_total': len(tasks),
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('BACKEND_PORT', 5000))
    
    logger.info(f"\n" + "="*60)
    logger.info("ACE - Autonomous Cognitive Engine")
    logger.info(f"Backend running at http://{host}:{port}")
    logger.info(f"Health check: http://{host}:{port}/health")
    logger.info("="*60 + "\n")
    
    try:
        app.run(host=host, port=port, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        logger.info("ACE shutdown")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
