"""
Coder Agent - Generates code
"""

import logging
from typing import Dict, Any
from agents.base import Agent

logger = logging.getLogger(__name__)

class CoderAgent(Agent):
    """Agent that generates code."""
    
    def __init__(self):
        super().__init__(
            name="Coder",
            description="Generates production-ready code"
        )
    
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Generate code."""
        self.set_status("coding")
        goal = task.get("goal", "")
        language = task.get("language", "python")
        
        logger.info(f"Generating {language} code for: {goal}")
        
        # Generate code template
        code = self._generate_code(goal, language)
        
        self.set_status("idle")
        return {
            "status": "success",
            "code": code,
            "language": language,
            "filename": f"generated.{self._get_extension(language)}"
        }
    
    def _generate_code(self, goal: str, language: str) -> str:
        """Generate code based on goal."""
        if language == "python":
            return '''#!/usr/bin/env python3
"""Generated module."""

import logging

logger = logging.getLogger(__name__)

class GeneratedClass:
    """Generated class."""
    
    def __init__(self):
        self.name = "GeneratedClass"
    
    def run(self):
        """Run the generated code."""
        logger.info(f"Running {self.name}")
        return "Success"

if __name__ == "__main__":
    obj = GeneratedClass()
    print(obj.run())
'''
        elif language == "javascript":
            return '''// Generated module

class GeneratedClass {
  constructor() {
    this.name = "GeneratedClass";
  }
  
  run() {
    console.log(`Running ${this.name}`);
    return "Success";
  }
}

module.exports = GeneratedClass;
'''
        else:
            return "// Generated code\n"
    
    def _get_extension(self, language: str) -> str:
        """Get file extension for language."""
        extensions = {
            "python": "py",
            "javascript": "js",
            "typescript": "ts",
            "java": "java",
            "csharp": "cs",
        }
        return extensions.get(language, "txt")
