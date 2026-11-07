# AI Computer-Use & Browser Agents Guide

*A plain-English tour of agents that click, type, and browse for you.*

By **Asdale Dynamics, LLC** — Dylan Asdale's beginner-friendly AI education project. We explain AI "like a friend would": step by step, never condescending.

## What this is

A guide to **computer-use agents** (software that moves a mouse and types on a keyboard for you) and **browser agents** (software that navigates web pages for you). It covers how they actually work, how to test them safely before trusting them, what permissions to give, how to watch what they cost, how to notice when they drift off track, and a readiness checklist to complete *before* you hand over passwords or let them buy anything.

Everything here is written for non-engineers. No code required — though there is a small build script if you want to regenerate the website.

## Companion guides

This is one of a family of guides, each covering a different slice of agentic AI:

- **agents-and-mcp-handbook** — connecting agents to tools via MCP (Model Context Protocol).
- **multi-agent-teams-guide** — orchestrating and coordinating teams of agents.
- **This guide** — agents that *use a computer or browser* directly: clicks, keystrokes, pages.

## How to read it

1. Start with `docs/01-agents-that-use-computers.md` — the "what and why".
2. Continue through the numbered chapters in order.
3. Keep the readiness checklist (`docs/08-readiness-checklist.md`) open the first time an agent touches anything that matters.

## What's in the repo

```
docs/               The guide itself (Markdown chapters)
site/               A static website built from docs/ (open site/index.html)
scripts/build_site.py  Rebuilds site/ from docs/
```

## Building the site

The website is plain static HTML with no external dependencies. Rebuild it any time with Python 3:

```bash
python3 scripts/build_site.py
```

That reads every `docs/*.md` file and writes `site/index.html` plus per-chapter pages into `site/`. You can open `site/index.html` directly in a browser or serve it locally:

```bash
python3 -m http.server 8000 --directory site
```

## Safety defaults baked into this guide

- Test in a **throwaway browser profile or sandbox first** (Chapter 4).
- Give the **least permission required** (Chapter 5).
- **Watch costs** with a hard cap (Chapter 6).
- **Spot drift** before it compounds (Chapter 7).
- **Never give passwords or payment approval** before completing the readiness checklist (Chapter 8).

This guide is educational only. It describes third-party tools in general terms and does not endorse any specific product, and it is never a substitute for your own judgment.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
