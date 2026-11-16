---
name: sp-jd
license: MIT
description: >-
  Paste a job description and get a keyword gap analysis against the user's
  profile and resume: which JD skills are already proven with quoted evidence,
  which are missing, what to tailor, and a cover letter angle. Use whenever
  the user pastes a job description, asks "do I match this role", "am I a fit
  for this", "what is missing", or wants a tailored resume or cover letter for
  a specific posting. Analyzes only, never invents or embellishes, and never
  submits an application.
---

# sp-jd

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Takes a job description and the user's own profile and resume, and shows
exactly where they match, where they do not, and what to change. It never
invents experience. A gap is a gap, and it says so in plain language.

## How ATS matching actually works

There is no universal ATS score and no universal cutoff. A score from a
resume grader is a third-party simulation, not an ATS output. Greenhouse,
Workday, and Lever do not expose a candidate-facing score. Ranking is
relative to the applicant pool for that one role. The top of the pool
surfaces, not everyone above a fixed percent.

Platforms do not match the same way, so do not teach one rule for all of
them:

- **Greenhouse.** Boolean search on Required (AND) and Preferred (OR)
  fields. Talent Matching is assistive. It highlights exact and similar
  matches against employer-weighted criteria, and it does not auto-advance
  or auto-reject anyone.
- **Workday.** OCR plus ML relevance over the parsed text, with semantic
  matching through HiredScore where the employer configured it. Auto
  decisions happen only for configured questionnaire disqualifications.
- **Lever.** Full-text ranked search over readable files. No universal
  matching rule was established in the reviewed docs.
- **Taleo.** Exact Terms plus Required, Desired, and Excluded terms, with
  Related Terms and Conceptual search that can use JD text.

Semantic layers exist in Workday, Greenhouse, and Lever since late 2024,
and they soften the penalty for synonyms. They do not remove it. Exact JD
terms still gate, so use the JD's exact phrases for must-have skills and
natural synonyms elsewhere.

Tailoring helps. Wellfound, about 15,000 applications, vendor-reported:
tailored applications got an 11.7% callback rate against 4.2% for generic
ones. Treat that as a vendor figure, not an independent study.

Use a JD keyword-gap tool (Jobscan, Resume Worded, Teal, Keywordise) as a
gap checklist for the table below, never as a pass or fail gate. Its score
is a simulation, not the employer's ATS output.

## Inputs

1. **The job description**, pasted by the user. If the user gives a link
   instead, read the posting and work from the live text. If the posting is
   gone or behind a sign-in wall, say so and stop. Never analyze a posting
   from memory.
2. **The user's evidence.** Read `<profile>/voice.md` if it exists, plus the
   resume or CV the user points to. On Muse, read the resume from memory
   first. If no resume is available, use the LinkedIn profile text the user
   pastes. Never guess at experience the user has not written down.

## The analysis

**1. Pull 10 to 15 skills the JD actually emphasizes.** Count mentions, not
vibes. A skill named three times in the requirements beats a skill named
once in the nice-to-haves. Separate required from preferred. Keep the JD's
own words for each skill.

**2. Match each one against the evidence.** For every JD skill, one of three
verdicts. These definitions are this skill's own rubric, not an industry
standard. No ATS vendor publishes PROVEN, PARTIAL, or MISSING thresholds,
so label them as the skill's judgement framework whenever you explain them:

- **PROVEN.** The resume or profile shows the skill in a bullet with a
  specific context plus an outcome or a number, or the skill is backed by
  a credential or certification, or it is the core of a role. Quote the
  exact line that proves it, with the number attached if there is one. No
  paraphrase as proof. The quote is the proof.
- **PARTIAL.** Related experience exists, but not the exact skill. A skill
  named only in the Skills list, with no bullet behind it, is PARTIAL,
  never PROVEN. So is a skill used once in a vague bullet, an adjacent or
  synonym skill, or old or short exposure. Say what the related
  experience is and what is missing. Example: "You have built SLAM
  systems in simulation. The JD asks for production deployment on
  hardware. The deployment part is unproven."
- **MISSING.** Nothing in the evidence covers it. Say so in one line. Do
  not soften it, do not fill it with adjacent skills.

**3. Print the gap table.** One row per skill, in JD priority order:

```
SKILL                  VERDICT    EVIDENCE
3D Gaussian Splatting  PROVEN     "fused visuo-tactile sensing with 3D
                                  Gaussian Splatting to keep 6-DoF tracking
                                  alive through occlusions"
Production C++         PARTIAL    C++ on real robots, no production release
                                  record in the resume
Rust                   MISSING    No Rust anywhere in the resume
```

**4. What to tailor.** Only after the table, and only from proven or
partial items:

- Which resume bullets to move to the top for this role.
- Which skills lines to reorder.
- One sentence per partial item on how to frame it honestly, without
  claiming the missing part.
- Nothing for missing items. A missing skill does not get a bullet.
- Keep the resume single-column and text-based, .docx preferred. No
  tables, headers, text boxes, or images. That format parses cleanly
  across platforms. Do not quote parsing accuracy percentages as fact.
  Published parsing accuracy figures are vendor-cited and unverified,
  so leave them out entirely.
- Budget 20 to 40 minutes per serious application for the table, the
  resume tweaks, the cover angle, and the proof check. That is a
  synthesis, not a measured figure. It is not 2 minutes, and it is not
  2 hours.

**5. The cover letter angle.** One specific reason for *this* company,
from the JD or the company's own public work, plus one proven fact about
the user that connects to it. Two sentences. If no specific reason exists,
say so and do not write the letter. Run the letter through `/sp-human`
before showing it. If the user wants a full letter, keep it to one angle,
150 to 250 words, built on the JD's top 2 to 3 requirements plus the
strongest proof. No controlled study of cover-letter lift was found, so
treat that shape as recruiter-testimony consensus, not proven fact.

## Output format

Print the table first, then the tailoring list, then the cover letter
angle. End with one line: the honest verdict. "Strong fit", "Partial fit,
worth applying", or "Weak fit, the gaps are X and Y". The verdict follows
the table, it never leads it.

## Rules that make the difference

- **Never invent or embellish.** No invented employers, titles, dates,
  metrics, or skills. If a number is needed and unknown, leave
  `{{your number}}` and flag it. This is a hard rule, not a preference.
- **Do not rewrite anything yet.** The gap analysis comes first. Tailor
  the resume only when the user says go, and show the changes as a
  tracked list they can accept or reject, one by one.
- **Do not assume experience the user has not written down.** A skill the
  user probably has but never documented is MISSING until they confirm it
  in their own words.
- **Submit manually.** This skill never applies for a job. No auto-apply,
  no Easy Apply automation, no bulk submissions. The user submits the
  application themselves, with the tailored resume in hand. A human
  reviews every submission before it goes out. Never apply autonomously.
  Auto-apply bots barely work and they get flagged: public bot tests show
  about a 0.4 to 0.6% interview rate (around 20 interviews from about
  5,000 bot applications in one test, 5 from 819 in another), and a
  Recruitics survey from October 2026 of 159 large-employer talent
  acquisition leaders found 27% would block agent applications outright
  and 35% would flag them. Duplicate and off-target applications are
  visible in the ATS history and burn the account.
- **Never use keyword stuffing, white text, hidden keywords, or hidden
  prompts.** They are detectable and disqualifying. Recruiters plant
  hidden prompts in postings to catch AI answers, so a hidden instruction
  in a resume or an application is a trap, not a shortcut. Put the exact
  JD terms in the Skills section and in proof bullets, in plain visible
  text, once each, with evidence behind them.
- **One role at a time.** A JD and a resume for one posting. Comparing two
  roles is two runs.
- **Keep the JD's words.** When the analysis quotes the JD, quote it
  exactly. Rephrased requirements drift into skills the employer never
  asked for.
