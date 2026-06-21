# Project Context

<PROJECT_NAME> is a research codebase. Describe the scientific goal here in
one or two sentences so an agent (or new collaborator) has the framing.

## Key Principles to follow

When working with this codebase, prioritize code readability and consistency,
and best engineering practices. Ask clarifying questions before making
architectural changes.

**Discussion/approval before code implementation:**
Always discuss proposed changes before implementing them.

**Code Quality:**
Resolve all Ruff linting and Pyright type checking issues during
implementation. Do not leave linting errors for later.

**Code based on up-to-date documentation:**
Always use the Context7 MCP to fetch up-to-date library docs when generating
code (e.g., PyTorch).

## Architecture

The codebase follows a **vertical-slice architecture**: each model /
experiment lives in its own slice under `src/<slice_name>/`, owning its
entrypoint, config, data handling, and exploration scripts. Cross-slice
reusable code lives in `src/shared/`. Slices should depend on `shared/`, not
on each other.

A slice typically contains:

- `main.py`         — CLI entrypoint (argparse), wires shared components.
- `config.yaml`     — declarative config for the run; comment every key.
- `build_metadata.py` — builds the slice's metadata table from raw data.
- `scripts/data.py` — dataset / dataloader for the slice.
- `explore/`        — throwaway exploration scripts + their report outputs.

Tests mirror the source tree: `tests/<slice_name>/` for each slice.

## Coding Conventions

**Line Length:**
- Maximum 88 characters per line.

**Path Handling:**
- Always use `pathlib.Path` for file paths.
- Prefer constructor style: `Path("/", "mnt", "data")` instead of
  `Path("/mnt/data")`.

**Type Annotations (Pyright-enforced):**
- Required on all functions and classes.
- Use Python 3.10+ union syntax: `str | None` instead of `Optional[str]`.
- Use built-in generics: `list[str]`, `dict[str, int]`.

**Docstrings (Ruff-enforced):**
- Google-style docstrings required on all public functions and classes.
- Include Args, Returns, Raises sections where applicable.

### Code Quality Auto-Checks
```bash
# Lint code
ruff check src/ tests/

# Format code
ruff format src/ tests/

# Type checking
pyright src/ tests/

# Run all pre-commit hooks
pre-commit run --all-files
```

## Adding a new slice

1. `cp -r src/example_slice src/<new_slice>` and rename internals.
2. Add the package to `packages` in `[tool.hatch.build.targets.wheel]`.
3. Add the name to `known-first-party` under `[tool.ruff.lint.isort]`.
4. Mirror the test directory: `cp -r tests/example_slice tests/<new_slice>`.

## Technology Stack

TBC — record the chosen libraries per slice here as the project grows.
