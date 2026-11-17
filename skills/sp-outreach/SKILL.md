---
name: sp-outreach
license: MIT
description: >-
  Run LinkedIn outreach for one person or a whole campaign. For one person:
  the 200-character invite note, the first message, and the two follow-ups.
  For a campaign: pick the path first (comment-then-DM, recruiter with job
  ID, warm-up, alumni, founder, apply-then-message), then write the
  connection note, the DM, the two follow-ups and the thank-you after they
  accept, and track every target in outreach.md. Use when the user says
  "write a connection request", "DM this person", "outreach message", "how
  do I follow up", or wants a referral, a job, an introduction, or is
  reaching out to several people at one company.
---

# sp-outreach

Profile directory: `<profile>` holds voice.md, log.md, plan.md and outreach.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

One person is a message. Several people is a campaign. This skill handles
both. It picks the path before it writes a word, because the path decides
what the message can say. The invite note is 200 characters. The first DM
decides whether there is a second one. Neither is a pitch.

## What to expect (benchmarks, with denominators)

Cold outreach converts at roughly 1 in 4 accepts and 1 in 10 replies.
These are automation-user samples, not the general population, so a careful
human job seeker with a narrow, specific list should beat the average and
a bought list should trail it.

- Expandi, 13.2M requests, May 2025 to Apr 2026: 28.5% acceptance,
  10.4% reply to messages.
- HeyReach, 96,051 campaigns, 12 months to Sep 2026: 20.75% median
  acceptance, 22.22% median reply per conversation started. Note the
  denominator differs from Expandi: reply per conversation, not per
  message sent.
- InMail, LinkedIn's own analysis, tens of millions, May 2023 to Apr
  2024: 6.4% average reply, 18 to 25% for recruiting.

Do not quote a single acceptance or reply rate without its denominator
and sample. Never present these as what a specific person will get.

## Automation is prohibited, not merely discouraged

LinkedIn User Agreement section 8.2 (effective 3 Nov 2025) bans bots,
scripts, and extensions that automate invites, messages, or scraping.
Enforcement is graduated: warning, then restriction, then permanent ban.
Do not teach automation tools as safe, and do not suggest a tool that
"mimics humans" as a workaround. Every send in this skill goes through
the host agent's tools when the user says go, one message at a time.

LinkedIn publishes no weekly invite cap. Operator consensus of about
100 requests per week is operator consensus only, never a LinkedIn rule,
so never cite it as one. The job-seeker default in this skill is 5 to 10
specific requests per day. That is a synthesis, not a LinkedIn rule.
A withdrawn invite cannot be resent for up to 3 weeks.

## 0. Inputs

Ask for, in one batched question:

1. **Who** - name, role, company. Or a company with no person yet.
2. **The opening** - a hiring post (paste it), a job ID or link, a specific
   person, or "I just want to get into <Company>".
3. **The hook** - the real reason to reach out now. A post they wrote, a
   thing their company shipped, a mutual connection, a talk they gave, a
   shared school. Not "they fit my ICP".
4. **Best proof** - one project, internship or achievement, ideally with a
   link.
5. **What the user wants** - a referral, a conversation, a job, a sale. Be
   honest internally, even if the message does not lead with it.

If there is no specific reason to message this person today, say so. A
message with no reason is what everyone else sends, and it is why most
cold outreach sits near the benchmarks above instead of above them.

Never scrape or guess personal details. Use only what the user provides, or
public professional pages they point to.

## 0.5 Live state first

Before any send in a session, confirm the account is clear: no
restriction, warning, checkpoint, or verification page. If the tracker
or log disagrees with live state (for example the log says a restriction
is in effect but no restriction page appears), correct the log
immediately, note the date, and work from the live state. A stale log
that contradicts what the browser shows is a bug, not a record. Never
send from a session that shows a restriction page; stop and report it.

## 1. Pick the path

Recommend the path with the best odds, and say why in one line:

| Situation | Best path |
| --- | --- |
| A hiring post on LinkedIn or X ("We are hiring, comment below") | **Comment** (2.1), then a **DM** to the poster referencing it |
| A recruiter is posting the role | A short **DM or InMail** to the recruiter with the job ID; no referral needed |
| A specific engineer on the team, no relationship | **Warm-up first** (2.4): 2-3 genuine comments over days, *then* a connection note, then the ask |
| Alumni from the user's college at the company | An **alumni connection note**, where the shared college is the hook; ask for 10 minutes of advice first, a referral second |
| A startup or founder | A **direct, value-first DM or email** to the founder: what the user built that is relevant, and a link |
| No person, just the company | Apply on the careers page first, then find a recruiter or alumnus and message them with the application ID |
| Personalised notes are used up, or the note field is not offered | **Blank invite, then a DM after they accept.** A real path, not a fallback to apologise for |

For one person with no campaign behind it, skip the table and go straight
to section 2.8.

## 2. Write the messages

### 2.1 Comment on a hiring post

- 1-3 lines, **specific and visible**: the role, one proof, and a hook. Not
  just "Interested".
- `Interested in the SDE-1 Backend role. I built a Go rate limiter handling [N] req/s (link in profile). Sending you a DM with my resume.`
- Then write the **follow-up DM** to the poster, referencing the comment.
- Give 2 variants. Tell them to comment early (posts get flooded) and to make
  sure their profile headline matches the role.

### 2.2 Connection note (LinkedIn)

- **Default limit: 200 characters.** That is the most-cited limit for free
  accounts. Premium is commonly 300, and some sources report 300 for
  everyone. Write every default variant at 200 or under and offer one
  300-or-under Premium variant. If you have a web tool, verify the current
  limit; otherwise say the composer enforces the real limit.
- Free accounts get only a few personalised notes per month: 5 per month
  on the current Help pages (some Help pages say 3, LinkedIn contradicts
  itself). Premium notes are unlimited. **A blank connection request plus
  a DM after they accept** is a perfectly good path, so offer it.
- **Note or blank?** With a note: 25.3% acceptance, 8.2% downstream
  reply. Blank: 27.6% acceptance, 5.3% downstream reply (Belkins/Expandi,
  11.5M requests, 2025). A note trades a little acceptance for more
  replies. Rule: **add a note only with a specific hook** (their post, a
  shared event, a mutual connection). If there is nothing specific to
  say, send it blank and earn the reply in the first DM instead. Never
  add a generic note just to fill the box.
- Shape: a hook (why them), then who you are in a few words, then a soft
  reason to connect. **No ask in the note** unless the path is recruiter
  plus job ID. The formula is `{one specific reference to them} + {one line
  of who you are} + {no ask}`.
- Show the exact **character count** for each variant.

```
Saw your post on killing the discovery call - we did the same thing in March
and it worked. I run ops at a 12-person studio. Would like to follow along.
                                                                    [187/200]
```

### 2.3 DM / InMail / email (after connecting, or to a recruiter)

- **First DM: under 400 characters**, a value or a specific question,
  one ask, no pitch in the connection note. Short InMails under 400
  characters get 22% more responses in LinkedIn's own data. Keep it to
  two to four sentences. An email runs longer, 150 words or under.
- **InMail only for unreachable, time-sensitive, or ignored-5-to-7-days
  high-value targets.** InMail averages a 6.4% reply (18 to 25% for
  recruiting, LinkedIn's own analysis), so a connection plus a DM beats
  it for most targets. When InMail is the right call, keep it under 400
  characters with the key point in the first 30 to 40 characters of the
  subject line.
- **Wait a day after they accept before the first message with an ask.**
  The thank-you in 2.6 goes out first, on the day they accept or the next
  morning. The ask comes after.
- **Two to four sentences.** A screen of text is a delete.
- Structure: a specific hook, then one proof (with a link), then **one small,
  clear ask** ("Would you be open to referring me for SDE-1, Job ID 12345?",
  or for alumni "Could I ask you 3 quick questions about the team?"), then an
  easy out ("Totally understand if not").
- Reference the specific thing from the note. Continuity is the whole
  reason the note was specific.
- **Give something before asking.** A number, a template, a name, an answer.
- **No calendar link in message one.** It reads as a funnel, because it is.
- Emails: 3 subject lines, short and specific, e.g.
  `SDE-1 (Job 12345): built a Go rate limiter`.

### 2.4 Warm-up (when there is no relationship)

Plan 2-3 genuine comments over days before requesting a stranger who
posts: a thoughtful comment on their recent post (draft it, but the user
must actually read the post), or a reaction to their talk, blog or
open-source project. **No fake engagement.** Comments must add something
real. This is high-prior-probability practice, not a measured lift: no
controlled study of comment-first versus cold was found, so never quote
a warm-up acceptance percentage. The logic is recipient-side: people
check your profile before replying, and a recent useful post plus
substantive comments make a cold message warm.

### 2.5 Referral ask and referral blurb

Ask only a real connection, never a stranger, and only after at least a
real exchange. Name the specific role plus one line on why the user fits
it. Make the ask tiny ("Would you be comfortable forwarding my profile
to [name]? Happy to draft a line you can paste") and offer the draft
below, with no obligation. Never ask in the first message, never ask
with no role or context, and never follow up aggressively. This is
practitioner consensus, evidence Weak: no benchmark study of
referral-ask formats was found.

Referral blurb, 2-3 lines the referrer can paste into their internal
referral form:
`<Name> is a <graduation year> <degree> grad who built <X> with <Y> (<link>),
strong in <skill>. Applying for <role>, Job ID <id>.` Fill every field from
the profile or the user. Never guess a year or degree.

### 2.6 Thank-you DM (after they accept)

A connection that goes quiet is a wasted accept. Send the thank-you the day
they accept, or the next morning at the latest.

- **Two to four sentences, specific and short.** One line of thanks that
  names what they did or said, one line of who you are, one specific
  line about their work or team that names a real paper, project, post,
  or team, not just the company name, one soft line about hearing what
  they are building. No benchmark study of thank-you DM formats was found;
  the rule is practitioner consensus, evidence Weak.
- Shape: `Hi [Name], thanks for connecting. I am [one line of who you are].
  Your work at [Company] is close to what I work on. Would love to hear what
  your team is building.`
- **No ask in the thank-you.** The ask comes later, after a real exchange,
  through the follow-up flow below.

### 2.7 Follow-ups

Two. That is the number.

- **+4 days** - add something new (an updated project, a newly posted role).
  Never "just bumping this" or "following up on my last message". If you
  have nothing new, you have no follow-up.
- **+10 days** - the close-the-loop message. Say you will stop, and mean it.
  This one gets a surprising share of the total replies, because it removes
  the pressure.

Then stop. A third follow-up converts nobody and costs the relationship.
The data backs the limit: 3-message sequences reply best at 9.8%, while
5 or more messages drop to 5.0% reply.

### 2.8 One person, no campaign

When the user is reaching out to one specific person and there is no
campaign behind it, skip section 1 and run this straight line: the
connection note (2.2), the thank-you when they accept (2.6), the first
message a day later (2.3), then the two follow-ups (2.7). Same limits,
same shapes, same tracker row. Nothing about a single message is simpler
than the campaign version. It is the same craft with one row instead of
many.

## 3. Rules for every message

- **Europe-only, strictly.** Never message a contact whose Europe
  location is unconfirmed, even when the user says reach out to everyone.
  Filter first, report the dropped ones.
- **No job outreach to pure professors.** Industry leaders who also hold
  academic titles are fine. A professor with no industry role is not.
- **Permanent exclusions.** TikTok and ByteDance, Korea, Israel. Never
  queue or message them.
- **Never withdraw a LinkedIn invite.** An invite that went out stays out.
- No "Dear Sir/Ma'am", "I hope this finds you well", "I am writing to...", or
  "please refer me" with nothing else.
- One proof and one ask per message. Make yes take 30 seconds: include the
  job ID and resume link.
- Never fabricate a connection, a shared experience, or an achievement.
- Respect a no or no reply. Do not double-message, and do not message two
  people on the same team on the same day.
- All messages go through `/sp-human` before they go out.
- Send the note, the DM and the follow-ups through the host agent's tools
  when the user says go. The host's own approval flow is the gate.

## 4. Tracker

For multiple targets, keep `<profile>/outreach.md` (append):

`| Company | Person (role) | Path | Sent | Accepted | Replied | Meeting | Status | Follow-up on |`

Track sent, accepted, replied, and meeting for every target, so the
skill learns its own rates instead of quoting vendor benchmarks as its
own. Personalise every message. No identical blasts. Update the row when
a reply lands, a follow-up goes out, or the thread closes. When a
connection accepts, set Follow-up on to the +4 day date; after the +4
day message goes out, set it to the +10 day date. A thank-you with no
follow-up date is an unfinished row. Prune
non-responders after 30 days: mark them closed, stop following up, and
do not re-queue them without a new reason.

## Output

For each target: the path and the one-line reason, the comment (if the path
starts with one), the connection note with its exact character count, the DM,
the thank-you DM, the referral blurb if a referral is the goal, and both
follow-ups with the days they go out. Then the tracker row. Send through the
host agent's tools when the user says go.
