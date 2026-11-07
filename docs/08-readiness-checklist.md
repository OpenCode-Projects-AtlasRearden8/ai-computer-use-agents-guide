# 8. The Readiness Checklist

*Before you hand over passwords or purchases.*

You've dry-ran the task ([Chapter 4](04-dry-runs.md)), you know your permission tier ([Chapter 5](05-permissions.md)), you've set the caps ([Chapter 6](06-watching-costs.md)), and you know what drift smells like ([Chapter 7](07-spotting-drift.md)). This page is the **gate** you walk through the first time an agent will touch anything valuable: a password, a payment, a purchase, or anything with your name on a public outcome.

## 8.1 Print-or-copy this list

Work top to bottom. **If you can't check an item, delay the task** — the checklist is in this order on purpose.

### Goal & scope
- [ ] I can state the desired *end state* in one sentence, and I'd recognize it if an agent weirdly achieved it.
- [ ] The task has a defined **stop point** ("stop before checkout," "draft only, don't send," "stop at the cart").
- [ ] I've decided what the agent **must not** do, and whenever possible I've fenced it with product features, not just hope.

### Plan & rehearsal
- [ ] I've seen (or asked for) the **step plan** it intends to follow, and it matches the goal.
- [ ] I've completed a **dry run** in a sandbox ([Chapter 4](04-dry-runs.md)) — including one rehearsal of the failure path ("what if the code is rejected?").
- [ ] I know the **abort move** for this tool (where's the pause/stop button, literally) and I've used it once.

### Supervision
- [ ] I'll be **within arm's reach** for this whole run — no "start it and walk the dog" for first-touch tasks or money tasks.
- [ ] I've set **max steps**, a **dollar cap**, and a **time cap** on this run ([Chapter 6](06-watching-costs.md)).
- [ ] I've scheduled when I will **verify the outcome independently** — my own eyes on the source of truth — *within the same day*.

### Secrets
- [ ] **No password will be typed into omnipresent sight.** If logins are needed: either I type the password *myself* at the moment needed, or the agent has a **dedicated account** created for it ([Chapter 5](05-permissions.md)) — minimum for the task — never my daily driver.
- [ ] My **password manager** is not fully open to the task (not the whole vault: one folder or manual entry at the moment of need).
- [ ] My **2FA stays on** for the account, on *my* device — the agent shows me a code to type, not a permanent session token grant.
- [ ] No personal data the agent *doesn't need for this step* is within its context (close other tabs; clean the profile; task-specific cookie profile).

### Money & irreversibility
- [ ] Any payment goes through a **virtual card** or other instrument with a **low cap and instant power-off**, not my main card.
- [ ] I've confirmed the steps the agent will take at **checkout / submit / send** — the atomic points where clicking quietly becomes an obligation.
- [ ] If the task is irreversible (sending, buying, publishing, deleting): the agent **must pause for explicit approval** before that step, and I've set that approval expectation in the product if it has the feature.
- [ ] I know **how to reverse** the common accidental outcomes (unsubscribe here, edit inbox there, card-freeze number saved somewhere) — or, where irreversible, I've accepted that specific risk in waking hours, not at 11 pm.

### Trust math
- [ ] This tool has earned its tier checkbook-style: I know its **logged track record** on me (quietly trivial things scrolling; not "trust me" marketing).
- [ ] The **vendor's policies** aren't actively across my red lines (screen recording, retention, training on my data) — I checked the pages I would *only* check if I cared.

## 8.2 Rulebook for passwords (a mini chapter)

Passwords are the single highest-leverage thing you can surrender to an agent, so be weirdly particular:

1. **Type it yourself.** For most personal-account tasks, you *type* the password while the agent waits. Adds fifteen seconds every time; costs one minor annoyance; removes the entire exfiltration path.
2. **Dedicated account > your account.** When the agent truly needs ongoing persistent access (e.g., a "monitoring" agent for your marketplace listings), create max-minimal accounts — dedicated email, unique strong password, 2FA to your phone, spending/rate limits where offered — and *treat it like a temp's badge*: rotate credentials on schedule.
3. **Never paste your password into a chat with any agent.** Beyond obvious exfiltration, chat logs are often retained by vendors; a memorable phrase typed *to an assistant* is a credential leak with extra steps.
4. **Shared folders only.** If a password manager integration is genuinely required, share a *single-item* or *single-folder* grant, and audit it quarterly.
5. **Session expiry is a feature.** After a run, log the agent's session out (just as you'd log out a shared computer). Standing logged-in browser profiles for agents are convenience bought with standing risk.

## 8.3 Rulebook for purchases

Purchases concentrate cost and irreversibility in a single click, so be extra deliberate:

1. **First purchase with an agent = supervised pilot**: one small, low-anger-if-wrong item (if you like the idea of agent shopping, try it as *curation* first — "find me 3 candidates and links," and you click "buy").
2. **You click "buy."** Good practice: the agent curates, adds to cart, and *you* execute the final payment step. If your tooling must auto-balance money, use the tier-3 rules ([Chapter 5](05-permissions.md)): dedicated instrument, tight ceiling, one-item scope, full supervision, immediate reconciliation.
3. **After-purchase reconciliation the same day:** does the order page show what the agent claimed? Watch your card activity for the next 72 hours if the agent stored a payment.
4. **Subscription gotchas:** agents following instructions like "start the free trial" can carry real-world legal weight. If it clicks "agree" on your behalf — you did, under the vendor's terms. Read enough *before* the pilot, and prefer tasks not entangled with agreements at all.

## 8.4 Go/no-go intuition aid

| If… | Then… |
|---|---|
| You cannot state the stop point in one sentence | Not ready. Tighten the ask. |
| Caps are unset | Not ready. 5 minutes. ([Chapter 6](06-watching-costs.md)) |
| It's your main password, your main card | Not ready. Dedicated account / virtual card, or type it yourself. |
| First real-world run with a *new* tool, and it's money/identity | Not ready. Do a second dry run with the failure path. |
| Dry run passed, caps set, fences drawn, you're free to watch until done | **GO.** |

## 8.5 Final word

None of this is about fear. It's the same self-protection any nurse, parent, or business owner already applies to *anyone* new with access to their life — **graduated trust, with the trust earned in bulk and revoked in an instant.** (You know the line nurses say about no exceptions being how the checklist saves everyone: it's only ever *sensible* constraints when you feel it's being a downer.)

The whole guide in one breath: **sandbox it, fence it, cap it, watch it, gate the secrets.** Thank you for sticking to every chapter — now go and automate, kindly.

---

Last stop: all the vocabulary in [Chapter 9 — Glossary](09-glossary.md). And for connecting agents to *tools* more generally (APIs, MCP), see the companion **agents-and-mcp-handbook**; for dividing work among *many* agents, see **multi-agent-teams-guide**.
