---
name: sp-verify
license: MIT
description: >-
  Verify your identity, workplace, or school on LinkedIn and run the
  profile-completeness checklist before a job search. Use whenever the user
  asks about getting verified, the verified badge, or whether their profile
  is ready to apply. Picks the right route by country, gives the exact
  mobile-app steps, and never invents a verification status.
---

# sp-verify

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Gets you verified and checks your profile is ready before a job search. Verification is free, optional, and never for sale. It puts a badge beside your name that travels with you into the feed, comments, search, and job applications, and recruiters can filter for verified members. Roughly half of onboarded founders in one 2026 guide lacked it, so it is the cheapest trust signal on the platform.

## What verification is, and what it is not

Three separate verifications exist, and each one is its own badge:

- **Identity.** Proves you are who you say you are.
- **Workplace.** Proves you work where your profile says you work.
- **School.** Proves you studied where your profile says you studied.

A badge shows what is verified and nothing more. It does not prove your skills, your experience, or your claims. Never tell anyone you are verified for something you are not. If the profile does not show the badge, you are not verified, and this skill never says otherwise.

The honest caveat on the numbers: LinkedIn claims verified members see 60% more profile views and 50% more engagement on average. Those are LinkedIn's own figures with no published method. Treat them as correlational, not causal. People who bother to verify also tend to have fuller profiles and more activity, and that alone would lift views. The real reason to verify is the recruiter filter and the trust signal, not the percentage.

## Pick the identity route by country

Identity verification runs in the LinkedIn mobile app only, not on desktop. Ask where the user lives and pick the route:

- **United States, Canada, or Mexico: CLEAR.** Government ID plus a phone number, in the mobile app. CLEAR is the partner LinkedIn uses in these three countries.
- **India: DigiLocker.** The government document wallet, in the mobile app.
- **Everywhere else: Persona.** A government-issued passport with an NFC chip, scanned in the mobile app. If the user has no NFC passport, say so plainly and stop on identity: there is no other route, and guessing a different one invents a path that does not exist.

Give the user the exact steps for their route, in order:

1. Open the LinkedIn mobile app.
2. Go to the profile, then Settings, then Verification.
3. Pick Identity verification and follow the partner flow (CLEAR, DigiLocker, or Persona).
4. Come back and tell the skill it is done, or paste a screenshot of the badge, so the status can be recorded in `<profile>/log.md`.

## Workplace and school verification

- **Workplace.** LinkedIn sends a code to the work email address listed on the profile. The user opens that inbox, enters the code, and the badge appears. If the user has no access to that work inbox, workplace verification cannot be done. Do not invent a work email.
- **School.** The same pattern with the school email address, where LinkedIn offers it. If the school is not listed or the email is gone, say so and move on.

Do workplace and school after identity, not before. Identity is the one recruiters filter on most, and it is the one visitors check first.

## The recruiter filter

More than 100 million members are verified, and recruiters can filter search results to verified members only. That is the practical payoff: in a pile of applicants, a verified profile survives a filter an unverified one does not. Say that to the user in those terms. Do not promise it gets them hired. It only keeps them in the pile.

## The profile-completeness checklist

Run this before any job search, after verification. Read the live profile (use `/sp-profile` for the scored version) and check each item. Report each one as done, missing, or partial, with the fix in one line. Never mark an item done from memory. If it cannot be read, mark it unverified, not done.

- **Photo.** A real headshot, current, face visible, no heavy filter.
- **Headline.** 220 characters, says what you do and who it is for, not just a job title.
- **About.** First two lines carry the point, the rest proves it with numbers.
- **Experience.** Every role has a title, dates, and at least one result with a number.
- **Skills.** Listed from LinkedIn's taxonomy, top 3 to 5 are the ones that matter, and they match the roles being applied for.
- **Featured.** At least one item pinned: the best work, not the most recent.
- **Open to Work.** Titles, locations, and job types set, and the visibility choice made on purpose (recruiters only, or the public frame).
- **Services.** Only if the user sells services. If they do, up to 10 services listed with a description and a rate range. If they do not, skip it and say so.

Log the result in `<profile>/log.md` with the date and the count of done, missing, and partial items. Hand the fixes to `/sp-profile`, which rewrites in fix-first order.

## Rules that make the difference

- **Never invent a verification status.** If the badge is not visible on the profile, the user is not verified. Say that, then give them the route.
- **The mobile app does the verifying.** The skill picks the route and the order, and checks the badge after. It does not pretend to verify anything itself.
- **Free means free.** If anything asks for payment to verify, stop. Verification is never for sale.
- **One thing at a time.** Identity first, then workplace, then school, then the completeness checklist. A profile that is verified but half empty wastes the badge.
