# 6. Watching Costs

*Why clicking costs tokens — and how to stay under a budget.*

## 6.1 Why agents cost more than chat

In plain terms: a chat message sends a snapshot of text and gets text back — one round trip. A computer-use agent sends a snapshot of text **plus a screenshot or page outline**, then acts, then **sends a new snapshot** after every click to figure out what changed. One task = potentially dozens of round trips, each shipping a heavy visual payload to the model.

That's the meter, and it spins with the loop in [Chapter 2](02-how-computer-use-agents-work.md):

| Task | Typical turn count | What drives the spend |
|---|---|---|
| Chat answer | 1–5 turns | Message length. |
| Browser agent price-compare | 20–80 turns | Pages fetched, images, retries. |
| Full computer-use desktop chore | 40–150 turns | Scrolling, many steps, recovery. |

Bigger screens cost more to send than smaller ones; scrolling costs clarify; failed navigation costs get re-sent. Two tasks that "look the same" can differ by 10× because one hit popup after popup.

## 6.2 Know your pricing shape

Products bill in one of these shapes; know which you're on:

1. **Subscription with usage caps/credits.** "N tasks/month" is usually a *step* budget, not truly unlimited — watch for meters and overage asks.
2. **Metered tokens.** Pay per snapshot-and-action turn, per images in context, and per output. Transparency is a feature here; the good ones show per-task cost.
3. **Per successful task.** Nice incentive alignment; just check *what counts as success* before an abandoned run still bills.
4. **Self-hosted compute.** Pay in hardware/time; the "cost" becomes your machine's RAM/GPU and electricity — and your *attention* while babysitting.

If a vendor shows **no way to see per-task cost**, Chapter 6's advice slows you down or stops at a paid boundary until you can see the meter.

## 6.3 The three caps

Set all three before any run beyond a dry run ([Chapter 4](04-dry-runs.md)):

### Cap 1 — Turn cap ("max steps")
Set it to your *expected shadow* + 30%. If the agent needs 30 clicks, cap at ~40. The agent hits the cap and stops instead of wandering forever. When it stops at a cap: don't just restart from scratch — read its log to find *why it wandered* (usually a popup, a wrong-notation page, or a repeated failed click).

### Cap 2 — Dollar cap
Budget per run: "this must cost under $X." For a first real-world run, make **X small enough to shrug off** (a coffee, not a tank of gas). Products meter by subscription credits instead of dollars? Then the equivalent is "no more than N tasks this month on experiments."

### Cap 3 — Time cap
Agents left to run while you sleep can bill long into the night. Decide "none of my runs last longer than M minutes" and enforce it with the product's stop control or a wall-clock habit (start the microwave, check the clock).

## 6.4 Understand what to re-run (and never to)

- **Research, comparisons, drafting, sorting** → safe to re-run; costs are low, outputs are expendable, and fresh runs often produce *better* results after a tool update.
- **Form submissions, purchases, sends, deletes** → **never auto re-run**. A repeated e-commerce flow can double-charge; a repeated send doubles the send.
- **Anything that hits a real-world API limit or rate limit** → the last thing you want is an agent retrying into a charge cycle. If error text includes "too many," stop.

## 6.5 Watch costs like a checkbook, not like a mood

Before any agent spending time on *your* money, do simple bookkeeping:

1. **Log each run** (or use the product's history): date, what task, what it did, cost in dollars (or credits/time), outcome.
2. **Weekly check** if you're a hobbyist; **per-run check** if you've set up recurring automation (Chapters 5 and 8 point to a notification and a schedule respectively).
3. **Once monthly, roll up**: how much did agents *actually* save vs. how much they cost in dollars + your babysit-time? Retire the tasks that don't pay for themselves. Agents are a tool; keep the ones that pay rent.

If a run goes over budget, don't just eat it — write down *why it ballooned*. Usually it's one of: unexpected 2FA wall; ambiguous target (similar/competing product pages); popup handling; or the task was bigger than one run should be. Each cause has a fix (a [permission fence](05-permissions.md), a narrower ask, a [dry-run rehearsal](04-dry-runs.md), a split task).

## 6.6 Mindset

> **Agents are like a well-meaning contractor: great value when you hand them a defined job with a materials budget; ruinous if you hand them a credit card and "make the house nice."**

Cap the steps and dollars per *specific task*; check the invoice habitually; re-run cheap things and never automatic-re-run expensive things. Then move to the discipline that catches the errors these caps *won't* — [Chapter 7, Spotting Drift](07-spotting-drift.md).
