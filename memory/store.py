"""
Memory storage and retrieval
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class MemoryStore:
    """Persistent memory store for ACE."""
    
    def __init__(self, db_path: str = "artifacts/memory/memory.json"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.data = self._load()
    
    def _load(self) -> Dict:
        """Load memory from disk."""
        if self.db_path.exists():
            with open(self.db_path, 'r') as f:
                return json.load(f)
        return {
            "conversations": [],
            "projects": [],
            "code_snippets": [],
            "errors": [],
            "learnings": [],
            "templates": []
        }
    
    def _save(self):
        """Save memory to disk."""
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def store_conversation(self, conversation: Dict) -> bool:
        """Store a conversation."""
        try:
            self.data["conversations"].append({
                **conversation,
                "timestamp": datetime.now().isoformat()
            })
            self._save()
            logger.info(f"Stored conversation")
            return True
        except Exception as e:
            logger.error(f"Error storing conversation: {e}")
            return False
    
    def store_project(self, project: Dict) -> bool:
        """Store project information."""
        try:
            self.data["projects"].append({
                **project,
                "timestamp": datetime.now().isoformat()
            })
            self._save()
            logger.info(f"Stored project: {project.get('name')}")
            return True
        except Exception as e:
            logger.error(f"Error storing project: {e}")
            return False
    
    def store_error(self, error: Dict) -> bool:
        """Store error information."""
        try:
            self.data["errors"].append({
                **error,
                "timestamp": datetime.now().isoformat()
            })
            self._save()
            logger.info(f"Stored error")
            return True
        except Exception as e:
            logger.error(f"Error storing error info: {e}")
            return False
    
    def search(self, query: str, category: str = "conversations") -> List[Dict]:
        """Search memory."""
        if category not in self.data:
            return []
        
        results = []
        for item in self.data.get(category, []):
            if self._matches_query(item, query):
                results.append(item)
        
        return results
    
    def _matches_query(self, item: Dict, query: str) -> bool:
        """Check if item matches query."""
        query_lower = query.lower()
        for value in item.values():
            if isinstance(value, str) and query_lower in value.lower():
                return True
        return False
