---
name: sp-stats
license: MIT
description: >-
  Pull your own LinkedIn posts and engagement (likes, comments, reposts,
  impressions, who reacted and commented) into local JSON from your own
  logged-in Chrome session, then build a dashboard from it. Use for "analyse
  my LinkedIn", "refresh my LinkedIn stats" or a monthly update.
  Experimental: LinkedIn internals change without notice.
---

# sp-stats

> **EXPERIMENTAL.** This skill replays LinkedIn's own internal API from your
> own logged-in browser session. LinkedIn changes those internals without
> notice, so any step below can stop working. When it does, the fix is to
> re-discover the endpoint and the field names from the live page, not to
> force the old ones. The Voyager method was last verified 22 Sep 2026; the
> Activity-page fallback in section 0a was verified 16 Nov 2026.

Own account only. Your own posts, your own engagement, read from your own
Chrome session. Nothing here touches anyone else's data.

## 0. Confirm before the full scrape

A full history is about 2,600 requests and about 2 hours. Say that to the
user first, with the current post count if you know it, and get a yes before
the loop starts. This is a time and cost gate, not a cap: once the user says
go, the scrape runs to completion.

Fresh off a restriction: if the account was recently restricted,
checkpointed, or rate-limited for volume, do not start a full scrape. Wait
until the account has been quiet for a few days, or run a small sample
first (one page of posts, counts only) and check it lands clean. A full
history is 2,600 requests, which is exactly the kind of volume that gets an
account restricted again.

## 0a. Browser-task fallback: read the Activity page directly

The Voyager method above needs in-page JavaScript and headers the host
browser tool may not provide. Verified 16 Nov 2026: in a browser task,
DevTools shortcuts did not open DevTools, right-click produced no menu, and
navigating directly to a Voyager URL returned "CSRF check failed" because
plain navigation cannot send the csrf-token header. When the Voyager fetch
is unavailable, do this instead:

1. Open `https://www.linkedin.com/in/me/recent-activity/all/` (Posts tab),
   scroll to the end until the footer is visible and no further entries
   load. Check the Videos and Images tabs the same way.
2. Record the counts LinkedIn itself displays per entry (likes, comments,
   reposts, impressions where shown). A button showing no count is 0.
3. Reposts carry the ORIGINAL author's counts. Record them separately and
   never rank them against the user's own posts.
4. Verify in a second session if one is available. Likes, comments and
   reposts should match exactly; impressions drift slightly because they
   are live.
5. Save the same posts.json shape (with isReshare flagged) and note the
   method as "activity-page" in meta.json. Do not claim Voyager-level
   completeness: per-post reactors and commenters are not available this
   way, so sections 5 and 6 do not apply to a fallback sample.

## 1. Setup

1. Use the user's own Chrome session through the host agent's browser tools.
   Navigate to `https://www.linkedin.com/in/me/recent-activity/all/` and wait
   4s.
2. Keep the LinkedIn tab as the visible, front tab. Since LinkedIn's
   September 2026 front-end change, a background LinkedIn tab freezes and
   every call times out.

## 2. Discover the posts endpoint

The queryId hash changes over time. Never hardcode it. Scroll the page 2-3
times, then in-page:

`performance.getEntriesByType('resource').map(e=>e.name).filter(u=>u.includes('voyagerFeedDashProfileUpdates')).pop()`

Keep that full URL as the template. Note: the browser tool may block
returning query strings or cookies from in-page JavaScript. Parse and use
URLs inside the page, and return only derived scalars.

Grab the template early. The performance resource buffer overflows silently,
so the URL is gone if you wait.

## 3. Paginate

Plain `start` is ignored. The server returns page 1 forever. Thread
`metadata.paginationToken` from each response into the next request: insert
`paginationToken:<encodeURIComponent(token)>,` right after `variables=(`.

Headers for all voyager fetches:

- `csrf-token`: the JSESSIONID cookie value, quotes stripped
- `accept: application/vnd.linkedin.normalized+json+2.1`
- `x-restli-protocol-version: 2.0.0`

Loop until the token is missing or unchanged (about 116 pages for a full
history). Run as a background async loop writing to a status object on the
page, for example `window.__spstats`. The browser tool times out at 45s, so
never await a long loop inside one tool call. Poll the status object instead.

## 4. Extract per page

From `included` on each page:

- `feed.Update`: activity id from entityUrn, `commentary.text.text`,
  content keys, `actor.name.text`
- `social.SocialDetail`: entityUrn activity id, the
  `*totalSocialActivityCounts` ref, `threadUrn` (needed for reactions;
  sometimes a ugcPost urn)
- `feed.SocialActivityCounts`: numLikes, numComments, numShares,
  `numImpressions` (only the recent 400 or so posts), reactionTypeCounts
- Timestamp: `Number(BigInt(activityId) >> 22n)` is epoch ms (works back to
  2013)
- Reshare detection: `isReshare = actor.name.text !== '<your display name>'`.
  Read the user's display name from the profile card on the page first.
  `resharedUpdate` is always absent in this format, so do not trust it.
  Reposted items carry the ORIGINAL author's social counts, which is a
  viral-outlier trap.

### The counts join (the ugcPost trap). Read this before trusting any number.

A post's SocialActivityCounts is sometimes keyed on `urn:li:ugcPost:<n>` or
`urn:li:share:<n>`, not `urn:li:activity:<n>`. Videos always are. A large
fraction of images and text posts are too. If you only match the
activity-keyed counts, you will silently record 0 likes, 0 comments and null
impressions for 30-40% of posts. A real 867-like post came back as 0 that way.

The reliable source of post-level counts is
`/voyager/api/feed/updates/urn:li:activity:<id>`. In its `included`, take the
`SocialActivityCounts` whose entityUrn matches
`socialActivityCounts:urn:li:(ugcPost|activity|share)` and is not a
`:comment:` one (pick the max-count one if several). It carries numLikes,
numComments, numShares and numImpressions authoritatively.

Either fetch counts this way for every post, or scrape fast through
profileUpdates and then re-fetch counts per post to correct. Sanity check:
any 2024 or later post with 0 likes AND 0 comments AND null impressions is
almost certainly a join miss. For videos, `numImpressions` exists on the
ugcPost counts. LinkedIn also tracks video views separately, which this field
is not.

## 5. Reactions (who liked)

Classic REST endpoint, no queryId needed:

`/voyager/api/feed/reactions?count=50&q=reactionType&start=N&threadUrn=<encoded threadUrn>`

`included` has `feed.social.Reaction` (reactionType, actorUrn) plus
`identity.shared.MiniProfile` (firstName, lastName, occupation,
publicIdentifier). Join on `Reaction.actorUrn === MiniProfile.entityUrn`.

Cap at 20 pages (1,000 reactors) per post. LinkedIn returns 1st-degree
connections first, and the counts are already exact from
SocialActivityCounts.

## 6. Comments

`/voyager/api/feed/comments?count=50&q=comments&sortOrder=CHRON&start=N&updateId=activity:<id>`

`feed.Comment` (commenterProfileId, commentV2.text, createdTime) joined to
MiniProfile by the trailing id of entityUrn.

## 7. Engagement harvest

Only for posts that are not reshares and have likes or comments above 0,
newest first. 300-500ms jittered sleeps, back off 8s on 429, retry 3 times.
About 2,600 requests is about 2h in a single loop. Run 2 concurrent workers
over disjoint slices (newest half plus oldest half) for about 1 request per
second combined. Do not go wider: that is the rate-limit risk. Give each
worker its own status object and a stop flag.

## 8. Getting data out

Getting data out of the page without blowing the agent's context: click a
neutral page spot to focus the document (clipboard needs focus), then
`navigator.clipboard.writeText(JSON.stringify(...))` in-page, then read the
clipboard from the shell (`pbpaste` on macOS, `xclip -o` or `wl-paste` on
Linux) into the data files, and validate them as JSON. 1.6MB works fine.

Dedupe reactors on (postId, key) and comments on (postId, key, ts) at save
time.

## 9. Output files

Write into `<profile>/linkedin-stats/data/` (Muse:
`~/workspace/linkedin/linkedin-stats/data/`, other hosts: a folder you
choose):

- `posts.json`: one object per post: `id`, `ts` (epoch ms), `text`,
  `contentType`, `isReshare`, `likes`, `comments`, `reposts`, `impressions`
  (null when LinkedIn does not report it), `reactionTypes`, `threadUrn`,
  `url`, `actorName`
- `reactors.json`: `postId`, `type`, `key`, `name`, `publicId`, `occupation`
- `commenters.json`: `postId`, `key`, `name`, `publicId`, `occupation`,
  `ts`, `text`
- `meta.json`: `scrapedAt`, `profile` (`name`, `urn`, `followers`,
  `headline`)

## 10. Dashboard

Do not write a static dashboard.html into the repo. On Muse, render the
dashboard as an artifact from the JSON: summary totals, top posts by likes,
comments and engagement rate, monthly trend, day-of-week and time-of-day
heatmap, top engagers, and the data-quality warning below. On other hosts,
build a self-contained dashboard.html in the same data folder from the same
numbers.

The original linkedin-stats skill shipped Node scripts (analyze.mjs,
build-dashboard.mjs). They were not ported. The agent computes the analysis
steps directly from the JSON instead. Port them only if the user asks.

## 11. Data-quality guard

Before any analysis, flag every original post from 2024 or later with 0
likes AND 0 comments AND null impressions. That is almost always a
counts-join miss, not a genuinely dead post. If more than 5 posts trip it,
say so loudly and re-fetch their post-level counts before ranking anything.
Bad counts silently understate engagement.

## 12. Hand it to the audit

Feed the JSON to `/sp-audit`. That skill reads this exact shape and ranks by
engagement rate and reach multiple, not impressions.
