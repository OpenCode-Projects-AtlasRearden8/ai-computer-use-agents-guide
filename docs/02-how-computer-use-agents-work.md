# 2. How Computer-Use Agents Work

*The loop: look → think → act → check.*

## 2.1 The loop, in one picture

Every computer-use agent runs the same basic cycle, over and over, until it decides it's done:

```
   ┌──────────────────────────────────────────┐
   │                                          ▼
 [ LOOK ] ──► [ THINK ] ──► [ ACT ] ──► [ CHECK ]
   screenshot   what's my     click /     compare new
   (or DOM      plan? What    type /      screen against
   snapshot)    do I click    scroll /    what i expected
                next?         open?
```

That's a loop a human temp worker would recognize: **see, decide, do, confirm**. Modern agents can run this loop dozens of times per minute. Each turn through the loop has a cost and a chance of error, so chapters 6 and 7 are both about taming this loop.

## 2.2 What "seeing" means to an agent

The agent's eyes are not yours. Different products give the agent different things to look at:

- **Screenshots** — the agent receives pixels. It identifies buttons, fields, and text from the image. This is the most general (and most fragile) mode: it has to truly *see*.
- **DOM / Accessibility snapshots** — for browser agents, many products hand the agent a structured outline of the page (elements, names, roles). More reliable than pixels, less human-like, and it can miss things that only render visually (canvas, some styles).
- **Hybrid** — structured data to navigate, screenshots to verify. Most capable products blend both.

You don't choose this; the product does. But it matters when things go wrong: visual-only agents can misclick due to layout quirks, while DOM-based agents can misread intent (important vs. unimportant fields).

## 2.3 What "thinking" means

The agent's "brain" is a large language model (LLM). Given the current screen plus its task and history, the LLM decides: *the next step*. Not the whole plan up front — usually just one step at a time, like driving.

Sometimes products show you a "plan" (three bullet points) or a visible **cursor/ghost mouse** while it works. Some let you set **max steps**; some pause to ask when a command is ambiguous. All of these are about making the loop easier to supervise.

## 2.4 What "acting" means

Actions the agent may take, from safest to spiciest:

| Action | Typical risk |
|---|---|
| Scroll, take screenshot | None |
| Click on public site content | Low — mostly navigation |
| Fill / submit a form | Medium — rules of the site aren't yours |
| Create / send email, post comment | Medium-high — others can see your name on it |
| Sign in to an account | High — the account is now agent-accessible |
| Buy / pay / agree to legal text | Ace-high — money and terms |

A well-built agent should ask before the high-risk steps. Products differ. Chapter 5 covers how to decide what to allow.

## 2.5 What "checking" means — and why it can't be trusted alone

After acting, the agent looks at the new screen and evaluates: *did that do what I planned?* Usually it did. But the check is done by the same brain that made the mistake. If it clicked the wrong button and the resulting page is *plausible* — it may not notice. That's called **self-confirmation bias** in agent circles, and it's why Chapter 7 insists on *your own*, independent confirmation of important outcomes, not just watching the agent's success messages.

## 2.6 Why a simple task takes 30 steps

Count the click-round-trips in "order the cheapest household paper towels":

1. Open browser & search.
2. Read search results; pick the store you cared about.
3. Search within the store; read results beyond page one; compare.
4. Hit a cookie banner; dismiss it.
5. Filter by brand; re-read; add to cart.
6. Cart shows a *better deal on bulk*; reconsider.
7. Sign-in wall; decide whether to stop or ask you.
8. Cart review; "you're not buying the one you usually buy" check.

Each numbered step is 2–4 turns of the loop, each turn costing tokens and wall-clock time. Ten-by-thirty ring the bell on ten-dollar-tasks: ordinary browsing is routine; *finishing* reliably is hard. This is not a knock on agents, it's the state of them; and it's why Chapters 4–7 push you toward small, regainable tasks rather than "do my whole life."

## 2.7 Mental model to keep

> **An agent is a fast, tireless, weirdly literal temp with great typing and zero memory of what things *mean* to you.**

Fast, tireless, literal, and temporarily dumb in familiar ways. Every remaining chapter is about supervising that temp accordingly.

---

Next up: what changes when the whole world is a web page — [Chapter 3 — Browser Agents](03-browser-agents.md).
