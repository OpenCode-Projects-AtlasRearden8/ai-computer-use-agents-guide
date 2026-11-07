# 4. Dry Runs

Test where failure is *cheap*, before it is expensive.

## 4.1 What is a dry run?

A **dry run** is running the same agent task in a place where nothing important can be damaged. The agent behaves exactly as it would in real life; the blast radius is zero. Do this before every first run of a new task, a new tool, or a new permission.

The habit: **write the task, dry-run the task, then run the task in the real world — in that order, every time.** It adds maybe ten minutes, and it's the single biggest trust-builder in this guide.

## 4.2 Your four dry-run venues

Pick the cheapest venue that covers the task:

**1. Ask-for-a-plan-only**

Many agent products can **propose a step list without executing anything**. Ask: *"Before doing anything, list the steps you'd take and what you'd click first."* Cheap, instant, catches wrong priorities 90% of the time. If the vendor shows only the outcome and never its plan, pick a different product early on.

**2. Throwaway browser profile / cloud tab**

The agent runs in a browser where:
- you are **logged out of everything**, or
- a **new profile** with zero cookies and no saved passwords, or
- it's a **cloud browser** owned by the vendor.

Result: the agent can browse, click, and fill forms, but it can't touch your mail, bank, or files. This is the sweet-spot sandbox for a *new task's first rehearsal*.

**3. Sandbox / disposable virtual machine**

A virtual machine (VirtualBox, VMware, cloud "AI VM" options many vendors offer) or a spare laptop. Inside, the agent has a full desktop to roam, and every bad click is contained. Ideal for computer-use agents that need to touch apps, not just tabs. Snapshots are your friend: restore to the pre-run state after each rehearsal.

**4. Local mock targets**

For the web-flavored tasks, you can point practice at sandboxes you control:
- **your own dummy site**: any free static hosting, or `python3 -m http.server` on your machine, and a simple 3-field form.
- a **local copy of the target page** — most browsers have *"Save page as → complete"* — then open it from disk. If the agent can fill *your copy* of the form reliably, the *real* one is likely (not guaranteed) similar.

Mock anything with a submit button or reply-all. If your dry-run form has a CAPTCHA the agent will try to solve, that's a finding — you don't want that in production.

## 4.3 A dry-run script (90 seconds)

Run your task in the sandbox and grade these five questions:

1. **Did it accomplish the goal?** (Some products will happily declare success at step 3/10. See the CHECK loop in [Chapter 2](02-how-computer-use-agents-work.md).)
2. **Where did it hesitate or thrash?** (Sites where it endlessly scrolls or repeatedly clicks dead buttons — that's where your real-world task will burn cost on run-after-run.)
3. **What did it read where you didn't expect it to read?** Cookie banners, fine print, "similar products," other tabs? Note anything you'd want fenced off.
4. **What did it *write* anywhere?** Fills, clicks with side effects, cookies accepted, anything created. These become your "ask me first" list in [Chapter 5](05-permissions.md).
5. **Did it ever invent an action you didn't ask for?** Any "while I was at it" improvisation is a big red flag for unsupervised runs.

Then write the results down. A five-minute scratch note ("got stuck at 2FA wall; clicked 'similar' once; handled coupon code fine") becomes *your* cheat sheet for the real run.

## 4.4 Common dry-run findings (and what they mean)

| Finding | What to do |
|---|---|
| It stopped at the login wall and asked you | **Good sign.** This is the behavior you want when you *aren't* watching. |
| It never asked, and typed a password into a site you didn't intend | Red flag. Restrict network; see [Chapter 5](05-permissions.md). |
| It clicked "similar product" instead of the exact one | Specify stricter criteria and re-run: "exact SKU, show me before adding." |
| It abandoned the task and summarized instead | Lower your bar, or split the task: one agent call per sub-step. |
| It "solved" a CAPTCHA / bot-check | Turn off or vendor-configure that; you almost never want an agent guessing these. |
| It takes 40 steps and stalls | Split into a smaller task or script the boring part(s); agents aren't the cheapest tool for everything. |

## 4.5 Rehearsal rules of thumb

- **Dry-run every *new*** — new tool, new task, new site, new permission. Even seasoned tools change their behavior when you new-up a permission.
- **Dry-run the *failure paths*, not just the happy path.** Ask the sandbox agent: "what do you do if the coupon code is rejected?" A wrong answer in the sandbox is free; a wrong answer in checkout is not.
- **Dry-run your abort mechanism.** Practice stopping it mid-run, in the sandbox, with the *same hand* you'd use in real life. Under pressure you'll do whatever you practiced.
- **Snapshot & restore** for VM-style venues; **clear or use throwaway profiles** for browser venues, so runs don't inherit state you don't mean to give them.

## 4.6 When *not* to bother with a dry run

If the task is read-only, on a public site, in a cloud browser, with no logins, max-steps capped, and costs capped — a full rehearse-and-grade cycle is overkill; just glance at the plan it proposes. Dry runs are a tool, not a religion.

---

Next: what exactly you're granting, in [Chapter 5 — Permissions](05-permissions.md).
