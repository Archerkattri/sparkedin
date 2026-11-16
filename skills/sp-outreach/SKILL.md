---
name: sp-outreach
license: MIT
description: >-
  Run a whole outreach campaign on LinkedIn: pick the path first
  (comment-then-DM, recruiter with job ID, warm-up, alumni, founder,
  apply-then-message), then write the connection note, the DM, the two
  follow-ups and the thank-you after they accept, and track every target in
  outreach.md. Use when the user wants a referral, a job, an introduction,
  or is reaching out to several people at one company.
---

# sp-outreach

Profile directory: `<profile>` holds voice.md, log.md, plan.md and outreach.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

One person is a message. Several people is a campaign. This skill is the
campaign version of `/sp-dm`: it picks the path before it writes a word,
because the path decides what the message can say.

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

Never scrape or guess personal details. Use only what the user provides, or
public professional pages they point to.

## 1. Pick the path

Recommend the path with the best odds, and say why in one line:

| Situation | Best path |
| --- | --- |
| A hiring post on LinkedIn or X ("We are hiring, comment below") | **Comment** (2.1), then a **DM** to the poster referencing it |
| A recruiter is posting the role | A short **DM or InMail** to the recruiter with the job ID; no referral needed |
| A specific engineer on the team, no relationship | **Warm-up first** (2.4): 1-2 genuine interactions over a week, *then* a connection note, then the ask |
| Alumni from the user's college at the company | An **alumni connection note**, where the shared college is the hook; ask for 10 minutes of advice first, a referral second |
| A startup or founder | A **direct, value-first DM or email** to the founder: what the user built that is relevant, and a link |
| No person, just the company | Apply on the careers page first, then find a recruiter or alumnus and message them with the application ID |
| Personalised notes are used up, or the note field is not offered | **Blank invite, then a DM after they accept.** A real path, not a fallback to apologise for |

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
- Free accounts get only a few personalised notes per month. **A blank
  connection request plus a DM after they accept** is a perfectly good path,
  so offer it.
- Shape: a hook (why them), then who you are in a few words, then a soft
  reason to connect. **No ask in the note** unless the path is recruiter
  plus job ID.
- Show the exact **character count** for each variant.

### 2.3 DM / InMail / email (after connecting, or to a recruiter)

- 100 words or under for a DM, 150 words or under for an email.
- Structure: a specific hook, then one proof (with a link), then **one small,
  clear ask** ("Would you be open to referring me for SDE-1, Job ID 12345?",
  or for alumni "Could I ask you 3 quick questions about the team?"), then an
  easy out ("Totally understand if not").
- Emails: 3 subject lines, short and specific, e.g.
  `SDE-1 (Job 12345): built a Go rate limiter`.

### 2.4 Warm-up (when there is no relationship)

Plan 1-2 genuine touches before the ask: a thoughtful comment on their recent
post (draft it, but the user must actually read the post), or a reaction to
their talk, blog or open-source project. **No fake engagement.** Comments must
add something real.

### 2.5 Referral blurb

2-3 lines the referrer can paste into their internal referral form:
`<Name> is a <graduation year> <degree> grad who built <X> with <Y> (<link>),
strong in <skill>. Applying for <role>, Job ID <id>.` Fill every field from
the profile or the user. Never guess a year or degree.

### 2.6 Thank-you DM (after they accept)

A connection that goes quiet is a wasted accept. Send the thank-you the day
they accept, or the next morning at the latest.

- **Two to four sentences.** One line of thanks, one line of who you are, one
  specific line about their work or team, one soft line about hearing what
  they are building.
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

## 3. Rules for every message

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

`| Company | Person (role) | Path | Sent | Status | Follow-up on |`

Personalise every message. No identical blasts. Update the row when a reply
lands, a follow-up goes out, or the thread closes.

## Output

For each target: the path and the one-line reason, the comment (if the path
starts with one), the connection note with its exact character count, the DM,
the thank-you DM, the referral blurb if a referral is the goal, and both
follow-ups with the days they go out. Then the tracker row. Send through the
host agent's tools when the user says go.
