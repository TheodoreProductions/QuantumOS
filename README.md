# QuantumOS

A TheodoreProductions™ quantum operating system with pygame-based sandbox escape game.

## Dependencies

This project uses [uv](https://docs.astral.sh/uv/) for Python package management.

### Required Dependencies
- `pygame>=2.6.1` - For graphics and game functionality

## Installation

1. Make sure you have [uv](https://docs.astral.sh/uv/) installed
2. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Applications

### Sandbox Escape Game
```bash
uv run python sandboxescape.py
```

### 3D Test Renderer
```bash
uv run python testCode.py
```

## Development

All dependencies are managed through `pyproject.toml` and locked in `uv.lock`. 

To add new dependencies:
```bash
uv add <package-name>
```

To run commands in the virtual environment:
```bash
uv run <command>
```

To activate the virtual environment:
```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```