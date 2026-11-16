---
name: sp-profile
license: MIT
description: >-
  Score a LinkedIn profile out of 100 against a 12-part rubric and rewrite the
  parts that lose points - headline, about, experience, featured, banner -
  then curate Featured from real performance and set up the Services page.
  Use when the user says "optimize my profile", "score my LinkedIn", "rewrite
  my headline", "fix my about section", "update Featured", "pick what to
  pin", "set up or refresh Services", or pastes their profile and asks how
  it reads.
---

# sp-profile

Profile directory: `<profile>` holds voice.md, log.md, plan.md and analytics.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

A profile is not a resume. A resume answers "what have you done". A profile
answers "should I message this person", and it answers it fast, from the
headline and the first two lines of the about. Do not quote a skim time
for this: the often cited 6 second figure comes from a 2018 Ladders
eye-tracking study of resumes, not LinkedIn profiles, so it is not a
LinkedIn finding.

## Input

Ask the user to paste: headline, about section, current role and the last two
experience entries, plus whether they have a banner and featured section. A
screenshot of the top card is enough for the first pass. Or read the
profile through the host agent's browser tools.

Blocked read: if the profile will not load (restriction, checkpoint,
sign-in wall), do not guess and do not score from memory. Draft from the
user's resume or CV instead, label every draft as drafted-from-resume, and
score only after access comes back and the live profile can be read.

## Score it

Read `rubric.json` in this folder. Twelve items, 100 points, each with what
full marks looks like. That score is this skill's own rubric, not a
LinkedIn score: LinkedIn no longer surfaces an All-Star meter or any
profile completeness score, so never present the total as LinkedIn's.
Score every item you actually saw, show the table,
and give the total. Be honest - most profiles land in the 30s and 40s on
the first pass, and a generous score is useless.

Score only what you verified. If the read could not verify an item (photo,
skills, recommendations, activity, contact), mark it unverified and leave
it out of the total. Never score it zero and never guess it. The total is
out of the points for the verified items only, so say that plainly, for
example 28/58 with 42 points unverified, and say what would verify them.

```
PROFILE SCORE  41/100

  headline            3/12   job title only, no outcome, no audience
  about first 2 lines 2/10   opens with "passionate about"
  about body          4/10   history, not offer
  featured            0/8    empty
  banner              0/6    default blue
  ...
```

## Then rewrite, in this order

Fix in descending order of points lost. Do not rewrite everything at once -
the user has to actually paste each of these in.

**1. Headline (220 characters max).** The formula that works:
`{target title recruiters type} | {2-3 core skills in LinkedIn taxonomy} | {1 specific proof}`.
Use the market wording of the title, not an internal title, and no
adjectives like "passionate", "results-driven", or "strategic thinker".
Give three options. Do not quote headline search-weight figures such as
"3x" or "40%": those weights are unverified vendor figures, and the
direction only is that the headline is the heaviest-weighted search field.

**2. About, first two lines.** Everything after line 2 is behind "see more" on
mobile, so those two lines are the whole about section for most readers. They
must state the role wanted plus the strongest proof. No "passionate", no "results-driven",
no third-person bio, no opening with your own name.

**3. About body.** First person, 150 to 300 words total. Structure:
the role, level, and focus plus what you want next; 2 to 3 concrete
achievements with numbers; a skills and tools line using the job
description terms once, in context, with proof; then a call to action
with role type, location or remote, and how to reach you. Do not
keyword-stuff the About: since the March 2026 feed rebuild, LinkedIn
retrieval reads meaning, so repeated job description terms with no proof
read as slop and risk the generic-content classifier.

**4. Featured.** Use the full method in the section below: top 3 to 5 items
from real performance, mixed types, best first. An empty featured section is
eight points and the only place on the profile you fully control. No
measured conversion data exists for Featured order or count, so 3 to 5
is practitioner consensus, not evidence.

**5. Experience.** Each role gets one line of scope and two to three bullets
that are outcomes with numbers, not duties. Each bullet names the system,
states the scope, and carries a number. Use titles in market wording
and keep titles and dates aligned with the resume the user sends:
a mismatch is a trust killer. Cut anything older than ten years
to a single line.

**6. Skills.** List 35 to 50 skills, spelled as LinkedIn's own taxonomy
spells them ("Power BI", not "PowerBi dashboards"). The cap is 100, but
the useful range is 35 to 50: above that the list dilutes. Pin the top 3
and get 10 or more endorsements on the top 3 to 5. Endorsements are a
weak, logarithmic signal: 0 to 10 matters, 50 to 200 adds about nothing.
Do not teach "5+ skills = 17x more views" as fact: it is an old LinkedIn
claim with no published method, so flag it as a vendor claim if it comes
up at all.

**7. Recommendations.** Two to three specific, recent recommendations
from a direct manager outweigh 99 or more endorsements for human trust,
because a recruiter can quote them. A good one names a specific outcome,
not character. The skill may describe what makes a good recommendation
when the user already has one, but it never drafts or sends a
recommendation request: never ask anyone for a LinkedIn recommendation
unless the user specifically requests it.

**8. Banner.** One sentence of positioning and one way to reach you. The
default blue gradient is the clearest signal on the page that nobody is home.

**9. Open to Work.** Recruiters-only if employed, public (green frame) if
openly hunting. Set titles, locations, and job types on purpose, and
keep replying to InMails.

**10. Follow or Connect primary.** Set Follow as the primary button only
if the user posts weekly; otherwise keep Connect primary. The setting
is under Settings and Privacy, Visibility, Followers. Do not tell the
user to turn on Creator Mode: that toggle was removed in March 2024 and
its features (Follow-primary, newsletters, Live, analytics) are
default-on for every profile.

## Featured: what to pin

Featured sits just below About and above Activity, as a scrollable
carousel. It stays hidden until the first item is added. Each item can be
a post, an article or newsletter edition, an external link, or uploaded
media or a document such as a PDF. Premium Business, Sales Navigator, and
Recruiter also allow pinning an experience, certification,
recommendation, course, award, skill, project, or education. Event and
Group posts cannot be featured, and a connections-only post stays
connections-only even when featured.

**1. Pick from performance, not from pride.** Read
`<profile>/analytics.md` if it exists, or the output of `/sp-audit` or
`/sp-analytics`. Rank the user's posts by engagement rate and reach, not
by raw impressions. Pick the top 3 to 5. A post the user loves that nobody
read does not go in Featured. A post that earned real comments does.
No measured conversion data exists for Featured order or count, so
3 to 5, best first, is practitioner consensus, not evidence.

**2. Mix the types.** A good Featured section is not six posts. Aim for a
mix across these four, in this order:

- The best-performing post, the one with the strongest real engagement.
- The flagship work: the paper, the project, or the package that defines
  the user. Link to the real thing, with its real numbers.
- The resume or CV, as an uploaded document, so a recruiter can grab it
  without asking.
- The portfolio or personal site link, so the profile is not a dead end.

**3. Write the title and description for each item.** LinkedIn shows the
title the user sets. Write it like a headline: specific, with a number
where one exists, under 60 characters where possible. The description is
one sentence on why this item is here. Never invent a metric for a title.
If the post has no number, the title says what it is about, plainly.

**4. Order them.** Drag to reorder in the browser, best first. The first
item is the only one most visitors see without swiping. Put the flagship
there, not the most recent.

**5. Review every quarter.** Featured rots. A pinned post from a year ago
tells a visitor the user stopped. Every three months, re-run the ranking
and swap out anything that no longer earns its slot. Log the current
Featured list in `<profile>/plan.md` so the next review starts from what
is live, not from memory.

## Services: the mini-storefront

Services is a free dedicated page on a personal profile, or on a Company
Page with 500 or fewer employees. Clients can message the user regardless
of connection degree, and the page is discoverable through LinkedIn search
and Google. List **up to 10 services** from LinkedIn's roughly 250
categories, with a description of about 500 characters, a rate range, a
location, and a remote option. Premium Business, Sales Navigator, and
Recruiter Lite add media on the page, a Services Showcase preview, and a
**Request services** button, plus an extra service-request opt-in. Client
reviews are available for profile-managed pages, not Company-managed ones.

**1. Pick the services first.** List what the user actually sells or does
for others, in the user's own words, before looking at LinkedIn's
categories. Then map each one to the closest category. If a service has no
honest category match, it does not go on the page. Never stretch a service
to fit a category that sounds better.

**2. Write the description.** About 500 characters, plain language, one
paragraph. Say what the user does, who it is for, and what the client
walks away with. No superlatives, no invented clients, no invented
results. If the user has a real number, a real project, or a real client
type, that goes in. If not, the description says what the work is and
stops there.

**3. Set the rate range honestly.** A range the user would actually accept,
not an aspirational one. If the user does not want rates public, use
"Contact for pricing" and leave the rate out. A wrong rate costs more than no rate: it filters out
the right client and attracts the wrong one. No published inquiry or
conversion benchmarks exist for Services, so do not promise a volume
from any rate choice.

**4. Set location and remote.** On-site, remote, or both, as the user
actually works. Do not claim remote for work that needs the user's hands
on hardware.

**5. Reply fast and invite reviews.** Reply within 24 hours: LinkedIn
shows a "usually responds within 24 hours" badge if the user replies
within a day to at least 80% of inquiries. Invite up to 20 past clients
to review the page. The mechanics are verified; conversion from either
is unmeasured, so do not promise it.

**6. Warn before setup.** Management type, personal or Company Page,
**cannot be changed after setup.** Ask the user which one they want, once,
before anything is created. Then the user creates it in the browser.

## Rules that make the difference

- **No API exists for Featured or Services.** The user adds everything in
  the browser. This skill drafts the titles, descriptions, and lists, and
  hands over a checklist. It never claims to have added anything itself.
- **Performance picks, not favorites.** If the analytics say a post
  underperformed, it does not get featured because the user likes it.
- **Never fabricate.** No invented metrics in a title, no invented
  clients in a Services description, no invented rate the user would not
  take.
- **Never draft or send a recommendation request** unless the user
  specifically asks for one.
- **Do not teach dropped myths as fact.** No "turn on Creator Mode"
  (toggle gone March 2024), no "5+ skills = 17x more views", no
  headline search-weight percentages, no keyword-stuffed About, and no
  All-Star meter. Where the evidence is only practitioner consensus or
  a vendor claim, say so.
- **Keep it current.** A Featured section older than a quarter is stale.
  Say so when it is, and offer the re-rank.

## Output

Score table, then the rewrites as copy-ready blocks in fix-first order, each
one already run through `/sp-human`. Re-score at the end and show the delta
honestly - if the rewrite gets to 88 and not 98, say 88, and say what the
remaining points need (usually recommendations, a real banner and posting
history, none of which a rewrite can create).

Save the rewrites to LinkedIn through the host agent's tools when the
user says go.
