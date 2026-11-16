---
name: sp-plan
license: MIT
description: >-
  Build the week on LinkedIn - what to post, when to post it, and who to engage
  with. Use when the user says "plan my week", "what should I post", "content
  calendar", "I have nothing to post about", or wants a posting schedule and an
  engagement list.
---

# sp-plan

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

The control room. Everything else in this pack executes; this decides what
gets executed. Run it once a week, on the same day.

## Input

If `<profile>/voice.md` and `log.md` exist, read them - the plan
should not repeat a theme from the last fortnight. If they do not exist, ask
for four things and write them down:

1. What the user sells, and to whom.
2. The two or three themes they want to be known for. Topic
   consistency drives LLM-retrieval relevance after the March 2026
   feed rebuild, so keep the list to 2-3 topics, not four or five.
3. What actually happened this week - a client call, a number, a mistake, a
   thing they built, an argument they had. This is where posts come from.
4. Ten to twenty people or companies worth being visible to.

## What to post

Post 2-5 times a week (Buffer, 2M+ posts, 94,000+ accounts:
2-5/week measured +1,182 impressions per post and +0.23pp
engagement vs 1/week). 1/week leaves growth on the table. 4 posts a
week is a good default for a job seeker or builder: consistency is a
floor, not a target, and quality is the constraint, since per-post
likes fall as pace rises even while the weekly total rises. Do not
pad a fifth post that has nothing specific to say.

Mix across the week, never two of the same type back to back, and
stay inside the same 2-3 topics all week:

| type | share | job |
| --- | --- | --- |
| **Proof** | 1 per week | something that happened, with a number |
| **Opinion** | 1 per week | a position that could lose you followers |
| **Teach** | 1 per week | one thing the reader can do today |
| **Story** | 1 per fortnight | a scene with dialogue and a cost |
| **Offer** | 1 per fortnight | what you sell, said plainly, no apology |

For each slot give: the theme, the specific angle drawn from what actually
happened this week, and the hook formula number from `sp-post/hooks.json` that
fits it. Not a topic - an angle. "AI" is not a plan. "The proposal we lost
because our AI draft had an em dash in it" is a post.

## When to post

There is no magic hour and no magic day. Three million-post datasets
disagree (Sprout, Hootsuite, Buffer give three different answers),
Flypost found the day of the week makes no change, and one smaller
dataset found Monday and Sunday best and Thursday worst, which is
noise, not signal. Post when the user's audience is awake, at a
consistent slot they can hold every week, and anchor the times to
their audience's timezone, not the user's, if those differ. Weekends
are for personal-story posts or nothing.

State this plainly: **the day and hour matter far less than whether the
first line is good.** If the user is optimising posting times before their
hooks work, they are polishing the wrong thing, and you should say so.

## A realistic weekly plan (synthesis, not a measured outcome)

The plan below is a synthesis of the cadence, mix, and engagement
rules in this skill, not a measured outcome. Label it as such when
you show it. It assumes 2-3 hours a week: 2-5 posts, 20 minutes a
day engaging with 3-5 target accounts, and 1 poll per month
maximum, never weekly.

## Who to engage with

Build a list of 10, split three ways:

- **5 reach** - people with an audience the user wants, whose posts they can
  genuinely add to. Comment before they have 20 comments or nobody sees it.
- **3 peers** - same level, same field. This is the group that reciprocates.
- **2 buyers** - people who could actually buy. Comment on their posts for
  weeks before any DM, and never pitch in a comment.

20 minutes a day, before posting, not after. Comments on other people's posts
are what makes the user's own post land.

## Output

The times below are consistent slots the user can hold, not best
hours: no dataset supports a best hour, so pick a slot and keep it.

```
WEEK OF SEP 8

MON  engage only  (20 min, list below)
TUE  8:15am  PROOF    #17 Time Anchor   - the 5hr -> 20min proposal rebuild
WED  engage only
THU  8:00am  OPINION  #1  Contrarian    - why we killed the discovery call
FRI  8:30am  TEACH    #21 Direct Value  - the 4-line reopen email, given away
SAT  -
SUN  4:00pm  STORY    #9  Cold Open     - the "going with someone cheaper" email

ENGAGE  (5 reach / 3 peers / 2 buyers)
  ...

Say "write Tuesday" and I will draft it.
```

Write the plan to `<profile>/plan.md` so the other skills can read it.
This is a plan. Run any part of it through the host agent's tools when
the user says go.
