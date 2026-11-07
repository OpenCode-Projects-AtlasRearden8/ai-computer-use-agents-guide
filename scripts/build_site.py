#!/usr/bin/env python3
"""Build a static HTML site from docs/*.md into site/.

Requires the `markdown` package (pip install markdown) and Python 3.9+.

Usage:
    python3 scripts/build_site.py
"""

import datetime
import pathlib
import re
import shutil
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

CSS = """\
:root {
  --bg: #fdfcf9;
  --ink: #23211c;
  --muted: #6b655a;
  --accent: #a4430c;
  --accent-soft: #fdf0e6;
  --line: #e6e1d7;
  --code-bg: #f4f1ea;
  box-sizing: border-box;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.7;
  font-size: 17.5px;
}
.wrap { max-width: 760px; margin: 0 auto; padding: 2.5rem 1.5rem 4rem; }
a { color: var(--accent); }
h1, h2, h3, h4 { font-family: "Helvetica Neue", Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 2rem; margin-top: 0; }
h2 { font-size: 1.35rem; margin-top: 2.4rem; border-bottom: 1px solid var(--line); padding-bottom: 0.35rem; }
h3 { font-size: 1.1rem; margin-top: 1.8rem; }
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 0.95rem; }
th, td { border: 1px solid var(--line); padding: 0.45rem 0.7rem; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); font-family: "Helvetica Neue", Arial, sans-serif; }
code { background: var(--code-bg); padding: 0.12em 0.35em; border-radius: 4px; font-size: 0.88em; font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }
pre { background: var(--code-bg); border: 1px solid var(--line); border-radius: 8px; padding: 1rem; overflow-x: auto; }
pre code { background: none; padding: 0; }
blockquote { border-left: 4px solid var(--accent); margin: 1.4rem 0; padding: 0.2rem 1.2rem; background: var(--accent-soft); border-radius: 0 8px 8px 0; }
input[type="checkbox"] { accent-color: var(--accent); margin-right: 0.35em; }
li { margin: 0.25rem 0; }
hr { border: none; border-top: 1px solid var(--line); margin: 2.5rem 0; }
.masthead { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 0.4rem; }
nav.chapters { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 0.95rem; }
nav.chapters ol { padding-left: 1.4rem; }
.pager { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; font-family: "Helvetica Neue", Arial, sans-serif; font-size: 0.95rem; }
.pager a { text-decoration: none; background: var(--accent-soft); border: 1px solid var(--line); padding: 0.55rem 0.9rem; border-radius: 8px; }
.pager .placeholder { visibility: hidden; }
footer.copyright { margin-top: 3.5rem; padding-top: 1.2rem; border-top: 1px solid var(--line); color: var(--muted); font-size: 0.85rem; font-family: "Helvetica Neue", Arial, sans-serif; }
"""

TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
MD_LINK_RE = re.compile(r'href="([^"#]+)\.md(#[^"]*)?"')
CHECKBOX_RE = re.compile(r"<li>\[ \] ")


def slug_for(path: pathlib.Path) -> str:
    return path.stem


def read_markdown_files() -> list[pathlib.Path]:
    files = sorted(p for p in DOCS.glob("*.md"))
    ordered = [DOCS / "index.md"] + [p for p in files if p.name != "index.md"]
    return ordered


def render_page(
    slug: str,
    title: str,
    body_html: str,
    chapters: list[tuple[str, str, str]],
    active_slug: str,
    footer,
) -> str:
    body_html = md_links_to_html(body_html)
    nav_items = "".join(
        f'<li><a href="{href}">{label}</a></li>'
        for href, label, _src in chapters
    )
    idx = [c[0] for c in chapters].index(active_slug + ".html")
    prev = chapters[idx - 1] if idx > 0 else None
    nxt = chapters[idx + 1] if idx + 1 < len(chapters) else None

    prev_link = (
        f'<a href="{prev[0]}">&larr; {esc(prev[1])}</a>'
        if prev
        else '<span class="placeholder"></span>'
    )
    next_link = (
        f'<a href="{nxt[0]}">{esc(nxt[1])} &rarr;</a>'
        if nxt
        else '<span class="placeholder"></span>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — Computer-Use &amp; Browser Agents Guide</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="wrap">
<p class="masthead">Computer-Use &amp; Browser Agents Guide</p>
<h1>{esc(title)}</h1>
{body_html}
<div class="pager">{prev_link}{next_link}</div>
<nav class="chapters">
<h2>Chapters</h2>
<ol>{nav_items}</ol>
</nav>
</div>
{footer}
</body>
</html>
"""


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def md_links_to_html(html: str) -> str:
    html = MD_LINK_RE.sub(lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html)
    return CHECKBOX_RE.sub(r'<li><input type="checkbox" disabled> ', html)


def extract_title(text: str) -> str:
    m = TITLE_RE.match(text)
    return m.group(1) if m else "Untitled"


def strip_title(text: str) -> str:
    m = TITLE_RE.match(text)
    if m:
        return text[m.end() :].lstrip("\n")
    return text


def build() -> int:
    if not DOCS.exists():
        print(f"error: docs/ not found at {DOCS}", file=sys.stderr)
        return 1

    md = markdown.Markdown(
        extensions=[
            "extra",       # tables, fenced code, footnote, etc.
            "sane_lists",
            "toc",
        ]
    )

    files = read_markdown_files()
    chapters_meta: list[tuple[str, str, str]] = []
    pages: list[tuple[str, str, str, str]] = []  # slug, title, html, active

    for path in files:
        raw = path.read_text(encoding="utf-8")
        title = extract_title(raw)
        slug = slug_for(path)
        html = markdown.markdown(
            strip_title(raw),
            extensions=["extra", "sane_lists", "toc"],
        )
        chapters_meta.append((f"{slug}.html", title, path.name))
        pages.append((slug, title, html, slug))

    style = CSS
    year = datetime.date.today().year
    footer = (
        '<div class="wrap"><footer class="copyright">'
        "A plain-English guide by Asdale Dynamics, LLC. MIT Licensed."
        "</footer></div>"
    )

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    (SITE / "styles.css").write_text(style, encoding="utf-8")

    for slug, title, body_html, active in pages:
        page = render_page(
            f"{slug}.html", title, body_html, chapters_meta, active, footer
        )
        (SITE / f"{slug}.html").write_text(page, encoding="utf-8")

    print(f"Built {len(pages)} pages into {SITE}/")
    for slug, title, _, _ in pages:
        print(f"  {slug}.html  <- {title}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
