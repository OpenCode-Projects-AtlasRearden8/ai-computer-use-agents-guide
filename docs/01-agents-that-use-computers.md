# 1. Agents That Use Computers

*A plain-English tour of agents that click, type, and browse for you.*

## 1.1 The chatbot vs. the agent

You already know one kind of AI: the **chatbot**. You type a question, it types an answer. It can write an email for you — but *you* copy it, paste it, hit send.

A **computer-use agent** is a different animal. You say the goal — *"find me the cheapest flight April 4–7, then draft an email to Priya with the options"* — and the agent does the whole thing itself:

1. It opens a browser window.
2. It looks at the page and decides where to click.
3. It clicks, types, scrolls, fills forms.
4. It reads the results and keeps going.
5. It stops and shows you what it did.

The difference isn't intelligence, it's **hands**. A chatbot has a mouth. An agent has a mouth, eyes, and a mouse.

## 1.2 Browser agents vs. computer-use agents

You'll meet two flavors, and it's worth keeping them straight:

**Browser agents** operate *inside a web browser only*. The web is the whole world to them. They can fill forms, search, compare prices, and navigate sites — but they can't touch your desktop apps, terminal, or files.

**Computer-use agents** operate *the whole screen* on a real or virtual machine. Anything you could do with a mouse and keyboard — export a spreadsheet from a desktop app, run a terminal command, arrange lightroom photos — is theoretically within reach. With the whole desktop comes the whole blast radius.

(Chapter 3 covers browser agents in detail; most of Chapter 2's loop applies to both.)

## 1.3 Wait — isn't this just macros? Or RPA?

Fair question. You may have heard of:

- **Macros & script recorders** — repeat a fixed series of steps. Break the moment a button moves or a popup appears.
- **Robotic Process Automation (RPA)** — enterprise software that automates application workflows via fixed rules and integration points. Powerful, but someone engineers every rule up front.

Agents differ at the foundation: they are **vision-and-judgment driven**. They look at whatever is actually on the screen, like a human temp worker would, and adapt when the screen isn't what they expected. That means:

- ✅ They can handle pages and apps that were **never designed for automation**.
- ✅ They can **recover** when a popup, cookie banner, or rename appears.
- ❌ They can also make **plausible-looking mistakes** a script would never make — like clicking the *wrong* "Delete."
- ❌ They are typically much **slower and more expensive** than a script, per step.

A macro follows a map. An agent drives by looking out the windshield. Most of this guide is about the windshield style of risk.

## 1.4 What good agents are actually good at

Based on where everyday tools stand today, agents tend to shine at tasks that are:

- **Boring but well-specified**: gather all your own recent orders across 4 sites into one table.
- **Read-heavy, write-light**: research, compare, summarize, draft.
- **Low stakes per step**: browsing public pages, searching, filling test forms.
- **Bounded in time and scope**: "spend at most 20 clicks" beats "handle my whole inbox."

They struggle with tasks that are:

- **Long-chain and unforgiving**, where one wrong click ruins everything (e.g., final purchase confirmations).
- **Vague**, where the goal requires taste or context the agent can't infer ("clean up my photos" — what does *clean* mean?).
- **High-stakes outputs** summed up from messy inputs (anything involving your money, identity, or legal standing).

## 1.5 The pitch and the catch

The pitch: **general-purpose automation without engineers.** Anyone who can describe a task can have it done. That's genuinely new, and for nurse-turned-author workflows like "check my book's rank and post the numbers into a sheet," it can feel like magic.

The catch: **agents fail like interns, not like software.** Software fails with an error message. An agent can fail by doing the *wrong thing confidently* — clicking "Similar" instead of "Exact," buying the size-up, replying *Cc: everyone*. So the operating stance in this guide is:

> **Try it where failure is cheap; supervise closely; verify outputs like you'd verify a temp employee's work; and only escalate trust as performance earns it.**

That stance has a name in the next chapters: dry runs (Chapter 4), least-privilege permissions (Chapter 5), cost caps (Chapter 6), drift-watching (Chapter 7), and a readiness gate before secrets or purchases (Chapter 8).

## 1.6 Quick quiz

1. Your automation breaks every time the site redesigns a button. Fixed script or agent? *(Agent — it re-reads the screen each time.)*
2. The task requires opening your tax software, a desktop app, filling from a PDF. Screen-only agent or browser-only agent? *(Screen-only — computer-use agent.)*
3. You want it to order your groceries. Right now? *(Not yet — read Chapter 8 first.)*

---

Next: what's going on under the hood in [Chapter 2 — How Computer-Use Agents Work](02-how-computer-use-agents-work.md).
