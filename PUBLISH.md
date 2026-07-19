# Publication Plan — AWAITING OWNER GO-AHEAD

**Status: NOTHING has been published externally. This repo is local-only (no remote, no push).**

Publication puts the taxonomy out under the owner's name and starts the public clock on the standard. It requires the owner's explicit OK before any step below is taken. Until then: no remote repo, no posts, no submissions, no sharing of these files.

## Why publish at all

Per the portfolio plan (phase 6): the open taxonomy is the ACORD-forms move — days of work, permanent option value. A standard only compounds if others can find and adopt it, and priority/authorship only accrues if publication is dated and attributable. Cost of all options below: $0.

## Options, ranked

### 1. Public GitHub repo + GitHub Pages — $0, do first

- Push this repo to a public GitHub repository (suggested: `lossbook/robot-incident-taxonomy` or under the owner's account; TO VERIFY name availability).
- Enable GitHub Pages on the repo so the taxonomy has a citable URL; the markdown renders as-is, no build needed.
- Add repo topics (`robotics`, `insurance`, `safety`, `taxonomy`, `open-standard`) for discoverability.
- Tag the initial release `v0.1` so adopters can pin a version.
- Effort: under an hour. Reversible only in the weak sense (public is public).

### 2. Community submission — after option 1, staged

Post/submit only after the GitHub URL exists, so all roads lead to the canonical copy. Candidate venues (TO VERIFY current norms and whether self-promotion rules allow it in each):

- Robotics communities: r/robotics, Hacker News (Show HN), ROS Discourse.
- Robotics safety circles: A3 (Association for Advancing Automation) contacts, RIA/ISO 10218- and ISO 3691-4-adjacent working-group people — via personal outreach, not cold submission.
- Insurance side: the robotics-program carriers and MGAs named in the research (Axis robotics program, AIUC) and any broker contacts — framed as "free standard, want your field feedback for v0.2".
- Trade press that covered the missing-loss-data gap (The Robot Report, PYMNTS coverage of physical-AI insurance) — a short pitch note, only if the owner wants visibility this early.

### 3. Lightweight standalone page — optional, later

A one-page site (GitHub Pages custom domain, ~$10/yr for a domain — the only non-zero cost in this plan, and optional). Skip until adoption interest exists.

## Pre-publication checklist (owner + one pass)

- [ ] Owner reads both taxonomy documents end-to-end and approves content going out under their name.
- [ ] Resolve or consciously ship the `TO VERIFY` markers (they can ship in a v0.1 draft — drafts are allowed open questions — but the owner should know they're there).
- [ ] Decide attribution identity: personal name, "Lossbook", or both (affects LICENSE.md attribution line and README).
- [ ] Replace the placeholder `$id` URL in the JSON Schema (`lossbook.example`) with the real published URL.
- [ ] Owner explicitly says "publish" — then, and only then, create the remote and push.

## What publication does NOT include

- No SaaS, no signup page, no data collection, no waitlist. The standard is the only thing shipping (see `BACKLOG.md` guard).
