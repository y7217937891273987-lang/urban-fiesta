# ACE Architecture

## Overview

ACE is built as a layered system with clear separation of concerns:

```
┌─────────────────────────────────────┐
│     Web UI / Chat Interface         │
├─────────────────────────────────────┤
│     REST API / Flask Backend        │
├─────────────────────────────────────┤
│      Orchestrator / Task Engine     │
├─────────────────────────────────────┤
│   Agents  │  Tools  │  Memory       │
├─────────────────────────────────────┤
│    Sandbox Executor / Safety Layer  │
└─────────────────────────────────────┘
```

## Components

### Interface Layer
- Web UI built with React/Vue
- Chat interface for natural language input
- Real-time task monitoring
- Artifact viewing and download

### Orchestration Layer
- Task creation and management
- Dependency resolution
- Parallel execution
- State management
- Error handling and retries

### Agent Layer
- Planner: Converts goals to plans
- Coder: Generates code
- Researcher: Gathers information
- Debug: Analyzes and fixes errors
- Business: Validates ideas
- Product: Builds complete products

### Tool Layer
- File operations
- Code execution
- Web scraping
- API calls
- Git operations
- Terminal commands

### Memory Layer
- Semantic search
- Conversation history
- Project memory
- Error patterns
- Learning and templates

### Execution Layer
- Task runner with retries
- Timeout management
- Resource limits
- Error recovery

### Sandbox Layer
- Isolated code execution
- Resource limits
- Permission restrictions
- Audit logging

## Data Flow

1. User enters goal in UI
2. UI sends to backend API
3. Orchestrator creates task
4. Planner agent analyzes goal
5. Plan is broken into subtasks
6. Appropriate agents assigned
7. Tools execute actions
8. Results stored in memory
9. UI updates with progress
10. Final artifact generated

## Configuration

All configuration through environment variables in `.env`:

- Model selection and API keys
- Server ports and debug mode
- Memory backend and vector size
- Execution limits and timeouts
- Feature flags

## Extensibility

ACE is designed to be extended:

- Add new agents by subclassing `Agent`
- Add new tools by subclassing `Tool`
- Add new memory types
- Add new model integrations
- Add new UI components

## Security

- Sandbox execution for code
- API key management via environment
- Input validation
- Output sanitization
- Audit logging
- Resource limits
