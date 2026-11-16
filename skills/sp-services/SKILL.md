---
name: sp-services
license: MIT
description: >-
  Curate the Featured section and set up the Services page on a LinkedIn
  profile. Use whenever the user wants to update Featured, pick what to pin,
  set up or refresh Services, or asks what belongs at the top of their
  profile. Picks the top 3 to 6 items from real performance, writes Featured
  titles and descriptions, and drafts the Services list of up to 10 services
  with a 500-character description and rate range. The user adds it in the
  browser; there is no API for Featured or Services.
---

# sp-services

Profile directory: `<profile>` holds voice.md, log.md, plan.md, and
analytics.md. Muse uses `~/workspace/linkedin/`, Claude Code uses
`~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Decides what belongs at the top of the profile and writes it, ready for
the user to add in the browser. Featured and Services are the two sections
a visitor sees before scrolling, and both are manual, rarely updated, and
have no API. This skill is the curation and the copy. The user does the
clicking.

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
by raw impressions. Pick the top 3 to 6. A post the user loves that nobody
read does not go in Featured. A post that earned real comments does.

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
not an aspirational one. If the user does not want rates public, say so and
leave the rate out. A wrong rate costs more than no rate: it filters out
the right client and attracts the wrong one.

**4. Set location and remote.** On-site, remote, or both, as the user
actually works. Do not claim remote for work that needs the user's hands
on hardware.

**5. Warn before setup.** Management type, personal or Company Page,
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
- **Keep it current.** A Featured section older than a quarter is stale.
  Say so when it is, and offer the re-rank.
