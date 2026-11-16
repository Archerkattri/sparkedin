---
name: sp-analytics
license: MIT
description: >-
  Keep a manual analytics journal for a LinkedIn profile and turn pasted
  numbers into decisions. Use whenever the user pastes LinkedIn analytics,
  asks how a post did, wants a weekly numbers check, or asks whether AI
  assisted posts or human posts perform better for them. Tracks search
  appearances, profile views, followers, and per-post numbers over time in
  <profile>/analytics.md. There is no API for personal-profile analytics, so
  the user pastes the numbers and this skill does the analysis.
---

# sp-analytics

Profile directory: `<profile>` holds voice.md, log.md, plan.md, and
analytics.md. Muse uses `~/workspace/linkedin/`, Claude Code uses
`~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Turns numbers the user pastes from LinkedIn into a journal, a trend, and a
decision. There is no API for personal-profile analytics. The
`r_member_social` permission is closed to new requests, and the statistics
endpoints that exist cover a Company Page's posts only. Any tool that
claims to pull a personal profile's analytics automatically is either
reading the logged-in browser session or inventing the numbers. This skill
does neither. The user pastes the numbers, the skill does the math.

## What to collect

Ask the user to paste, once a week, from Profile, Analytics, and each
post's View analytics screen. The journal lives in
`<profile>/analytics.md`, one dated entry per week. Fields:

**Profile, weekly:**

- Search appearances, with the week they cover. LinkedIn refreshes these
  weekly, on Wednesdays.
- Profile views, last 90 days. Free accounts see the 3 most recent
  viewers by name. Premium sees the full list.
- Followers, total and gained this week.

**Per post:**

- Impressions.
- In-network vs out-of-network split.
- Profile viewers gained from that post.
- Followers gained from that post.
- Reactions, comments, reposts.
- Link clicks, where LinkedIn shows them.

If a field is not shown for a post, leave it blank. A blank is honest.
A zero is a claim. Never write zero where LinkedIn showed nothing.

## The weekly entry

Each week, append one entry to `<profile>/analytics.md`:

```
## 2026-11-16
Search appearances: 42 (week of Nov 9)
Profile views: 18
Followers: 1,247 (+2)
Posts this week:
- "Your robot can see the object..." impressions 1,204, in-network 61%,
  out-of-network 39%, profile viewers +9, followers +3, reactions 47,
  comments 8, reposts 2
```

Then write three lines under it: what went up, what went down, and what
changed since last week. No more. The journal is a record, not a report.

## The analysis

**1. The funnel.** Search appearances vs profile views vs recruiter
messages is a funnel, and each step has its own fix. Many appearances
and few views means the headline and photo are not earning the click.
Many views and no messages means the profile is not closing. Say which
step is leaking before suggesting any fix, and hand the fix to
`/sp-profile`.

**2. Reach multiple.** Impressions divided by followers. A post with a
reach multiple above 1 reached beyond the user's own followers. Rank
posts by reach multiple and engagement rate, not by raw impressions. A
post with 5,000 impressions to 1,200 followers did better than a post
with 6,000 impressions to 5,000 followers. This is the same ranking
`/sp-audit` uses. Use both skills together: this one keeps the numbers,
that one ranks the history.

**3. AI vs human, within person.** The only honest comparison is the user
against themselves. Tag each post in the journal as human-written,
AI-assisted, or AI-written, using the user's own account of how it was
made. Then compare the two groups on reactions, comments, and reach
multiple, holding format and length roughly steady. Independent studies
found mostly-AI posts earning about 24 percent fewer reactions than the
same person's human posts, and completely-AI posts about 32 percent
fewer. Those are other people's numbers. This journal produces the user's
own number, which is the one that matters.

**4. The monthly summary.** Once a month, read the four weekly entries
and write one paragraph: the trend, the best post and why, the worst post
and why, and one thing to try next month. File it at the top of
`analytics.md` so the newest summary is the first thing read.

## How this fits with sp-stats

`/sp-stats` pulls the user's own posts and engagement into local JSON
through the browser session, and builds a dashboard. It is experimental,
heavy, and not to be run fresh off a restriction. `/sp-analytics` is the
lightweight, manual companion: pasted numbers, a weekly habit, no browser
session reading at all. Use this skill every week. Use `/sp-stats` when a
full pull is worth the cost.

## Rules that make the difference

- **Never scrape analytics.** No reading the analytics pages through the
  browser session, no copying numbers the user did not paste. The user is
  the source. If they did not paste it, it is not in the journal.
- **Never invent a number.** A missing field stays blank. A week with no
  pasted numbers stays empty, with a note that it was skipped.
- **Compare within person only.** Never compare the user's numbers to a
  benchmark, an average, or another creator. The journal measures the user
  against their own past weeks.
- **Analytics are private.** These numbers belong to the owner only.
  Never post them, never quote them in a post, never share them without
  the user saying so.
- **Say what the number cannot prove.** A spike in impressions after a
  poll does not prove polls always work. A quiet week does not prove the
  audience left. Report the number, name the most likely cause, and mark
  it as a guess when it is one.
