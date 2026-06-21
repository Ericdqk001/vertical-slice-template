set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

@setup: venv-setup pre-commit-setup
    echo "Setting up..."

@venv-setup:
    uv venv --clear
    uv sync --all-groups

@pre-commit-setup:
    uv run pre-commit install
    uv run pre-commit autoupdate

@lint:
    uv run ruff format .
    uv run ruff check . --fix

@check:
    uv run ruff check .
    uv run pyright src tests

@test:
    uv run pytest
