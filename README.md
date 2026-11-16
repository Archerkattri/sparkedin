# Sparkedin

**Thirteen LinkedIn skills that do the work. Free, MIT licensed, no signup, no API key.**

Sparkedin turns your AI agent into your LinkedIn operator. It writes your posts, comments on the right threads, replies under your own posts, runs outreach campaigns, scores your profile, plans your week, and pulls your own stats. Every word goes out in your voice, and nothing goes out without your say-so.

Built for Muse first. Also works with Claude Code, ChatGPT, and Codex.

## What it does

- **Write.** One idea becomes a post built on 21 proven hook formulas, with three hook options and a full draft.
- **Engage.** Comments that add something real, replies that sort the signal from the noise, and an inbox triaged into leads, recruiters, peers, and spam.
- **Reach out.** Full campaigns. Pick the path first, then the note, the DM, two follow-ups, and the thank-you when they accept. Every target tracked.
- **Measure.** Your profile scored out of 100 with fixes in order, your past posts ranked by what actually worked, and your own engagement pulled into JSON and a dashboard.
- **Sound like you.** Every word passes through the humanizer first. It strips invisible characters, stock phrasing, and the tells that make generated text read as generated, then scores the result before it goes out.

## The thirteen

| Command | What it does |
| --- | --- |
| `/sp-post` | One idea into a post. Three hook options from [21 formulas](skills/sp-post/hooks.json), one full draft, humanized, then posted when you say go. |
| `/sp-comment` | Comments on other people's posts. Nine types, picked by what the post actually is. Never "Great post!". |
| `/sp-reply` | The thread under your own post. Sorts every comment into lead, substance, peer, support, or noise, then replies in that order. |
| `/sp-profile` | Scores your profile against a [12-part rubric](skills/sp-profile/rubric.json) out of 100, then rewrites in fix-first order. |
| `/sp-plan` | The week. What to post, when to post it, and the 10 people to engage with. Writes `<profile>/plan.md`. |
| `/sp-human` | The humanizer. Two scripts that actually run. See below. |
| `/sp-carousel` | Document posts. Slide-by-slide copy, the cover that earns the swipe, and the PDF to upload. |
| `/sp-repurpose` | One video, newsletter, or transcript into a week of posts that each stand alone. |
| `/sp-dm` | The 200-character invite note, the first message, and the two follow-ups. |
| `/sp-outreach` | A whole outreach campaign. Picks the path first, then writes the note, the DM, the thank-you, and the two follow-ups, and tracks every target in `<profile>/outreach.md`. |
| `/sp-inbox` | Triages the inbox into lead, recruiter, peer, ask, or spam, and tells you which tell gave the sequence away. |
| `/sp-audit` | Post-mortem on what you have already published. Ranks by engagement rate and reach multiple, not impressions. |
| `/sp-stats` | Your own posts and engagement into local JSON, plus a dashboard. Experimental: LinkedIn internals change without notice. |

## The humanizer

`/sp-human` ships two Python scripts with no dependencies. They run on your machine, on your text, and nothing is uploaded.

```bash
python3 humanize.py draft.txt --report      # clean it, show every change
python3 detect.py draft.txt                  # score it, five checks
python3 detect.py before.txt after.txt       # prove the delta
```

**Cleaned automatically:**

- **Invisible characters.** Zero-width spaces and joiners, word joiners, soft hyphens, byte-order marks, Unicode tag characters, non-breaking and narrow spaces. Your keyboard does not make these. They survive copy-paste and they are invisible in every editor you own.
- **Typography.** Em dash to comma, en dash to hyphen, curly quotes to straight, ellipsis to three dots.
- **The lexicon.** 136 stock words and phrases with plain-English replacements, with capitalisation preserved and URLs untouched. It lives in [`slop.json`](skills/sp-human/slop.json) and it is meant to be edited. The house writing-guide rules are baked in: any em dash is a hard fail, zero contractions caps the voice check, and a draft with no numbers or names scores zero on specificity.

**Flagged instead of fixed:** "It's not just X, it's Y", rule-of-three triads, one-word rhetorical questions, hashtag walls, reflex engagement bait, uniform sentence length. Changing the shape of a sentence needs judgement, so those are handed back for a rewrite rather than mangled by a regex.

**The five checks**, scored 0 to 100, higher is more human:

| Check | What it measures |
| --- | --- |
| BURSTINESS | Sentence-length variation. Models write even. |
| SPECIFICITY | Numbers, names, and concrete markers per 100 words |
| SLOP DENSITY | Lexicon hits per 100 words |
| FINGERPRINT | Invisible characters, em dashes, and curly quotes per 1,000 |
| VOICE | Contractions, person, and structural tells |

The verdict weights the mean at 60% and the **weakest single check** at 40%, because a detector only needs one signal to fire.

## Get started

### Muse

```bash
git clone https://github.com/Archerkattri/sparkedin.git
cp -r sparkedin/skills/sp-* ~/workspace/custom-skills/
```

A router skill for Muse installs ships at the repo root. See `muse-install/`.

### Claude Code

```bash
git clone https://github.com/Archerkattri/sparkedin.git
cp -r sparkedin/skills/sp-* ~/.claude/skills/
```

Or as a plugin:

```
/plugin marketplace add Archerkattri/sparkedin
/plugin install sparkedin
```

Project-local instead of global: copy the same folders into your repo's `.claude/skills/`.

### ChatGPT

Upload the skill folder, or a zip of it, through Plugins, Skills, Create, Upload from your computer. Each skill carries `agents/openai.yaml` with its display name and starter prompt. ChatGPT reads the same `SKILL.md` as everyone else.

### Codex

Copy the skills into `.agents/skills/` in your repo or `~/.agents/skills/`. Same files, same format.

### First, your voice

Spend ten minutes on `templates/voice.md`. Copy it to your profile directory and fill it in, or paste three of your own posts into your agent and say "write my voice.md from these". Every skill reads that file. Skip it and everything comes out sounding like everyone else.

On Muse, the agent reads your voice from its memory first and only falls back to voice.md.

Your voice, log, and plan live in one profile directory, resolved per host:

- Muse: `~/workspace/linkedin/`
- Claude Code: `~/.claude/linkedin/`
- ChatGPT and Codex: a folder you choose

Skill files refer to it as `<profile>`.

## About

Most LinkedIn tools stop at a draft. Sparkedin finishes the job. It was built to close the gap between "your agent wrote it" and "it went out", without handing your voice over to a template. The skills execute through your agent's own tools, so a post, an invite, or a DM only moves when you say go, and your agent's own approval flow is the gate.

Sparkedin is built and maintained by Krishi Attri. It started as a fork of the LinkedIn agent skill by Jake Schincariol, and grew into a full pack: an execution model instead of drafts only, a portable profile directory, ChatGPT sidecars, a Muse router, a campaign-level outreach skill, and an own-account stats skill.

## A few honest notes

- **Your agent's approval flow is the gate.** There is no separate draft-only mode and no pace cap in the skill itself.
- **LinkedIn restricts accounts for high-volume automated activity.** If your account gets restricted, pace is the likely cause.
- **The five checks are local heuristics, not detector APIs.** They are modelled on the signals public detectors key on, and they run entirely on your machine. They are not GPTZero, Originality, Copyleaks, Winston, or Turnitin, they do not call those services, and they cannot promise those verdicts. Fixing what they measure tends to move those numbers, because they are measuring the same underlying things.
- **The invisible-character pass is real and it is narrow.** It removes the zero-width and format characters that end up in generated text and survive a copy-paste. That is a genuine, checkable fingerprint. It is not a claim about defeating a cryptographic watermarking scheme, and this repo does not make one.
- **Nothing here fabricates.** No invented metrics, clients, or outcomes go under your name. If a draft needs a number you have not given, it comes back with `{{your number}}` in it and a flag, every time.

## Credit

Sparkedin is a fork of the LinkedIn agent skill by Jake Schincariol, [opusjake.ai](https://opusjake.ai), MIT licensed. The original is at [github.com/Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill). The execution model, the portable profile directory, the ChatGPT sidecars, the Muse router, the outreach skill, and the stats skill are new here. The hooks, the humanizer scripts, the lexicon, and the rubric are his.

## License

MIT.
