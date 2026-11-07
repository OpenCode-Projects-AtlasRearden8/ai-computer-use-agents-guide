# STATUS.md

*Last updated: 2026-11-07*

## What was built

**AI Computer-Use & Browser Agents Guide** — a plain-English beginner manual about agents that click, type, and browse for you, published as Markdown docs plus a static HTML website, by Asdale Dynamics, LLC (Dylan Asdale).

### Contents

- `docs/` — 10 Markdown chapters:
  - `index.md` — overview and chapter map
  - `01-agents-that-use-computers.md` — what computer-use agents are vs. chatbots/macros/RPA, strengths and limits
  - `02-how-computer-use-agents-work.md` — the look → think → act → check loop, screenshots vs. DOM, why simple tasks take many steps
  - `03-browser-agents.md` — browser vs. desktop agents, cloud-tab/extension/self-hosted delivery models, prompt injection, a first-task ladder
  - `04-dry-runs.md` — plan-only rehearsal, throwaway browser profiles, VMs, mock targets; a 90-second grading script
  - `05-permissions.md` — blast-radius mindset, an account/screen/writes/money/files permission checklist, permission tiers
  - `06-watching-costs.md` — why agents cost more than chat, billing shapes, the three caps (steps/dollars/time), what is safe to re-run
  - `07-spotting-drift.md` — per-run, cross-run, and harness drift; five detection habits; incident recovery
  - `08-readiness-checklist.md` — a printable gate before handing over passwords or purchases, plus password and purchase rulebooks
  - `09-glossary.md` — plain-English glossary
- `site/` — generated static website: one HTML page per chapter (`index.html` through `09-glossary.html`) plus `styles.css`. No JavaScript, no external assets, no tracking.
- `scripts/build_site.py` — Python build script (uses the `markdown` package) that converts `docs/*.md` into the pages in `site/`, rewriting internal `.md` links to `.html` and task-list checkboxes into real checkbox inputs.
- `README.md` — project overview, structure, build instructions; credits Asdale Dynamics, LLC.
- `LICENSE` — MIT; copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.

### Distinct from companion guides

- **agents-and-mcp-handbook** (agents ↔ tools via MCP) covers API-style tool connection; this guide covers *hands-on-computer* agents.
- **multi-agent-teams-guide** covers coordinating multiple agents; this guide covers supervising a single agent with a mouse and keyboard.

## How to run it

Rebuild the site (requires Python 3.9+ and `markdown` 3.x, e.g. `pip install markdown`):

```bash
python3 scripts/build_site.py
```

Then open `site/index.html` in a browser, or serve locally:

```bash
python3 -m http.server 8000 --directory site
```

## Verification results (2026-11-07)

- `python3 scripts/build_site.py` → builds 10 pages successfully; no errors.
- Static analysis of generated site: 10 HTML pages, 110 internal `<a href>` links, all link targets resolve to existing files (no broken links, no stray `.md` hrefs).
- `docs/` cross-chapter links verified valid against the file list.
- Served the site with `python3 -m http.server` and fetched `index.html`, `08-readiness-checklist.html`, `09-glossary.html`, `styles.css` → all HTTP 200.
- Checked rendered HTML: 19 checkboxes render in the readiness checklist; fenced code blocks and tables render in chapters 2–4.
- Scanned all files for secrets, API keys, and personal data → none present; all content is generic education.
- No network access needed to read the site; no JavaScript; no external fonts/CDNs.

## Known gaps / next steps

- The site is single-directory, page-per-chapter; no in-page table of contents, search, or print stylesheet.
- No dark mode.
- `build_site.py` is a thin wrapper over the `markdown` package; tests are not automated — the verification steps above are manual/ad-hoc. A small automated test file is a natural next step.
- Product-specific examples are deliberately generic (no named vendor products); a future edition could add a vendor-agnostic comparison table with dated, sourced notes.
- Chapter 10 candidates: phone/mobile agents, screenshot-based QA workflows, and an agent-incident log template.
