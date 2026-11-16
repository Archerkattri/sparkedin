---
name: sp-poll
license: MIT
description: >-
  Design a LinkedIn poll and follow up manually with the people who voted.
  Use whenever the user wants a poll, asks what to ask their audience, or
  wants to follow up on poll results. Covers the 140-character question, 2 to
  4 options at 30 characters each, durations of 1 day, 3 days, 1 week, or 2
  weeks, the results post, and the manual voter follow-up list. The author
  sees who voted how; the follow-up is always human.
---

# sp-poll

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Designs a poll worth voting on, then turns the voter list into
conversations. Teach the disagreement about polls honestly, because
the format is the sharpest disagreement in the field. Within-creator,
polls measured -58% reactions, the worst format (Flypost, only 47
creators qualified, so a strong hint, not settled). Cross-sectionally,
polls had the highest median reach (1,154, MagicPost) and a 1.64x
reach multiplier (AuthoredUp, cited in Flypost), while scoring
4.20% on company pages (Socialinsider) and 0.37% engagement in a
fourth dataset (Ordinal). Votes are not reactions. Use a poll
sparingly, for research, never as a growth engine. Max 1 poll per
month. Its real value is not the percentages. It is that the author sees exactly
who voted and how. That list is the point of the skill.

## The limits, exact

- **Question:** 140 characters, one question only.
- **Options:** 2 to 4 (5 in the iOS app). **30 characters each.**
- **Duration:** 1 day, 3 days, 1 week, or 2 weeks. Default is 1 week.
- **One vote per member.** Voters can undo and re-vote while the poll is
  open.
- **Not anonymous to the author.** The author sees who voted and how.
  Other voters see only percentages.
- **Cannot edit after posting.** A typo means delete and repost.
- **Banned topics.** Never ask about health, religion, politics,
  ethnicity, sexual orientation, union membership, or precise location.

## Design the poll

**1. Start from a real disagreement.** A poll works when the audience
genuinely splits. "What should I build next" works. "Do you like my work"
does not. If the answer is obvious, it is not a poll, it is a like button
with extra steps. Prefer a diagnostic or stakes poll with a real
trade-off over an opinion poll with no stakes: "Best day to post?"
fails because nothing rides on the answer.

**2. Write the question first.** One sentence, 140 characters or fewer,
plain language, no jargon the audience has to decode before voting. Read
it out loud. If it needs a second sentence to make sense, rewrite it.

**3. Write the options.** 30 characters each, and they must be genuinely
different choices, not four ways of saying yes. Prefer 3 options:
not 2 yes/no, not 4 diffusing votes. Order matters: put the
most likely answer second, not first, so the first option does not win by
position alone. Never include "Other" or "See results" as an option.
LinkedIn already shows results to voters.

**4. Pick the duration.** 7 days, or 3 days. 7 days is the consensus
recommendation; 3 days is the dissent, because reach peaks in the
first 18-24 hours and a 7-day poll buries the results post. 1 day for
a hot, time-bound question only, and 2 weeks only when the poll is
tied to a decision that far out. Longer is not better. A poll that sits open for two weeks looks
abandoned by day five. No LinkedIn-published duration guidance exists,
so present 7 or 3 days as practitioner consensus, not a LinkedIn rule.

**5. Draft the post around it.** The poll is the post. The text above it
is one or two lines: why you are asking, and what you will do with the
answer. Say what you will do with the answer, because a poll with no
consequence is a survey nobody trusts. Run the text through `/sp-human`
before it goes out.

## Publish it

Hand the finished poll to `/sp-publish`. If the API rejects a poll post,
post it in the browser with the user clicking post. Either way, log it in
`<profile>/log.md` with the date, the question, and the duration, so the
results post has something to point back to.

## After it closes

**1. Write the results post.** One short post, within days of the close,
while voting is fresh: what won, by how much, and what you will do
about it. A poll without a results post teaches the
audience their vote went nowhere. Link back to the original poll.
Share what you learned and what you will do differently. Do not
teach that a set share of voters return to see results, or that a
February 2026 re-weighting gave polls the highest per-view dwell:
both are single-vendor, unverified claims, so leave them out.

**2. Build the follow-up list.** The author can see who voted and how.
Read that list in the browser and sort it:

- **Voted for the winning option and you know them.** A short reply or
  DM: thanks for voting, here is what happens next.
- **Voted for an option that signals a need you can help with.** A
  personal message, one sentence on what they picked and why you are
  writing. No pitch in the first message.
- **Someone you wanted to reach voted.** That is the warmest open you
  will get all week. Use it within two days of the close, while the poll
  is still fresh in their mind.
- **Everyone else.** No follow-up. A vote is not consent to be messaged.

**3. Follow up manually.** The follow-up is always human. Write each
message by hand, in the user's voice, one person at a time. Never batch
the voter list into a sequence, never automate the sends, and never
message someone only because they voted. The vote opens the door. It
does not oblige them to walk through it.

## Rules that make the difference

- **One poll per month, maximum.** Polls are a research tool, not a
  growth engine. Never run them weekly.
- **One question, one decision.** If the poll needs two questions, it is
  two polls, on two different days.
- **Never fabricate the results.** Report the real percentages from the
  poll. If the turnout was low, say so. A poll with 11 votes is still a
  poll, and pretending otherwise is worse than the small number.
- **No sensitive questions.** The banned list above is a hard rule, not a
  suggestion.
- **Never export or scrape the voter list.** Read it in the browser and
  write down the names worth following up. Any tool that pulls that list
  out of the session is scraping, and this skill does not do that.
