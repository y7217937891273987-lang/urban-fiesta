# Contributing to ACE

We welcome contributions to ACE! Please follow these guidelines.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Submit a pull request

## Development Setup

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
pip install pytest pytest-asyncio pytest-cov
```

## Running Tests

```bash
pytest
pytest --cov=core --cov=agents  # with coverage
```

## Code Style

- Use Python 3.8+
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions small and focused

## Adding a New Agent

1. Create a new file in `agents/`
2. Inherit from `Agent` base class
3. Implement the `execute` method
4. Add tests in `tests/`
5. Update README with agent description

## Adding a New Tool

1. Create a new file in `tools/`
2. Inherit from `Tool` base class
3. Implement the `execute` method
4. Add parameter validation
5. Add tests

## Submitting PRs

- Write clear commit messages
- Add tests for new functionality
- Update documentation
- Ensure all tests pass
- Keep PRs focused and reasonably sized
