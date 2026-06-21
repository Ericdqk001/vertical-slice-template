#!/usr/bin/env bash
# Reusable setup helper sourced by job-launch scripts.
# Keeps environment bootstrapping in one place across slices.
set -euo pipefail

# Resolve the repo root regardless of where the caller runs from.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export REPO_ROOT

# Activate the uv-managed virtualenv if present.
if [[ -d "${REPO_ROOT}/.venv" ]]; then
  # shellcheck disable=SC1091
  source "${REPO_ROOT}/.venv/bin/activate"
fi
