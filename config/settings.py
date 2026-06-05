"""
ACE Configuration Settings
"""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""
    
    # Model Configuration
    primary_model: str = "gpt-4"
    secondary_model: str = "gpt-3.5-turbo"
    code_model: str = "gpt-4"
    debug_model: str = "gpt-4"
    fallback_model: str = "gpt-3.5-turbo"
    local_model_enabled: bool = False
    local_model_url: str = "http://localhost:11434"
    
    # API Keys
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    serpapi_api_key: Optional[str] = None
    
    # Server Configuration
    host: str = "localhost"
    backend_port: int = 5000
    frontend_port: int = 3000
    debug: bool = False
    
    # Memory Configuration
    memory_database: str = "sqlite:///memory.db"
    memory_vector_size: int = 1536
    memory_backend: str = "sqlite"
    
    # Execution Configuration
    sandbox_enabled: bool = True
    max_execution_time: int = 300
    max_file_size: int = 10485760  # 10MB
    max_retries: int = 3
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/ace.log"
    
    # Features
    web_search_enabled: bool = True
    code_execution_enabled: bool = True
    file_creation_enabled: bool = True
    git_enabled: bool = True
    
    # Paths
    project_root: Path = Path(__file__).parent.parent
    artifacts_dir: Path = Path("artifacts")
    config_file: Path = Path(".env")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **data):
        super().__init__(**data)
        # Ensure artifact directories exist
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        (self.artifacts_dir / "projects").mkdir(parents=True, exist_ok=True)
        (self.artifacts_dir / "code_snippets").mkdir(parents=True, exist_ok=True)
        (self.artifacts_dir / "memory").mkdir(parents=True, exist_ok=True)
        (self.artifacts_dir / "downloads").mkdir(parents=True, exist_ok=True)
