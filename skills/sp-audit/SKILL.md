---
name: sp-audit
license: MIT
description: >-
  Post-mortem on what the user has already published - which posts actually
  worked, why, and what to stop doing. Use when the user pastes their LinkedIn
  analytics or past posts and asks "what's working", "why did this flop", "read
  my analytics", "audit my content", or wants to know what to double down on.
---

# sp-audit

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

The only honest source of what works for an account is that account. Every
rule in every LinkedIn guide, including the ones in this pack, is a prior. The
user's own last 30 posts are the evidence.

## Input

Ask for whichever the user has:

- The post analytics export (LinkedIn: Analytics -> Content -> Export). CSV.
- Or the `/sp-stats` JSON output: `data/posts.json`, `data/reactors.json`,
  `data/commenters.json`, `data/meta.json`. See "From sp-stats JSON" below.
- Or a screenshot per post with impressions, reactions, comments, reposts.
- Or just the posts and their reaction counts, which is enough for a first
  pass.

Also read `<profile>/log.md` if it exists, since it records which
hook formula each post used.

## What to actually measure

Raw impressions are the least useful number on the page, because they are
mostly a function of how many people already follow the user, and because
impressions count displays, including repeats, not people. Members
reached is the audience proxy. Never equate impressions with reach.
Compute these instead, and show the working:

| metric | how | what it tells you |
| --- | --- | --- |
| **Engagement rate** | (reactions + comments + reposts) / impressions | whether the post earned its reach |
| **Comment ratio** | comments / reactions | whether it started something or just got a nod |
| **Reach multiple** | impressions / follower count | whether it travelled past the existing audience |
| **Save/send rate** | if available | the strongest single predictor of future reach |

Rank by engagement rate and reach multiple, not impressions, and rank by
each separately. A post can top one and bottom the other. A post with 900
impressions and 40 comments beat the one with 12,000 impressions and 6.
Use medians, not means, and exclude viral outliers when you set a
baseline. AuthoredUp excludes posts above 10% engagement when
benchmarking, for the same reason. Filter out posts under 100
impressions before ranking: an engagement rate on a tiny-impression post
is noise.

## From sp-stats JSON

`posts.json` carries one object per post: `id`, `ts` (epoch ms), `text`,
`contentType`, `isReshare`, `likes`, `comments`, `reposts`, `impressions`
(null when LinkedIn does not report it), `reactionTypes`, `threadUrn`,
`url`, `actorName`. `reactors.json` and `commenters.json` carry who reacted
and commented (`postId`, `name`, `publicId`, `occupation`, plus `type` for
reactions and `ts`/`text` for comments). `meta.json` carries `scrapedAt`
and the profile (`name`, `urn`, `followers`, `headline`).

Rank originals only (`isReshare` false). Reposts carry the original
author's counts, so ranking them with your own posts is a viral-outlier
trap. Compute the same four metrics as above. Use `followers` from
`meta.json` for the reach multiple. `reactors.json` and `commenters.json`
also answer who your real audience is: the people who show up across
many posts, and whether the user replies to them (compare the user's own
comments in `commenters.json` against the posts other people commented on).

Data-quality guard, before you rank anything: a 2024 or later original
with 0 likes AND 0 comments AND null impressions is almost certainly a
counts-join miss from the scrape, not a genuinely dead post. If more than
5 posts trip it, say so loudly, leave them out of the bottom 5, and tell
the user to re-fetch their post-level counts before trusting the audit.

## Then find the pattern

With the top 5 and bottom 5 side by side, look for what actually separates
them, and be willing to conclude something the user will not like:

- Hook formula. Which numbers from `hooks.json` are in the top 5?
- Format. Text, document, image, video.
- Length.
- Theme.
- Day and time - check this **last**, and only if the other four show nothing.
  It is almost never the cause, and it is where people want it to be.
- First-hour comments. Posts the user replied to inside an hour versus not.

State the finding as a claim with the evidence attached, and say how confident
it is. With 30 posts you can see a pattern; with 6 you cannot, and you should
say that instead of inventing one.

## The audit framework

Collect the last 20 to 50 posts with impressions, reactions, comments,
reposts, saves, profile views, followers gained, format, length, hook
style, and topic. Rank by engagement rate and by reach multiple
separately. Tag every post by topic, format, and hook. Then decide:

- **Double down:** top quartile on both engagement rate and reach
  multiple.
- **Fix:** high reach, low engagement. That is a hook or body mismatch:
  the post travelled but did not earn a response.
- **Retire:** low on both, twice running.

Re-run monthly, not after one viral post. One viral post is an outlier,
not a strategy.

Traps to check before you decide anything:

- Impressions versus reach, above. Rank on members reached where you
  have it, never on impressions alone.
- Repost attribution. A repost's engagement accrues to the repost, not
  to the original, in most dashboards. Rank originals only.
- Cross-format comparisons without within-author controls measure who
  uses the format, not the format. Compare a format against your own
  posts in other formats, same author, same period.
- Engagement rate on a post under 100 impressions is noise. Filter it
  out before ranking.

Decisions an audit drives: which 2 to 3 topics to keep, which format is
the weekly anchor, which hook style your audience rewards, what to
repurpose (top-decile posts become carousels or articles), and what to
stop.

## Output

```
AUDIT  ·  31 posts  ·  Jun 12 - Sep 5

TOP 5 BY ENGAGEMENT RATE
  8.1%  #3  Mistake      "$18,000 is what no contract cost me"      1,940 imp
  6.4%  #20 Walk-Away    "I fired my highest-paying client"         2,210 imp
  ...

BOTTOM 5
  0.4%  #5  List         "7 tools every founder needs"             11,400 imp
  ...

WHAT THE DATA SAYS
1. Posts where you were the one who looked bad: mean 6.2% vs 1.1% for
   everything else. n=6. This is your strongest signal and it is not close.
2. Tool listicles get impressions and nothing else. High reach, no comments,
   no leads. Three of your bottom five.
3. Day of week shows nothing. Your Tuesday mean and your Friday mean are
   inside the noise. Stop optimising it.

STOP: listicles about tools.
DO MORE: the ones with a cost you paid, and a number.
```

Then hand the conclusions to `/sp-plan` so next week's plan is built on the
user's own evidence rather than on defaults.
