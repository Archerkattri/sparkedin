---
name: sp-publish
license: MIT
description: >-
  Publish a LinkedIn post through the official Share API and schedule posts
  through the host agent's cron. Use whenever the user wants a post published
  to LinkedIn, scheduled for a time, or posted with an image, video, document,
  article, or poll. Covers text, image, video, document, article, and poll
  posts via POST https://api.linkedin.com/rest/posts. The Share API is the
  sanctioned publishing path; browser posting stays as a fallback.
---

# sp-publish

Profile directory: `<profile>` holds voice.md, log.md, plan.md, and
scheduled.md. Muse uses `~/workspace/linkedin/`, Claude Code uses
`~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Publishes a LinkedIn post through the official Share API, or schedules it
for later through the host agent's cron. This is the sanctioned lane for
getting words onto LinkedIn. It does not drive the logged-in browser
session to post, and it does not pretend a browser fallback is the same
thing.

## The honest constraint, stated up front

LinkedIn's User Agreement section 8.2 (effective 3 November 2025)
prohibits browser-session automation: extensions and agents that click,
post, connect, message, comment, or scrape while logged in. The Share API
is the sanctioned path for publishing. Browser posting stays available as
a fallback, with this constraint stated every time it is used: it is the
user posting in their own browser, not automation, and it carries the
restriction risk the agreement describes. This skill never hides that
difference.

## Setup, once

1. Create an app at the LinkedIn Developer portal. Request the
   **Share on LinkedIn** product, scope `w_member_social`. Add
   `openid`, `profile`, and `email` if the app also needs to confirm who
   is signed in.
2. Complete the OAuth flow as the user. Store the access token where the
   host agent keeps credentials. **Tokens last 60 days.** Put a renewal
   reminder at day 50, and renew before it expires. Programmatic refresh
   tokens (up to 365 days) exist only for approved partner apps, so plan
   on a manual re-authorization roughly every two months.
3. Send every request with the `LinkedIn-Version` header. LinkedIn
   versions the API monthly and supports each version for about a year.
   Pin the version you tested against and check it when a call fails.

## Publish now

1. Take the approved draft. It must already exist: written by `/sp-post`,
   `/sp-carousel`, or `/sp-poll`, and run through `/sp-human`. This skill
   never writes the post. It publishes it.
2. Pick the post type and build the call to
   `POST https://api.linkedin.com/rest/posts`:

   - **Text.** The post text, plus the visibility setting the user chose.
   - **Image.** Single or multi-image. Media upload is multi-step:
     register the upload, upload the binary, then reference the returned
     asset in the post call. Do not skip the register step.
   - **Video.** Same multi-step upload as images. Keep the file inside
     LinkedIn's published size and length limits, and check the upload
     status before posting.
   - **Document.** PDF or slides, same multi-step upload. The document
     title is what shows in the feed, so write it like a headline.
   - **Article.** Share a link with a title and description. Put the link
     in the post, not hidden in a comment, when the point of the post is
     the article itself. For a plain text post, the link still goes in the
     first comment, per `/sp-post`.
   - **Poll.** The API supports polls in vendor guides, but LinkedIn's
     own docs do not confirm a self-serve member poll endpoint. Attempt
     it through the API first. If the API rejects it, say so plainly and
     post the poll in the browser instead, with the user clicking post.
3. Read the response. A 201 with a post URN is published. Anything else
   is not published. Report the error exactly, do not retry blindly, and
   do not claim the post went out until the response says so.
4. On success, append the post to `<profile>/log.md` with the date, the
   post URN, the first line, and the type, so `/sp-audit` and
   `/sp-analytics` have a history to work from.
5. If the post has a link that belongs in the first comment, add it as a
   comment on the new post through the same API, then note it in the log.

## Schedule for later

LinkedIn has no native scheduling for personal posts. Scheduling lives in
the host agent, not in this skill:

1. The user approves the draft and names the date and time.
2. Write the approved post, its type, its media, and its publish time to
   `<profile>/scheduled.md`. One entry per scheduled post, with the full
   text, not a pointer to a draft that might change.
3. Set a host agent cron for that time. The cron's job is one line: run
   `/sp-publish` on the named entry in `scheduled.md`.
4. At publish time, run the same publish-now flow. On success, move the
   entry from `scheduled.md` to `log.md`. On failure, leave it in
   `scheduled.md`, mark it failed with the error, and tell the user. Never
   silently drop a scheduled post.
5. If the access token expires before the scheduled time, the publish
   fails. Check token expiry when the post is scheduled, and warn the user
   if the token runs out first.

## What this skill cannot do

- Read the user's own posts back through the API. The
  `r_member_social` permission is closed to new requests. Verify a
  published post by opening the post URL the API returned.
- Post as a Company Page without the Community Management API and Page
  admin rights. That is a vetted product, not self-serve.
- Connect, message, comment, endorse, or apply for jobs. There is no
  open API for any of those. Do not build a workaround.
- Schedule inside LinkedIn. There is no native scheduling to call.

## Rules that make the difference

- **Approved drafts only.** Nothing publishes without the user saying go
  on the exact text. A scheduled post is an approved post with a time on
  it, not a draft with a deadline.
- **One post, one call.** Never batch multiple posts into one request.
  Never publish a queue in a burst.
- **Report the response.** Published means a 201 and a URN. Everything
  else is a failure with an error message, reported as one.
- **Never fabricate.** The post text is the user's approved words. This
  skill adds no metrics, no claims, no links the user did not approve.
