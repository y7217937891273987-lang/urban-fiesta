#!/usr/bin/env python3
"""
ACE - Autonomous Cognitive Engine
Main entry point for the ACE system
"""

import os
import sys
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(project_root / 'logs' / 'ace.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(project_root / '.env')

# Import core components
from core.orchestrator import Orchestrator
from ui.backend import create_app
from config.settings import Settings


def ensure_directories():
    """Ensure all required directories exist."""
    dirs = [
        'logs',
        'artifacts',
        'artifacts/projects',
        'artifacts/code_snippets',
        'artifacts/memory',
        'artifacts/downloads',
        'config',
        'templates'
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)


def start_backend():
    """Start the Flask backend server."""
    logger.info("Starting ACE backend...")
    app = create_app()
    
    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('BACKEND_PORT', 5000))
    debug = os.getenv('DEBUG', 'false').lower() == 'true'
    
    logger.info(f"Backend running on {host}:{port}")
    app.run(host=host, port=port, debug=debug)


def start_orchestrator():
    """Start the main orchestrator."""
    logger.info("Initializing ACE Orchestrator...")
    orchestrator = Orchestrator()
    return orchestrator


def main():
    """Main entry point."""
    logger.info("="*60)
    logger.info("ACE - Autonomous Cognitive Engine")
    logger.info("="*60)
    
    # Ensure directories
    ensure_directories()
    
    # Load settings
    settings = Settings()
    logger.info(f"Configuration loaded from {settings.config_file}")
    
    # Start backend
    try:
        start_backend()
    except Exception as e:
        logger.error(f"Error starting backend: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
