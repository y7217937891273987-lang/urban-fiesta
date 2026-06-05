# ACE API Reference

## Base URL

```
http://localhost:5000/api
```

## Tasks

### Create Task

**POST** `/tasks`

Create a new task.

Request body:
```json
{
  "goal": "Generate a React dashboard",
  "type": "plan",
  "context": "optional context"
}
```

Response:
```json
{
  "id": "uuid",
  "goal": "Generate a React dashboard",
  "task_type": "plan",
  "status": "pending",
  "created_at": "2024-01-15T10:00:00"
}
```

### Get Task

**GET** `/tasks/{task_id}`

Get task details and status.

Response:
```json
{
  "id": "uuid",
  "goal": "Generate a React dashboard",
  "status": "completed",
  "results": {},
  "error": null
}
```

### List Tasks

**GET** `/tasks`

List all tasks.

Response:
```json
[
  { "id": "uuid1", "goal": "Task 1", "status": "completed" },
  { "id": "uuid2", "goal": "Task 2", "status": "running" }
]
```

### Execute Task

**POST** `/tasks/{task_id}/execute`

Start execution of a task.

Response:
```json
{
  "status": "success",
  "task": { ... }
}
```

## Memory

### Search Memory

**GET** `/memory/search`

Search memory for information.

Query parameters:
- `q`: search query
- `category`: memory category (conversations, projects, code_snippets, errors)

Response:
```json
{
  "results": [...],
  "count": 5
}
```

## Agents

### Get Agent Status

**GET** `/agents/status`

Get status of all agents.

Response:
```json
{
  "agents": [
    { "name": "Planner", "status": "idle", "current_task": null },
    { "name": "Coder", "status": "idle", "current_task": null }
  ]
}
```

## Artifacts

### List Artifacts

**GET** `/artifacts`

List all generated artifacts.

Response:
```json
{
  "artifacts": [
    { "path": "projects/my-app/", "size": 1024 }
  ]
}
```

### Get Artifact

**GET** `/artifacts/{artifact_path}`

Get artifact content.

Response:
```json
{
  "path": "projects/my-app/main.py",
  "content": "..."
}
```

## Health

### Health Check

**GET** `/health`

Check API health.

Response:
```json
{
  "status": "healthy",
  "service": "ace-backend"
}
```
