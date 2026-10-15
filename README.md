# vertical-slice-template

A starter template for research projects using a **vertical-slice
architecture**. Each experiment/model is an isolated slice under `src/`,
sharing only what lives in `src/shared/`. Tooling (uv, ruff, pyright, pytest,
pre-commit) is pre-wired to match the conventions in `CLAUDE.md`.

## Use this template

Click **"Use this template"** on GitHub, or:

```bash
gh repo create <name> --private --template Ericdqk001/vertical-slice-template
```

Then rename `<PROJECT_NAME>` in `CLAUDE.md` and `pyproject.toml`.

## Setting up

### Install uv

* Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
* macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Install Just (command runner)

* Windows: `winget install --id Casey.Just --exact`
* macOS: `brew install just`
* Linux: see https://github.com/casey/just#installation

### Run (in a new terminal)

```bash
just setup     # create venv, sync deps, install pre-commit hooks
just test      # run the test suite
just check     # ruff + pyright
just lint      # format + autofix
```

## Layout

```
src/
  shared/            # cross-slice reusable code
  <slice_name>/      # one directory per experiment
    main.py          # CLI entrypoint
    config.yaml      # run config
    build_metadata.py
    scripts/data.py  # dataset/dataloader
    explore/         # throwaway exploration + reports
tests/
  <slice_name>/      # tests mirror the source tree
  shared/
```

See `CLAUDE.md` for conventions and the "Adding a new slice" checklist.
