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

# Ensure logs directory exists
logs_dir = project_root / 'logs'
logs_dir.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(logs_dir / 'ace.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Load environment variables
env_file = project_root / '.env'
if env_file.exists():
    load_dotenv(env_file)
else:
    logger.warning(f".env file not found at {env_file}. Using defaults.")

# Import core components
try:
    from core.orchestrator import Orchestrator
    from ui.backend import create_app
    from config.settings import Settings
except ImportError as e:
    logger.error(f"Failed to import core components: {e}")
    logger.error("Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)


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
    
    logger.info(f"Backend running on http://{host}:{port}")
    logger.info(f"Health check: http://{host}:{port}/health")
    
    try:
        app.run(host=host, port=port, debug=debug, use_reloader=False)
    except OSError as e:
        if "Address already in use" in str(e):
            logger.error(f"ERROR: Port {port} is already in use")
            logger.error("Solution: Edit .env and change BACKEND_PORT to an available port (e.g., 5001)")
        else:
            logger.error(f"ERROR: {e}")
        sys.exit(1)


def main():
    """Main entry point."""
    logger.info("="*60)
    logger.info("ACE - Autonomous Cognitive Engine")
    logger.info("="*60)
    
    # Ensure directories
    ensure_directories()
    
    # Load settings
    try:
        settings = Settings()
        logger.info(f"Configuration loaded")
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        sys.exit(1)
    
    # Start backend
    try:
        start_backend()
    except KeyboardInterrupt:
        logger.info("ACE shutdown requested")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error starting backend: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
