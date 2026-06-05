# ACE Installation Guide

## One-Command Installation & Setup

Choose your operating system:

### Windows

**Method 1: Double-Click (Easiest)**
1. Navigate to the ACE folder
2. Double-click `run-ace.bat`
3. Wait for setup to complete
4. ACE launches automatically

**Method 2: Command Line**
```batch
run-ace.bat
```

### macOS / Linux

**Method 1: Single Command**
```bash
bash run-ace.sh
```

**Method 2: Using bash shorthand**
```bash
./run-ace.sh
```
(Make sure it's executable: `chmod +x run-ace.sh`)

---

## What Happens Automatically

The startup script does everything for you:

```
┌─────────────────────────────────────┐
│ 1. Check Python Installation        │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│ 2. Create Virtual Environment       │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│ 3. Install All Dependencies         │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│ 4. Set Up Configuration (.env)      │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│ 5. Create Workspace Folders         │
└────────────┬────────────────────────┘
             ↓
┌─────────────────────────────────────┐
│ 6. Launch ACE Backend               │
└─────────────────────────────────────┘
```

**Total time:** 2-3 minutes on first run, 30 seconds on subsequent runs.

---

## Requirements

- **Python 3.8 or higher**
- **Git** (for cloning the repository)
- **Port 5000** available (configurable in `.env`)
- **2GB+ free disk space**

---

## Verified Working On

- ✅ Windows 10 / 11
- ✅ macOS 12+ (Intel and Apple Silicon)
- ✅ Ubuntu 20.04+
- ✅ Debian 11+
- ✅ CentOS 8+

---

## Next Steps After Installation

1. **Verify Installation**
   ```bash
   curl http://localhost:5000/health
   ```

2. **Read Quick Start**
   - See `QUICKSTART.md` for first task examples

3. **Configure API Keys (Optional)**
   - Edit `.env` file
   - Add OpenAI, Anthropic, or other API keys

4. **Read Full Docs**
   - Architecture: `docs/ARCHITECTURE.md`
   - API Reference: `docs/API.md`
   - Contributing: `CONTRIBUTING.md`

---

## Getting Help

If something goes wrong:

1. **Check logs:**
   ```bash
   cat logs/ace.log
   ```

2. **Verify Python:**
   ```bash
   python --version  # Windows
   python3 --version # Mac/Linux
   ```

3. **Check ports:**
   ```bash
   # Windows
   netstat -ano | findstr :5000
   
   # Mac/Linux
   lsof -i :5000
   ```

4. **Reinstall dependencies:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

5. **Check the docs:**
   - See `docs/ARCHITECTURE.md` for system design
   - See `docs/API.md` for API endpoints

---

## Docker Installation (Alternative)

If you prefer Docker:

```bash
docker-compose up --build
```

Then access:
- Backend: http://localhost:5000
- Health: http://localhost:5000/health

---

**Installation complete! ACE is ready to use.** 🚀
