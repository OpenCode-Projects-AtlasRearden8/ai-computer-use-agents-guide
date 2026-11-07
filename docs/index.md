# The Guide at a Glance

*A plain-English tour of agents that click, type, and browse for you.*

Welcome! If you have ever wished an assistant could just **do the thing** — fill in the form, sort the email, compare the prices, book the appointment — instead of merely telling you how, this guide is for you.

That's what **computer-use agents** and **browser agents** are: AI software that operates a computer the way you do. They look at the screen, decide what to do next, move the mouse, type on the keyboard, and open web pages. You describe the goal. They handle the clicking.

## Who this is for

Anyone curious about "AI that uses the computer for me" — no engineering background required. We'll say what the jargon means the first time we use it, then mostly avoid it.

## What you'll learn, chapter by chapter

| Chapter | Question it answers |
|---|---|
| [1. Agents That Use Computers](01-agents-that-use-computers.md) | What *is* a computer-use agent, and how is it different from ChatGPT or a macro? |
| [2. How Computer-Use Agents Work](02-how-computer-use-agents-work.md) | The loop: look → think → act → check. What "seeing" means to an agent. |
| [3. Browser Agents](03-browser-agents.md) | What changes when an agent lives inside a browser instead of at the whole screen? |
| [4. Dry Runs](04-dry-runs.md) | How to test an agent somewhere nothing bad can happen. |
| [5. Permissions](05-permissions.md) | What am I actually allowing, and how do I keep the blast radius small? |
| [6. Watching Costs](06-watching-costs.md) | Why clicking costs tokens, and how to stay under a budget. |
| [7. Spotting Drift](07-spotting-drift.md) | How to notice an agent going off-track before it compounds. |
| [8. The Readiness Checklist](08-readiness-checklist.md) | What to have in place *before* handing over passwords or purchases. |
| [9. Glossary](09-glossary.md) | Every term in the guide, in plain English. |

## How to use this guide

- **Read chapters 1–3 straight through.** They build one mental model.
- **Treat chapters 4–8 as a toolkit.** Each one is a safety habit you can adopt in a few minutes.
- **Never skip chapter 8.** It's the difference between an assistant and an accident.

## The one-paragraph version

Computer-use agents are a new kind of software: they don't have special APIs into your apps — they use the same screen and keyboard you do. That makes them wonderfully general (anything you can do, they can *attempt*) and wonderfully risky (attempts can go wrong in human ways). The whole of this guide is about getting the upside while keeping risk small: test in a sandbox, grant few permissions, watch the meter, watch the behavior, and only then — if ever — hand over something valuable.

Let's start with what these things actually are.
