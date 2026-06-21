# scripts/

Repo-level operational scripts (job launchers, environment setup, cleanup).
Reusable bash helpers live in `scripts/lib/` (kept out of the Python
`.gitignore` distribution rules via an explicit re-allow). Slice-specific
runtime code belongs in `src/<slice>/scripts/`, not here.
