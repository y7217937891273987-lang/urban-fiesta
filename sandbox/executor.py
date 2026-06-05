"""
Sandboxed code execution
"""

import subprocess
import logging
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional
import os

logger = logging.getLogger(__name__)

class SandboxExecutor:
    """Safely execute code in isolation."""
    
    def __init__(self, timeout: int = 30, max_output: int = 1024*1024):
        self.timeout = timeout
        self.max_output = max_output
    
    def execute_python(self, code: str) -> Dict[str, Any]:
        """Execute Python code safely."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                f.flush()
                temp_file = f.name
            
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            output = result.stdout[:self.max_output]
            error = result.stderr[:self.max_output]
            
            logger.info(f"Python execution completed with return code {result.returncode}")
            
            return {
                "status": "success" if result.returncode == 0 else "error",
                "output": output,
                "error": error,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            logger.error(f"Python execution timed out after {self.timeout}s")
            return {
                "status": "timeout",
                "error": f"Execution timed out after {self.timeout} seconds"
            }
        except Exception as e:
            logger.error(f"Error executing Python: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
        finally:
            if 'temp_file' in locals():
                Path(temp_file).unlink(missing_ok=True)
    
    def execute_javascript(self, code: str) -> Dict[str, Any]:
        """Execute JavaScript code safely."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                f.write(code)
                f.flush()
                temp_file = f.name
            
            result = subprocess.run(
                ['node', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            output = result.stdout[:self.max_output]
            error = result.stderr[:self.max_output]
            
            return {
                "status": "success" if result.returncode == 0 else "error",
                "output": output,
                "error": error,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "error": f"Execution timed out after {self.timeout} seconds"
            }
        except Exception as e:
            logger.error(f"Error executing JavaScript: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
        finally:
            if 'temp_file' in locals():
                Path(temp_file).unlink(missing_ok=True)
