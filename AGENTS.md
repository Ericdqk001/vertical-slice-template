<!-- Mirror of CLAUDE.md for Codex and other agents; keep both in sync. -->

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

## Design Philosophy

Follow John Ousterhout, *A Philosophy of Software Design* (2nd ed., 2021).
The goal is to minimise complexity: anything that makes code hard to
understand or change.

**Avoid unnecessary complexity:**
- Watch for its three symptoms: change amplification (one change touches many
  places), cognitive load (too much to know to make a change), and unknown
  unknowns (unclear what must change).
- Its two causes are dependencies and obscurity; keep both to a minimum.
- Think strategically, not tactically: spend a little extra effort on clean
  design now instead of piling up quick hacks.
- Don't add abstractions, layers, options or config keys before they are
  needed. Pass-through methods and shallow wrappers add complexity.

**Deep modules:**
- Prefer modules (functions, classes, files) with a simple interface that
  hides a lot of functionality. Interface cost should be small relative to the
  benefit.
- Hide information: keep implementation details inside the module; avoid
  leaking them through the interface (information leakage).
- Pull complexity downwards: the module should handle the hard cases and
  sensible defaults so callers don't have to.
- Don't split code just for length. Many tiny functions/classes ("classitis")
  move complexity into the connections between them.
  - Split when the piece is a self-contained concept understandable without
    reading its caller, is (or will be) reused, or hides real complexity
    behind a simple interface.
  - Don't split when the piece only makes sense alongside its caller, is a
    one-line wrapper, or forces readers to jump between functions to follow
    one piece of logic.

**Refactoring and reuse:**
- When the same logic appears in more than one slice, refactor it into
  `src/shared/` and import it from there. Don't copy code between slices.
- Shared code must be general-purpose (somewhat general interface, specific
  enough to be useful); keep slice-specific details in the slice.
- When refactoring into `shared/`, add or move the matching tests to
  `tests/shared/`.

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

1. Create `src/<new_slice>/` following the slice layout above.
2. Add the package to `packages` in `[tool.hatch.build.targets.wheel]`.
3. Add the name to `known-first-party` under `[tool.ruff.lint.isort]`.
4. Mirror the test directory: create `tests/<new_slice>/`.

## Technology Stack

TBC — record the chosen libraries per slice here as the project grows.
