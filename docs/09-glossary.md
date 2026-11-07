# 9. Glossary

*Every term in this guide, in plain English.*

**Agent** — AI software that takes actions toward a goal, not just answers questions. Contrast: a chatbot only talks.

**Allowlist** — a list of things explicitly permitted (sites it may visit, actions it may take). Safer than a blocklist, which tries to name everything forbidden.

**Blast radius** — the maximum harm possible if something goes wrong: "this agent has access to my bank and mail, so its blast radius is huge."

**CAPTCHA** — those "prove you're human" challenges. Agents being asked to solve them is usually a sign the site forbids this kind of traffic, and often against the site's terms.

**Cloud browser** — a browser running on the vendor's servers, streamed to your screen. Your machine stays clean because the browsing never touches it.

**Computer-use agent** — an agent that operates an entire computer screen: mouse, keyboard, applications. The general case; bigger powers, bigger risks.

**Cookie / session** — a site's memory that "this browser is logged in." Cookies an agent keeps are standing access; prune or clear between runs.

**DOM / accessibility snapshot** — the structured "skeleton" of a web page (what elements exist and what they say). Browser agents often read this instead of (or alongside) screenshots.

**Drift** — an agent wandering from your goal, over one run or many. Covered in [Chapter 7](07-spotting-drift.md).

**Dry run** — a rehearsal of the task somewhere harmless. Covered in [Chapter 4](04-dry-runs.md).

**Extension (browser)** — a small program installed inside your browser. An agent in extension mode can work on your actual logged-in sessions — convenient, high blast radius.

**Least privilege** — granting only the permissions required, nothing more. The core principle of [Chapter 5](05-permissions.md).

**LLM (large language model)** — the "brain" that reads the screen and chooses actions in most agent products.

**Loop (agent loop)** — the look → think → act → check cycle agents repeat until done. Covered in [Chapter 2](02-how-computer-use-agents-work.md).

**Max steps / turn cap** — a limit on how many actions an agent may take in one run. Your first defense against a runaway agent.

**MCP (Model Context Protocol)** — a standard way to connect AI to tools and data. The subject of the companion guide, the **agents-and-mcp-handbook**. Distinct from computer use: MCP gives an agent an *API* into a tool, while computer-use gives it *hands*.

**Multi-agent teams** — coordinating several agents (a researcher, a writer, a checker). The subject of the companion guide, the **multi-agent-teams-guide**.

**Prompt injection** — text on a web page (or in content an agent reads) that tries to hijack the agent and make it do the attacker's task instead of yours. The big web-specific risk in [Chapter 3](03-browser-agents.md).

**RPA (Robotic Process Automation)** — older, rule-based enterprise automation. Follows fixed scripts; doesn't adapt like an agent does.

**Sandbox** — an isolated environment (throwaway browser profile, virtual machine, cloud browser) where the agent can act without touching anything real.

**Snapshot (VM)** — a saved state of a virtual machine you can restore to after a run, wiping everything the agent did.

**Token** — the unit AI models read and write text in; also how many AI services charge. Agents consume far more tokens than chat because every step ships a fresh screen.

**Turn / step** — one cycle of the agent loop: look, decide, act. Costs are per turn; caps are in turns.

**Virtual card** — a card number from your bank with its own limit, usable once or for one vendor, and killable instantly. The best instrument for agent purchases.

**VM (virtual machine)** — a computer running inside your computer, throwaway by design. The strongest(ish) sandbox for full computer-use agents.

**2FA (two-factor authentication)** — a second proof (a code on your phone) beyond a password. Keep it on for any account an agent touches, on *your* device.
