# Sparkedin

Thirteen LinkedIn skills that do the work. Free, MIT, no signup, no API key,
nothing to connect.

One of them writes your posts off 21 hook formulas. One comments on other
people's posts. One handles the replies under yours. One scores your profile
out of 100 and rewrites what lost points. One plans the week: what to post,
when, and who to engage with. One runs a whole outreach campaign, path first.
One pulls your own stats into JSON and a dashboard.

And one is the humanizer, which is the reason the rest are usable. It strips
the em dashes, the slop vocabulary and the invisible watermark characters out
of a draft, then scores what is left against a five-check detection panel
before it goes out.

**This skill executes.** Unlike the pack it forked from, Sparkedin does not
stop at a draft. When you say go, it posts the post, sends the invite, sends
the DM, through your agent's own tools. The only gate is your agent's own
approval flow: Muse asks on an approval card, ChatGPT and Claude ask in their
own way. There are no caps and no draft-only rule in the skill itself.

## Install

### Muse

Copy this repo's `skills/` tree into your custom skills, or clone it and point
Muse at it:

```bash
git clone https://github.com/Archerkattri/sparkedin.git
cp -r sparkedin/skills/sp-* ~/workspace/custom-skills/
```

The pack also ships a router skill at the repo root for Muse installs; see
`muse-install/`.

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

Project-local instead of global: copy the same folders into your repo's
`.claude/skills/`.

### ChatGPT

Upload the skill folder (or a zip of it) through Plugins, Skills, Create,
Upload from your computer. Each skill carries `agents/openai.yaml` with its
display name and starter prompt. ChatGPT reads the same `SKILL.md` as
everyone else.

### Codex

Copy the skills into `.agents/skills/` in your repo or `~/.agents/skills/`.
Same files, same format.

Then spend ten minutes on `templates/voice.md`. Copy it to your profile
directory and fill it in, or paste three of your own posts into your agent
and say "write my voice.md from these". Every skill reads that file. Skip it
and everything comes out sounding like everyone else.

On Muse, the agent reads your voice from its memory first and only falls
back to voice.md.

## The profile directory

Voice, log and plan live in one profile directory, resolved per host:

- Muse: `~/workspace/linkedin/`
- Claude Code: `~/.claude/linkedin/`
- ChatGPT and Codex: a folder you choose

Skill files refer to it as `<profile>`.

## The thirteen

| command | what it does |
| --- | --- |
| `/sp-post` | One idea into a post. Three hook options from [21 formulas](skills/sp-post/hooks.json), one full draft, humanized, then posted when you say go. |
| `/sp-comment` | Comments on other people's posts. Nine types, picked by what the post actually is. Never "Great post!". |
| `/sp-reply` | The thread under your own post. Sorts every comment into lead / substance / peer / support / noise, then replies in that order. |
| `/sp-profile` | Scores your profile against a [12-part rubric](skills/sp-profile/rubric.json) out of 100, then rewrites in fix-first order. |
| `/sp-plan` | The week. What to post, when to post it, and the 10 people to engage with. Writes `<profile>/plan.md`. |
| `/sp-human` | The humanizer. Two scripts that actually run. See below. |
| `/sp-carousel` | Document posts. Slide-by-slide copy, the cover that earns the swipe, and the PDF to upload. |
| `/sp-repurpose` | One video, newsletter or transcript into a week of posts that each stand alone. |
| `/sp-dm` | The 200-character invite note, the first message, and the two follow-ups. Two. |
| `/sp-outreach` | A whole outreach campaign. Picks the path first, then writes the note, the DM, the thank-you and the two follow-ups, and tracks every target in `<profile>/outreach.md`. |
| `/sp-inbox` | Triages the inbox into lead / recruiter / peer / ask / spam, and tells you which tell gave the sequence away. |
| `/sp-audit` | Post-mortem on what you have already published. Ranks by engagement rate and reach multiple, not impressions. |
| `/sp-stats` | Your own posts and engagement into local JSON, plus a dashboard. Experimental: LinkedIn internals change without notice. |

## The humanizer

`/sp-human` ships two Python scripts with no dependencies. They run on your
machine, on your text, and nothing is uploaded.

```bash
python3 humanize.py draft.txt --report      # clean it, show every change
python3 detect.py draft.txt                  # score it, five checks
python3 detect.py before.txt after.txt       # prove the delta
```

**What comes out automatically:**

- **Invisible characters.** Zero-width spaces and joiners, word joiners, soft
  hyphens, byte-order marks, Unicode tag characters, non-breaking and narrow
  spaces. Your keyboard does not make these. They survive copy-paste and they
  are invisible in every editor you own.
- **Typography.** Em dash to comma, en dash to hyphen, curly quotes to
  straight, ellipsis to three dots.
- **The lexicon.** 136 stock words and phrases with plain-English
  replacements - delve, leverage, robust, seamless, crucial, testament to, "in
  today's fast-paced world", "let that sink in" - with capitalisation preserved
  and URLs untouched. It lives in
  [`slop.json`](skills/sp-human/slop.json) and it is meant to be edited. The
  house writing-guide rules are baked in: any em dash is a hard fail, zero
  contractions caps the voice check, and a draft with no numbers or names
  scores zero on specificity.

**What gets flagged instead of fixed:** "It's not just X, it's Y", rule-of-three
triads, one-word rhetorical questions, hashtag walls, reflex engagement bait,
uniform sentence length. Changing the shape of a sentence needs judgement, so
those are handed back for a rewrite rather than mangled by a regex.

**The five checks**, scored 0-100, higher is more human:

| check | what it measures |
| --- | --- |
| BURSTINESS | sentence-length variation. Models write even. |
| SPECIFICITY | numbers, names and concrete markers per 100 words |
| SLOP DENSITY | lexicon hits per 100 words |
| FINGERPRINT | invisible characters, em dashes, curly quotes per 1,000 |
| VOICE | contractions, person, structural tells |

The verdict weights the mean at 60% and the **weakest single check** at 40%,
because a detector only needs one signal to fire.

## The fine print, which is the honest part

**These skills execute through your agent, and your agent's approval flow is
the gate.** There is no separate draft-only mode and no pace cap in the
skill. One fact to know: LinkedIn restricts accounts for high-volume
automated activity, so if your account gets restricted, pace is the likely
cause.

**The five checks are local heuristics, not detector APIs.** They are modelled
on the signals public detectors key on, and they run entirely on your machine.
They are not GPTZero, Originality, Copyleaks, Winston or Turnitin, they do not
call those services, and they cannot promise those verdicts. Fixing what they
measure tends to move those numbers, because they are measuring the same
underlying things. That is the whole claim. Nobody can honestly sell you
"undetectable", and anybody who does is selling you something.

**The invisible-character pass is real and it is narrow.** It removes the
zero-width and format characters that end up in generated text and survive a
copy-paste. That is a genuine, checkable fingerprint. It is not a claim about
defeating a cryptographic watermarking scheme, and this repo does not make
one.

**Nothing here fabricates.** No invented metrics, clients or outcomes go under
your name. If a draft needs a number you have not given, it comes back with
`{{your number}}` in it and a flag, every time.

## Files

```
skills/sp-post/hooks.json        21 hook formulas: template, example, what it is for, how it gets ruined
skills/sp-human/slop.json        the lexicon: 136 terms, 17 invisible classes, 15 structural tells
skills/sp-human/humanize.py      the three cleaning passes
skills/sp-human/detect.py        the five-check panel, with the house hard rules
skills/sp-profile/rubric.json    the 100-point profile score
skills/sp-outreach/              the campaign skill: path table, notes, DMs, thank-yous, tracker
skills/sp-stats/                 the own-account stats scrape: posts, reactors, commenters, meta
skills/sp-*/agents/openai.yaml   ChatGPT display name, starter prompt, invocation policy
templates/voice.md               your voice profile. Fill this in first.
muse-install/                    router skill for Muse custom-skills installs
```

## Credit

Sparkedin is a fork of the LinkedIn agent skill by Jake Schincariol,
[opusjake.ai](https://opusjake.ai), MIT licensed. The original is at
[github.com/Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill).
The execution model, the portable profile directory, the ChatGPT sidecars and
the Muse router are new here. The hooks, the humanizer scripts, the lexicon
and the rubric are his.

## License

MIT. Take it, change it, ship it.
