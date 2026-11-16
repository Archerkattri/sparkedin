---
name: sp-repurpose
license: MIT
description: >-
  Turn one long asset - a YouTube video, podcast, newsletter, blog post,
  transcript or client call - into a week of LinkedIn posts. Use when the user
  says "repurpose this", "turn this into posts", "I have a video/newsletter/
  transcript", or pastes a long piece of content and wants it on LinkedIn.
---

# sp-repurpose

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

One good long asset contains a pillar and its derivatives: 5-7
standalone text posts, plus a carousel, a poll question, a personal
story, and a contrarian take. Most people extract one and throw the
rest away.

## Input

A transcript, an article, a newsletter, a script, a call summary. If the user
gives a YouTube URL and there is a transcript tool available in the session,
use it; otherwise ask them to paste the text. Read the whole thing before
extracting anything.

## Extract, do not summarise

A summary of a video is not a post. Nobody wants the summary. Go through the
asset and pull out the things that stand alone:

| pull | what it is |
| --- | --- |
| **Claims** | every sentence that would start an argument |
| **Numbers** | every figure, cost, duration, percentage |
| **Stories** | every moment with a person, a scene and a cost |
| **Mechanisms** | every "the way this works is..." explanation |
| **Mistakes** | every admission of something that went wrong |
| **Lines** | every sentence that is already quotable as-is |

List what you found, with counts, before writing anything. If the asset yields
fewer than four items, it is thin, and four posts squeezed out of it will be
thin too. Say that.

## Then build the week

Use the AuthoredUp "Create Once, Publish Five" framework. One pillar
(a 2,000-word post, blog, or video) becomes 5-7 standalone insights
as text posts, 1 step-by-step carousel, 1 central question as a poll,
1 personal story, and 1 contrarian take. Each derivative uses a
different format, angle, and hook, and each must pass the standalone
test below.

Each extract becomes one post, and each post has to stand completely on its
own - the reader has not seen the video and never will. Never write "as I
mentioned in my latest video". The post is the thing.

**Standalone test:** each derivative must make sense with no knowledge
of the anchor. If it needs the anchor to make sense, it is a teaser,
not a post. Rewrite it until it stands alone, or drop it.

**Spacing:** space derivatives 3+ days apart. Do not publish them on
consecutive days: five posts from one source in one week reads as a
content mill, even when each one stands alone. Spread one pillar
across two weeks or more.

**Article-post loop:** expand a high-engagement post into an article,
then extract 5-10 posts from the article. A post that already earned
engagement is a proven anchor, so mine it before starting a new one.

Assign a hook formula from `sp-post/hooks.json` to each, and vary them: five
posts from one source with the same hook shape reads as a content mill.

Order them across the weeks so the strongest claim goes first, the story goes
midweek, and the mechanism post goes last, when people who liked the earlier
ones are watching for it.

## Output

```
SOURCE: "Why we killed discovery calls" (18 min, 3,400 words)

FOUND  4 claims, 6 numbers, 2 stories, 3 mechanisms, 1 mistake, 5 quotable lines

WEEK 1-2 (derivatives spaced 3+ days apart)
TUE  #1  Contrarian    Discovery calls are a tax you pay for a bad website
FRI  #17 Time Anchor   We got 6 hours a week back by deleting one calendar link
TUE  #9  Cold Open     "Can we just hop on a quick call?"
FRI  #21 Direct Value  The 4-question form that replaced the call. Steal it.

Say "write Tuesday" and I will draft it.
```

Then draft on request, one at a time, each through `/sp-post` and `/sp-human`.
Do not dump four finished posts at once - they will all sound the same, and
the user will edit none of them.
