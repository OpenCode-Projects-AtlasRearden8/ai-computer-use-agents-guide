# 5. Permissions

*What am I actually allowing? Keep the blast radius small.*

## 5.1 The blast-radius mindset

With agents, "what could go wrong" is best thought of as **blast radius**: if this agent has a bad day, what is the *maximum* damage?

- Agent in a cloud browser, logged out, read-only → radius ≈ whatever pages it looked at.
- Agent as an **extension in your everyday browser** → radius ≈ your whole digital life: mail, banks, saved passwords, autofill, history.
- Agent on a VM → radius ≈ what's in that VM plus its allowlisted network paths.

Every permission decision below is about **shrinking the radius before the run**, not cleaning up after.

## 5.2 The checklist of permissions to think through

### Screen & sessions
- **What can it see?** Screen-recording permissions on Mac/Windows are account-wide. A screen agent sees every notification that pops up while it's there — patient health info, two-factor codes, salary letters. **Close personal windows before runs.**
- **Which browser profile?** Give it a **dedicated profile** (fresh, minimal, no saved passwords, no autofill), never your daily profile.

### Accounts
- **Never your personal login.** If a task needs an account, create **a dedicated account for the agent**, with:
  - an email address separate from your primary;
  - **minimal privileges** (read-only? comment-only? non-admin?);
  - your own 2FA device, with a separate app account or hardware token;
  - spending caps, if the service supports them.
- **Password managers:** if you must, grant access to *one folder* containing the specific credentials for *this* task's sites — not the vault. (Even better: type the password in yourself at the moment of need; see [Chapter 8](08-readiness-checklist.md).)

### Web-writes
- **Publishing, posting, emailing.** Grant selectively: maybe "may comment here" but "may not send email ever," or "may send but only to these addresses." Many products let you lock reads vs. writes; if a product can't distinguish, that's a yellow flag.
- **Update/publishing platforms:** never an "admin" role on day one; reviewer or editor first. Agents don't need "delete site" buttons.

### Money
- **Payment methods:** never your daily driver card. If a task *must* pay, use a **virtual card with a low dollar cap** from your bank's card controls — you can raise the cap later, revoke instantly today.
- **Purchase approval:** good products offer "**ask me before checkout**" or "confirm-cart-then-pause" modes. Turn it on for anything that spends.

### Filesystem & machine
- **Working directories** for file outputs should be one folder, not "C:\Users\you." Agents given a whole disk can *read* whole disks.
- **Downloads & uploads** are exfiltration paths and brand-new attacker surfaces. Restrict or review regularly.

### Network
- **Where can it go?** Allowlists beat blocklists whenever a product supports them. If not, plan the amount of browsing into the task and give max-steps caps instead.

### Long-lived things
- **Cookies / saved sessions** = standing access. Self-hosted browser profiles that keep logins between runs are convenient *and* are effectively a locker full of keys. Prune old sessions periodically; re-authenticate at the frequency of your tolerance for damage.
- **API keys / service tokens** the agent might carry for some products: treat as secrets. Rotate if in doubt. Never paste your keys into a live chat with an agent.

## 5.3 Concrete permission tiers

A simple, copyable policy you can keep in one note:

**Tier 0 — Observe-only.** Public pages, no logins, no form-fills, screenshot-in-screenshot-out, max 15 steps, $0.
*Use for: first touch on any new tool.*

**Tier 1 — Assisted research.** Public pages plus form-fills on throwaway profiles; no submits; cloud browser or fresh profile.
*Use for: comparisons, drafts, price tables.*

**Tier 2 — Logged-in light writes.** One special account, minimal grant; writes allowed only [labels, folders, drafts, saved views, not sending]; virtual card slug for $0; approval before any submit.
*Use for: inbox sorting, draft emails, sheet appends.*

**Tier 3 — Money & identity.** Real account, real payment, real-world effect. Only after [Chapter 8](08-readiness-checklist.md)'s checklist is complete; virtual card with a low cap; human-confirm every purchase; start once and supervise fully.

Escalate one tier at a time; de-escalate freely (you can always pull permissions back without any drama by blowing away cookies/profiles or rotating credentials).

## 5.4 Watching your permissions over time

- **Write down what you granted.** A single note listing what the tool has access to (with dates) turns re-audits into a five-minute chore, not an archaeology project.
- **Spring-clean quarterly.** Look at installed browser extensions, cookie jars, connected-account lists (Google/Apple/Microsoft "security" pages), and admin roles for the bots you've added.
- **When a product changes hands / changes terms**, re-derive Tier 0 for it; don't grandfather trust across company boundaries you didn't choose.

## 5.5 One last framing

**Never hand over the keys to the C-suite.** Instead of "you may do anything with my email," try: "You may *sort* my email, show me three drafts, and send only the one I pick." That's one mental model swap: **least privilege is not a gate to keep the agent out — it's a fence that keeps the agent *and* you inside a bounded experiment.**

That fence — permissions — plus a budget (Chapter 6), a check habit (Chapter 7), and a checklist (Chapter 8) is most of what separates happy experimenting from a cautionary tale.

---

Next: the dollar meter, in [Chapter 6 — Watching Costs](06-watching-costs.md).
