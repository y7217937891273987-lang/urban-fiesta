# ACE Quick Start Guide

## For Windows Users - Fastest Way

### Just Double-Click One File

```
run-ace.bat
```

**That's it!** The script will:
- ✅ Check Python
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Set up configuration
- ✅ Create folders
- ✅ Start ACE automatically

**No other steps. No terminal commands. Just double-click and go.**

---

## For Mac/Linux Users - Fastest Way

### Run One Command in Terminal

```bash
bash run-ace.sh
```

**That's it!** Same process as Windows.

---

## When ACE Starts

You'll see:

```
=====================================================
 ACE - Autonomous Cognitive Engine
 Automated Setup & Launch
=====================================================

[STEP 1/6] Checking Python installation...
[DONE] Python found: Python 3.11.0

[STEP 2/6] Setting up Python environment...
[DONE] Virtual environment already exists

[STEP 3/6] Activating virtual environment...
[DONE] Environment activated

[STEP 4/6] Installing dependencies...
[DONE] All dependencies installed

[STEP 5/6] Setting up configuration...
[DONE] Configuration created

[STEP 6/6] Preparing workspace...
[DONE] Workspace ready

=====================================================
 LAUNCHING ACE BACKEND
=====================================================

 Backend: http://localhost:5000
 Health:  http://localhost:5000/health

 Press Ctrl+C to stop
```

---

## Your ACE is Now Running

### Test It

Open a new terminal/command prompt and run:

```bash
curl http://localhost:5000/health
```

You should see:

```json
{"status": "healthy", "service": "ace-backend"}
```

---

## Create Your First Task

```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"goal": "Generate a Python function", "type": "code"}'
```

Response:

```json
{
  "id": "abc-123-def",
  "goal": "Generate a Python function",
  "task_type": "code",
  "status": "pending",
  "created_at": "2024-01-15T10:00:00"
}
```

---

## View Task Status

```bash
curl http://localhost:5000/api/tasks
```

---

## Stop ACE

Press **Ctrl+C** in the terminal where ACE is running.

---

## Next Time

Just run the same command again:

**Windows:** Double-click `run-ace.bat`

**Mac/Linux:** `bash run-ace.sh`

Everything else happens automatically.

---

## Troubleshooting

### "Python is not installed"

**Windows:**
1. Download from https://www.python.org
2. Install with "Add Python to PATH" checked
3. Run the script again

**Mac:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3 python3-pip python3-venv
```

### "Port 5000 is already in use"

Edit `.env` and change:
```
BACKEND_PORT=5001
```

### "Dependencies failed to install"

Try running manually:
```bash
pip install -r requirements.txt
```

---

## Full Documentation

- **Architecture:** See `docs/ARCHITECTURE.md`
- **API Reference:** See `docs/API.md`
- **Contributing:** See `CONTRIBUTING.md`

---

**You're all set! ACE is ready to go.** 🚀
