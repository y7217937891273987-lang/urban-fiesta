# ACE - Autonomous Cognitive Engine

**ACE** is a complete, production-grade autonomous AI platform designed to plan, code, research, build products, and execute complex tasks end-to-end.

## What is ACE?

ACE is an intelligent orchestration system that combines:
- **God-Mode Autonomy**: Deep reasoning, multi-step execution, project creation, self-directed task completion
- **Multi-Model Swarm Intelligence**: Coordinate work across multiple AI models with intelligent routing and fallback logic
- **Docker-Ready Production Deployment**: Complete containerization, reproducible startup, persistent storage
- **Persistent Memory**: Semantic search, long-term learning, reusable templates
- **Secure Sandbox Execution**: Isolated code execution, restricted file access, audit logging

## Core Capabilities

ACE can:
- Accept natural language goals and break them into structured tasks
- Plan projects end-to-end with dependency management
- Generate complete, production-ready code (Python, JavaScript, TypeScript, React, APIs, CLI tools)
- Research the web and APIs, compare options, extract facts
- Debug code iteratively, inspect logs, propose fixes
- Build business ideas, landing pages, dashboards, full-stack products
- Maintain memory across sessions and learn from past work
- Execute in a controlled sandbox with audit trails
- Package outputs as working deliverables with documentation

## Architecture

```
ACE/
├── core/                 # Orchestration engine, task graph, state management
├── agents/               # Planner, Architect, Researcher, Coder, Debug, Business, Product, Memory, Compliance
├── tools/                # File creation, code execution, web fetch, API calls, Git, terminal
├── memory/               # Semantic search, conversation memory, project memory, learning
├── executor/             # Task execution, dependency resolution, parallel execution
├── sandbox/              # Sandboxed code execution, isolation, resource limits
├── ui/                   # Web-based UI (Flask backend, React/Vue frontend)
├── config/               # Configuration management, environment variables, model routing
├── templates/            # Code templates, project templates, business templates
├── tests/                # Unit tests, integration tests
├── docker/               # Docker configuration, compose files
├── scripts/              # Setup scripts, startup scripts, utilities
├── docs/                 # Architecture, API docs, user guides
└── main.py              # Application entry point
```

## Quick Start

### Option 1: One-Click Startup (Recommended)

**Windows:**
```batch
run-ace.bat
```

**Mac/Linux:**
```bash
bash run-ace.sh
```

This will:
1. Check Python installation
2. Create virtual environment
3. Install dependencies
4. Start ACE backend on localhost:5000
5. Start ACE UI on localhost:3000
6. Open browser automatically

### Option 2: Manual Setup

```bash
# Clone repository
git clone https://github.com/y7217937891273987-lang/urban-fiesta.git
cd urban-fiesta

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys if desired

# Run ACE
python main.py

# UI automatically opens on localhost:3000
```

### Option 3: Docker (Production)

```bash
docker-compose up --build
```

UI will be available at `localhost:3000`.

## Usage

### Web Interface
1. Open browser to `http://localhost:3000`
2. Enter your goal in natural language
3. Click "Create Task" or "Start Project"
4. Monitor execution in real-time
5. View generated code, artifacts, and logs
6. Refine and iterate

### Example Tasks

**Generate a Product:**
```
Create a full-stack SaaS dashboard for tracking team productivity with login, charts, and export features
```

**Build a Website:**
```
Generate a landing page for an AI writing assistant with pricing, testimonials, and email capture form
```

**Write Code:**
```
Write a Python CLI tool that fetches GitHub repository stats and generates a markdown report
```

**Debug and Fix:**
```
Here's my Python code [paste]. It's throwing KeyError on line 42. Debug and fix it.
```

**Research:**
```
Research and compare the top 5 React UI component libraries. Create a comparison matrix.
```

## Configuration

Edit `.env` to configure:

```bash
# Model Configuration
PRIMARY_MODEL=gpt-4                # OpenAI GPT-4 (default)
SECONDARY_MODEL=gpt-3.5-turbo
CODE_MODEL=claude-3-opus           # Anthropic Claude
DEBUG_MODEL=gpt-4
FALLBACK_MODEL=gpt-3.5-turbo
LOCAL_MODEL_ENABLED=false          # Set to true for local Ollama/LM Studio

# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...

# Server
HOST=localhost
BACKEND_PORT=5000
FRONTEND_PORT=3000

# Memory
MEMORY_DATABASE=sqlite:///memory.db
MEMORY_VECTOR_SIZE=1536

# Execution
SANDBOX_ENABLED=true
MAX_EXECUTION_TIME=300
MAX_FILE_SIZE=10485760              # 10MB
```

## Integration with Odysseus

ACE is designed to complement and extend Odysseus:

- **Odysseus** provides the chat and UI layer
- **ACE** provides the autonomous planning, code generation, and multi-agent orchestration
- Both can run on localhost with persistent memory
- ACE agents can be invoked from Odysseus workflows
- Shared memory and artifact storage

## File Organization

### Generating in Your Workflow

All generated code, artifacts, and projects are stored in `artifacts/`:

```
artifacts/
├── projects/              # Generated project folders
│   ├── my-app-2024-01-15/
│   │   ├── src/
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   └── ...
├��─ code_snippets/         # Reusable code templates
├── memory/                # Persistent memory and embeddings
├── logs/                  # Execution logs
└── downloads/             # Generated downloadable files
```

## Features

### Planning & Orchestration
- [ ] Task graph creation and DAG resolution
- [ ] Dependency detection and parallel execution
- [ ] Subtask management and milestone tracking
- [ ] Retry logic with exponential backoff
- [ ] Multi-step workflow execution

### Code Generation
- [ ] Python, JavaScript, TypeScript, React, Vue
- [ ] Full-stack applications
- [ ] REST APIs and GraphQL
- [ ] CLI tools and automation scripts
- [ ] Landing pages and dashboards
- [ ] Database-backed systems
- [ ] Docker configuration

### Intelligence
- [ ] Multi-model routing (GPT-4, Claude, Llama, local models)
- [ ] Semantic code search
- [ ] Intelligent fallback when models fail
- [ ] Context-aware model selection
- [ ] Token cost optimization

### Memory & Learning
- [ ] Semantic search over past projects
- [ ] Error pattern detection
- [ ] Success replication
- [ ] Code snippet retrieval
- [ ] Project template library
- [ ] Performance learning

### Debugging & Testing
- [ ] Automatic error detection
- [ ] Stack trace analysis
- [ ] Fix proposal and application
- [ ] Unit test generation
- [ ] Integration test generation
- [ ] Log inspection and filtering

### Business Building
- [ ] Idea validation and niche analysis
- [ ] Competitor comparison
- [ ] Feature selection
- [ ] Landing page generation
- [ ] Pricing strategy
- [ ] Launch checklist generation

### Security & Compliance
- [ ] Sandbox execution with resource limits
- [ ] API key management via environment variables
- [ ] Audit logging of all actions
- [ ] Compliance checking for regulated industries
- [ ] Safe defaults and approval gates

## API Reference

### REST Endpoints

```bash
# Create a new task
POST /api/tasks
{
  "goal": "Generate a React dashboard",
  "context": "...",
  "options": {...}
}

# Get task status
GET /api/tasks/{task_id}

# Get task logs
GET /api/tasks/{task_id}/logs

# Get generated artifacts
GET /api/tasks/{task_id}/artifacts

# Search memory
GET /api/memory/search?q=authentication

# Get agent status
GET /api/agents/status

# Execute a tool
POST /api/tools/execute
{
  "tool": "code_executor",
  "params": {...}
}
```

## Extending ACE

### Adding a New Agent

```python
from agents.base import Agent

class MyAgent(Agent):
    def __init__(self):
        super().__init__(name="MyAgent")
    
    async def execute(self, task):
        # Implement agent logic
        return result
```

### Adding a New Tool

```python
from tools.base import Tool

class MyTool(Tool):
    def __init__(self):
        super().__init__(name="my_tool")
    
    def execute(self, **params):
        # Implement tool logic
        return result
```

### Adding Memory Types

Extend the memory layer by adding new memory schemas and retrieval methods.

## Testing

```bash
# Run all tests
pytest

# Run specific test suite
pytest tests/test_agents.py

# Run with coverage
pytest --cov=core --cov=agents
```

## Troubleshooting

### Port Already in Use
```bash
# On Windows
netstat -ano | findstr :5000
taskkill /PID {PID} /F

# On Mac/Linux
lsof -i :5000
kill -9 {PID}
```

### Out of Memory
Reduce `MAX_EXECUTION_TIME` or `MAX_FILE_SIZE` in `.env`.

### Model API Errors
Verify API keys in `.env` and check model availability.

### Sandbox Issues
Ensure Docker is running if using sandboxed execution.

## License

MIT License - See LICENSE file

## Contributing

See CONTRIBUTING.md for development guidelines.

## Support

For issues, feature requests, or questions:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include logs from `logs/` directory

## Roadmap

- [ ] Real-time collaboration
- [ ] Vision/image generation
- [ ] Audio processing
- [ ] Advanced RAG with vector databases
- [ ] Self-hosted model support
- [ ] Mobile app
- [ ] Browser extension
- [ ] Enterprise features (audit, compliance, SSO)

## Acknowledgments

Built to integrate with and extend the Odysseus framework.
