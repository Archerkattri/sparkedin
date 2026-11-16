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
verdicts:

- **PROVEN.** The resume or profile shows it. Quote the exact line that
  proves it, with the number attached if there is one. No paraphrase as
  proof. The quote is the proof.
- **PARTIAL.** Related experience exists, but not the exact skill. Say what
  the related experience is and what is missing. Example: "You have built
  SLAM systems in simulation. The JD asks for production deployment on
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

**5. The cover letter angle.** One specific reason for *this* company,
from the JD or the company's own public work, plus one proven fact about
the user that connects to it. Two sentences. If no specific reason exists,
say so and do not write the letter. Run the letter through `/sp-human`
before showing it.

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
  application themselves, with the tailored resume in hand.
- **One role at a time.** A JD and a resume for one posting. Comparing two
  roles is two runs.
- **Keep the JD's words.** When the analysis quotes the JD, quote it
  exactly. Rephrased requirements drift into skills the employer never
  asked for.
