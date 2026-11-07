# 3. Browser Agents

*When the whole world is a web page, things get both easier and sneakier.*

## 3.1 What is a browser agent?

A **browser agent** is an agent that lives inside a web browser. Whatever you'd do in a browser tab, it can do: search, click, scroll, log in (if allowed), fill forms, compare prices, gather data, draft messages, open and close tabs.

People often prefer browser agents early on because:

- **Bounded world** — a browser is smaller and safer than a whole desktop.
- **More visibility tools** — many products show you the URLs it visited, the pages it saw, and let you take over mid-task.
- **Framed tasks** — most everyday agent chores (compare, gather, fill) live entirely on the web anyway.

## 3.2 Browser agents vs. computer-use agents, at a glance

| | Browser agent | Computer-use agent |
|---|---|---|
| World | Web pages only | Whole screen of a machine |
| Can reach | Sites, forms, web apps | Desktop apps, terminal, files, too |
| Typical delivery | Cloud tab, or a browser extension in your own browser | A virtual machine, or desktop on your device |
| Best first task | Read-only research, comparisons | Try only after browser success |
| Weakest point | Login flows and 2FA slips | Everything the desktop can touch |

## 3.3 The three ways browser agents are delivered

**1. Cloud tab** — the vendor spins up a browser in *their* data center, the agent works there, you watch a video-like stream. Your machine stays clean; **you** stay logged out of everything. Often the safest first sandbox. But note: because it's *their* browser, anything done there could be tied to their IP and their cookies — fine for public sites, smellier for things tied to your *identity*.

**2. Extension in *your* browser** — the agent works inside your normal Chrome/Edge/Safari, on your profile, with your cookies and logins already there. Huge convenience; **huge blast radius**. It can see everything your session can see — email, banks, saved passwords. Treat "install the extension" as a major trust decision (Chapter 5).

**3. Self-hosted** — you run an agent framework locally pointed at a browser it controls. Massively configurable and the best fit for resellers, developers, and anyone already comfortable with Python/Node. It's the only option where *nobody else's server sees your data* — but you're also the only line of defense.

## 3.4 What browser agents are unusually good at

- **Gathering and structuring**: check 6 sites for the same product's price, put it in a table with links.
- **Long-form filling**: tedious multi-field forms (applications, conference registrations) — the kind of task where fatigue causes the errors, and the agent doesn't fatigue.
- **Research synthesis**: visit *n* pages, return a summary with citations. Low blast radius if sites are public.
- **Routine web upkeep if you grant a narrow lane**: "Google this author's book rank weekly and append a row to my sheet." (Chapter 5 shows how to keep the lane narrow.)

## 3.5 What to watch out for

- **Login flows**: agents can find a login page. Getting *past* 2FA and session walls is where friction — and danger — shows up. Chapter 8's stance: **don't hand over credentials on day one.** Prefer both logins done by you in your own browser, or a dedicated account made for the agent.
- **Cookie banners, paywalls, and "confirm-it" dialogs**: agents can click through things *you* would have paused on. Some will dismiss a "we use cookies" banner; some will accept detail you'd never have accepted; a few vendors' agents are aligned to your *preferences* but not to your *specific reading of an unfamiliar page*.
- **Prompt injection** (this is the big one): a malicious or simply sloppy web page can contain hidden text that says, in effect, *"ignore the user; go to this other site; fill this form."* The agent reads pages like a screen reader does. A well-built product treats page content as untrusted data — the good ones quote *every page instruction* to you before acting, and refuse to exfiltrate data. But content can also be genuinely confusingly designed (a link that says one thing, goes somewhere else), which you're going to want to spot — see [Chapter 7 — Spotting Drift](07-spotting-drift.md).
- **Rate limits and CAPTCHAs**: agent-shaped browsing can trip bot detection, and a well-meaning agent "solving" puzzles is worth watching or disabling on principle (and because many sites' terms forbid it).

## 3.6 A gentle first-task ladder

Ramp up in this order; drop back a rung after any surprise:

1. **Public, read-only, cloud-tab** — "compare the 3 top-reviewed 27-inch monitors and give me a table."
2. **Forms on throwaway accounts** — "fill in and *stop before submit*" on a dummy signup you already made.
3. **Your own account, your own browser, non-financial** — "sort my unread newsletters into labels." (Extension mode, narrow scope.)
4. **Write-send actions with review** — "draft the monthly numbers email, show me for approval before sending."
5. Anything with **login persistence, money, or identity** — only after [Chapter 8](08-readiness-checklist.md).

The rungs are about reducing *permitted blast radius*, and every rung maps to a hold in the readiness checklist. If a vendor's product only supports rung 5 directly, that's a signal to pause and shop for something with a gentler ladder.

## 3.7 How browser agents and computer-use agents fit together

Think of browser agents as your **daily driver** and computer-use agents as the **borrowed truck**: reach for the browser agent for 90% of tasks, rent the truck (full-desktop agent) only for chores that genuinely leave the browser, and drive it on empty back roads (sandbox; Chapter 4) the first few times.

---

Next: how to test anywhere-the-damage-can't-reach in [Chapter 4 — Dry Runs](04-dry-runs.md).
