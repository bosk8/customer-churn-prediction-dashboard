# Style Decisions Log

Timestamp format: YYYY-MM-DD HH:MM

## Assumptions
- 2025-10-30 00:00 — Streamlit app will host custom CSS via injected `<style>` using variables from `style.md`.
- 2025-10-30 00:00 — Single-page layout; no multi-route nav required initially.

## Derivations
- 2025-10-30 00:00 — Button component derived from link/label rules: uppercase, `letter-spacing: .05em`, hover ≤200ms; uses `--text-muted` → `--text-primary` on hover; border via `--border-w` `--border-color`.
- 2025-10-30 00:00 — Table row hover color uses FAQ hover background `#18181b` to maintain subtle hover behavior, since a dedicated table hover token is not in `style.md`.

## Conflicts & Resolutions
- 2025-10-30 00:00 — Need sticky headers in table; not explicitly listed. Resolution: Allowed under "Grid & Layout" and border utilities; implement with neutral borders and `--surface-card` without introducing new tokens.


