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

Gets you verified and checks your profile is ready before a job search. Verification is free, optional, and removable, and never for sale. It puts a badge beside your name that travels with you into the feed, comments, search, and job applications, and recruiters can filter for verified members. The name on the verification must match the profile name. It is the cheapest trust signal on the platform.

## What verification is, and what it is not

Three separate verifications exist, and each one is its own badge:

- **Identity.** Proves you are who you say you are.
- **Workplace.** Proves you work where your profile says you work.
- **School.** Proves you studied where your profile says you studied.

A badge shows what is verified and nothing more. It does not prove your skills, your experience, your seniority, your hireability, or your claims. Never tell anyone you are verified for something you are not. If the profile does not show the badge, you are not verified, and this skill never says otherwise.

The honest caveat on the numbers: LinkedIn claims verified members see 60% more profile views and 50% more engagement on average. Those are LinkedIn's own figures with no published method. Treat them as correlational, not causal, and never promise the lift. People who bother to verify also tend to have fuller profiles and more activity, and that alone would lift views. The real reason to verify is the recruiter filter and the trust signal, not the percentage. Do not use the "+50% engagement, nearly +90% profile views, 115M+ verified" figure from a Facebook reel: it is unverified, so leave it out entirely.

Readers can filter comments to verified members only (since October 2026), but LinkedIn has not said the badge raises comment ranking, so do not claim it does.

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

- **Workplace, work email.** LinkedIn sends a code to the work email address listed on the profile. The user opens that inbox, enters the code, and the badge appears. This route covers limited companies only. If the user has no access to that work inbox, workplace verification by email cannot be done. Do not invent a work email.
- **Workplace, Microsoft Entra Verified ID.** Where the employer offers it, verify through the employer's Entra Verified ID flow instead of, or in addition to, the work email code.
- **Workplace or school, LinkedIn Learning licence.** An active LinkedIn Learning licence from the employer or the school can also verify workplace or education, where LinkedIn offers that route.
- **School.** The same pattern with the school email address, where LinkedIn offers it. If the school is not listed or the email is gone, say so and move on.

Do workplace and school after identity, not before. Identity is the one recruiters filter on most, and it is the one visitors check first.

## The recruiter filter

Recruiters can filter search results to verified members only. That is the practical payoff: in a pile of applicants, a verified profile survives a filter an unverified one does not. Say that to the user in those terms. Do not promise it gets them hired. It only keeps them in the pile. Do not quote a count of verified members: no verified count is used here, so do not invent one.

## The profile-completeness checklist

Run this before any job search, after verification. Read the live profile (use `/sp-profile` for the scored version) and check each item. Report each one as done, missing, or partial, with the fix in one line. Never mark an item done from memory. If it cannot be read, mark it unverified, not done. This checklist is the skill's own readiness check, not a LinkedIn score: LinkedIn no longer surfaces an All-Star meter or any profile completeness score.

- **Photo.** A real headshot, current, face visible, no heavy filter.
- **Headline.** 220 characters, says what you do and who it is for, not just a job title.
- **About.** First two lines carry the point, the rest proves it with numbers.
- **Experience.** Every role has a title, dates, and at least one result with a number.
- **Skills.** 35 to 50 skills listed from LinkedIn's taxonomy, top 3 pinned, and the top 3 to 5 are the ones that matter and match the roles being applied for. Aim for 10 or more endorsements on the top 3 to 5: endorsements are a weak, logarithmic signal, so 0 to 10 matters and 50 to 200 adds about nothing.
- **Featured.** At least one item pinned: the best work, not the most recent.
- **Open to Work.** Titles, locations, and job types set, and the visibility choice made on purpose (recruiters only, or the public frame).
- **Services.** Only if the user sells services. If they do, up to 10 services listed with a description and a rate range. If they do not, skip it and say so.

Log the result in `<profile>/log.md` with the date and the count of done, missing, and partial items. Hand the fixes to `/sp-profile`, which rewrites in fix-first order.

## Rules that make the difference

- **Never invent a verification status.** If the badge is not visible on the profile, the user is not verified. Say that, then give them the route.
- **The mobile app does the verifying.** The skill picks the route and the order, and checks the badge after. It does not pretend to verify anything itself.
- **Free means free.** If anything asks for payment to verify, stop. Verification is never for sale.
- **Never quote a single Premium price.** Prices vary by market and offer, so do not state one price as the Premium price.
- **One thing at a time.** Identity first, then workplace, then school, then the completeness checklist. A profile that is verified but half empty wastes the badge.
