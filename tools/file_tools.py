"""
File manipulation tools
"""

import os
import logging
from pathlib import Path
from typing import Dict, Any
from tools.base import Tool

logger = logging.getLogger(__name__)

class CreateFileTool(Tool):
    """Create a file."""
    
    def __init__(self):
        super().__init__(
            name="create_file",
            description="Create a new file with content"
        )
    
    def execute(self, path: str, content: str, **params) -> Dict[str, Any]:
        """Create a file."""
        if not self.validate_params(["path", "content"], path=path, content=content):
            return {"status": "error", "message": "Missing parameters"}
        
        try:
            file_path = Path(path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            logger.info(f"Created file: {path}")
            return {"status": "success", "path": str(file_path)}
        except Exception as e:
            logger.error(f"Error creating file: {e}")
            return {"status": "error", "message": str(e)}

class ReadFileTool(Tool):
    """Read a file."""
    
    def __init__(self):
        super().__init__(
            name="read_file",
            description="Read content from a file"
        )
    
    def execute(self, path: str, **params) -> Dict[str, Any]:
        """Read a file."""
        if not self.validate_params(["path"], path=path):
            return {"status": "error", "message": "Missing path"}
        
        try:
            content = Path(path).read_text()
            logger.info(f"Read file: {path}")
            return {"status": "success", "content": content}
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            return {"status": "error", "message": str(e)}
