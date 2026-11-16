---
name: sp-email
license: MIT
description: >-
  Find a person's work email online, label it published or a guess, then
  send the CV outreach email with the industry resume attached and track
  the send, bounce, and reply in outreach.md. Use when the user wants to
  email someone about a role, or asks "find their email".
---

# sp-email

Profile directory: `<profile>` holds voice.md, log.md, plan.md and outreach.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

LinkedIn covers the invite and the DM. This skill covers the other half of
outreach: the email. Same campaign, different channel. Find the address
first, check it is real, then send the same CV outreach the LinkedIn path
uses, and watch for the bounce.

## 0. Inputs

Ask for, in one batched question:

1. **Who** - name, role, company. Or a company with no person yet.
2. **The country** - the outreach template names the country, so this is
   required, not optional.
3. **What you already know** - a LinkedIn profile, a company page, a paper,
   a talk, anything that narrows the search.
4. **What the user wants** - a role, a conversation, a referral. Be honest
   internally, even if the message does not lead with it.

## 1. Find the email

Work in this order. Stop at the first hit that is usable, and say where it
came from.

1. **Company site.** Team page, contact page, press releases, careers page.
   The company domain is the anchor for everything after.
2. **Published in public.** Papers (author contact line), conference speaker
   pages, talks, company blog posts, news articles, press quotes, GitHub
   profiles, the LinkedIn contact info section. If the address is printed
   somewhere a stranger can read it, it is published.
3. **Pattern guess, only from a known pattern.** If you have a published
   address at the same domain, the company pattern is visible. Common
   patterns: `first.last@`, `firstinitiallast@` (jsmith@),
   `first@`, `firstlast@`. Build the guess from the pattern you actually
   saw, not the pattern you expect.
4. **Nothing found.** Say NOT FOUND plainly and stop. Do not invent an
   address, do not try a random pattern at a domain with no evidence, and
   do not email a personal address you happened across.

### Label every address

- **PUBLISHED** - seen printed somewhere. Name the source.
- **GUESS** - constructed from a pattern seen at the same domain. Name the
  pattern and the published address it is based on.
- **NOT FOUND** - no address, no pattern, nothing to send to.
- **DO NOT EMAIL** - the person asked not to be contacted, the only address
  is personal, or the address belongs to someone else at the company.

A GUESS is a weaker send than a PUBLISHED address. Say so when you present
it, and let the user decide. Never present a GUESS as if it were verified.

### Staleness checks

An address that was right a year ago can be dead now. Before you send,
check the person still holds the role at the company:

- **Role change.** They left, got promoted out of the team, or moved
  companies. The old address may still deliver, but to the wrong person.
- **Acquisition or shutdown.** The company was acquired, the domain changed,
  or the company is gone. Attabotics went bankrupt in July 2025 and was
  acquired that September; a guess at its old domain was already wrong
  before the role ended.
- **Dead domain.** A company address that no longer exists. One TUM
  address was dead and had to be replaced by a secretariat redirect.
- **Auto-reply.** An out-of-office that says unreachable until a date is
  not a bounce, but it is a reason to wait, not to try another address.

If the staleness check fails, say so and do not send. A stale address is
worse than no address: it wastes the one shot at a first impression.

## 2. Filters first

Apply these before you write a word. They are standing rules, not
suggestions.

- **Europe-only, strictly.** Never email a contact whose Europe location is
  unconfirmed, even when the user says reach out to everyone. Filter first,
  report the dropped ones.
- **No job outreach to pure professors.** Industry leaders who also hold
  academic titles are fine. A professor with no industry role is not.
- **Permanent exclusions.** TikTok and ByteDance, Korea, Israel. Never
  queue or send to them.
- **Never invent or embellish facts.** Never claim CPT eligibility for US
  internships. Never guess a language level on any form or in any message.
- **Never withdraw a LinkedIn invite.** That rule lives on the LinkedIn
  side, but it is part of the same outreach. An invite that went out stays
  out.

## 3. Write the email

Use the approved CV outreach template. Swap only the name, the company,
and the country. Nothing else.

**Subject:** `Full-time robotics perception roles in [country]`

**Body:**

```
Hi [First],

I am reaching out because I am looking at full-time industry roles in robotics perception and computer vision in [country], and I wanted to ask if [Company] has any openings right now, or if you know of teams hiring in this space.

My work is in visuo-tactile SLAM and 3D Gaussian Splatting for robot perception, plus manipulation. My CV is attached. If a resume is also needed, I am happy to send it.

Thanks,
Krishi
krishiattriwork@gmail.com · archerkattri.github.io · linkedin.com/in/krishi-attri15
```

- Attach the industry resume to every email.
- Run the email through `/sp-human` before it goes out, same as any draft.
- If the person already replied to a LinkedIn DM or the role is a specific
  posting rather than a general openings question, say so and adjust the
  first line to name it. Do not force the general template onto a specific
  conversation.

## 4. Send

Send through the host agent's email tools when the user says go. The
host's own approval flow is the gate. Send one email per person, never a
blast with several recipients. Log the send immediately, before you move
to the next target, so a crash does not lose the record.

## 5. Follow-ups

Two. That is the number, same as `/sp-outreach`.

- **+4 days** - add something new (an updated project, a newly posted
  role). Never "just bumping this" or "following up on my last message".
  If you have nothing new, you have no follow-up.
- **+10 days** - the close-the-loop message. Say you will stop, and mean
  it. This one gets a surprising share of the total replies, because it
  removes the pressure.

Then stop. A third follow-up converts nobody and costs the relationship.
Do not follow up on an email that bounced.

## 6. Bounces and replies

Watch the inbox after every send. A bounce is a result, not a retry prompt.

- **Bounce on a GUESS address.** Mark it a dead end and move on. Never
  retry a bounced guessed address, and never try another format at the
  same domain without new evidence. Two Ocado guesses failed this way on
  the same pattern, and retrying the pattern would have failed twice more.
- **Bounce on a PUBLISHED address.** Mark it stale, not dead. Check
  whether the person moved or the domain changed, and only then decide if
  a new address is worth finding.
- **Bounce on any address.** Never resend to it. Six dead ends from one
  batch stay dead.
- **Reply.** Log it, quote it, and stop the follow-up clock for that
  person. A reply, even a no, ends the sequence.
- **Auto-reply.** Log the date it lifts. Do not follow up before then.

## 7. Tracker

Keep `<profile>/outreach.md` (append). This is the same tracker
`/sp-outreach` uses, with an Email column added:

`| Company | Person (role) | Path | Email | Sent | Status | Follow-up on |`

Path is `email` for this skill, or `email + LinkedIn` when both channels
are running on the same person. Email carries its label: `PUBLISHED`,
`GUESS`, `NOT FOUND`, or `DO NOT EMAIL`. Status is `sent`, `bounced`,
`replied`, or `closed`. Update the row when a bounce lands, a reply lands,
or a follow-up goes out.

## Output

For each target: the address with its label and its source, the staleness
check result, the filters passed or the reason dropped, the email with the
subject line, and the tracker row. Send through the host agent's tools
when the user says go. Then watch for the bounce or the reply, and log
whichever lands.
