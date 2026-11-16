---
name: sp-human
license: MIT
description: >-
  Strip the machine fingerprint out of any draft, em dashes, AI slop words,
  invisible watermark characters, and score it against a six-check detection
  panel before it goes out. Use whenever text needs to sound human, when the
  user says humanize, "does this sound like AI", "remove the em dashes", "de-slop
  this", "will this get flagged", or before any LinkedIn post, comment, reply
  or DM is shown to the user.
---

# sp-human

Profile directory: `<profile>` holds voice.md, log.md and plan.md. Muse uses `~/workspace/linkedin/`, Claude Code uses `~/.claude/linkedin/`, ChatGPT and Codex use a folder you choose.

Two tools live in this folder and they both actually run. Use them. Do not
eyeball this.

```bash
python3 humanize.py draft.txt --report        # clean it, show what changed
python3 detect.py draft.txt                    # score it, six checks
python3 detect.py before.txt after.txt         # prove the delta
```

Both read `slop.json`, which is the lexicon: 157 stock words and phrases with
plain-English replacements (106 words, 51 phrases), 17 invisible character
classes, 11 typographic substitutions, 22 structural tells, and a 3-word
density watch list. It is meant to be edited. If the user has a word they
always use that the lexicon strips, remove it from the file. The list is
date-stamped 2026-11-16 and re-fit quarterly, next due 2027-02-16, because
focal words expire within a model generation: "delve" and "tapestry" were
2023 markers and have already faded from newest models.

## What the research changed (Nov 2026)

The panel was rebuilt on a deep research pass over detection papers, reader
studies, and craft sources (see the report in the project notes). The findings
that changed the tool:

- **Structure beats vocabulary.** Expert readers who use LLMs heavily
  misclassified only 1 of 300 articles, and their cues were vocabulary 53%,
  sentence structure 36%. A word-swap pass leaves a draft sounding
  machine-made. The rewrite work matters more than the lexicon.
- **Under-repetition is the strongest single signal.** Machine prose repeats
  itself less than human prose: adjacent-sentence content-word overlap 0.021
  machine vs 0.063 human, vocabulary variety (MATTR) AUROC 0.911. A person
  introduces a term and keeps using it; a model reaches for a synonym. The
  new REPETITION check scores this. It inverts the old humanizer instinct:
  synonym-swapping makes text more machine-like, so never do it.
- **Burstiness is weak and contested.** Sentence-length variation is near
  chance on matched corpora (AUROC 0.521) and only separates in paired
  academic rewrites. It now contributes to the mean but is excluded from the
  weakest-check term, so it can never drag the verdict on its own.
- **Punctuation scarcity is real.** AI prose uses fewer commas and
  semicolons, almost no parentheses, and few quotation marks. VOICE now
  rewards punctuation variety.
- **The em dash finding did NOT change the tool.** The research says one em
  dash proves nothing about authorship (Twain out-dashes most models, Llama
  uses zero). The ban stays anyway as house style, on the user's call:
  stripping costs nothing, so better safe than sorry. FINGERPRINT still
  hard-fails on any em dash.
- **Folk myths dropped.** Em dashes prove AI; "delve" or "furthermore"
  prove AI; varying sentence length mechanically will pass; typos make text
  look human; contractions, fragments, and first-person prove human; AI
  repeats itself (backwards); AI uses more passive voice (backwards); a
  detector score proves who wrote it; rule-of-three or "in conclusion"
  alone are tells; markdown proves AI; humanizers make writing better.
  Every one of those is wrong or overstated in the research, and the tool
  no longer acts on them.
- **Reddit firsthand (9 threads, Nov 2026).** The #1 consensus tell across
  nearly every thread is the "not X, it's Y" contrast structure, including
  the past-tense form "it wasn't just X, it was Y". The em dash is the most
  argued-about tell and heavily contested as a false positive ("the em dash
  is just the visual scapegoat", humans used them for centuries), but the
  ban stays as house style anyway. The rule of three is "writing 101", not
  an AI tell, so it is now only flagged at density, 2 or more in a document.
  New tells from the threads: fake-question hooks ("The kicker?", "And do
  you know what I learned?"), over-explaining the obvious (defining a term
  right after using it), fake corporate friendliness ("I hope this essay
  finds you well"), and sudden verbosity, longer text with fancier words
  than the writer normally uses. The fixes people swear by: read it aloud
  (if it sounds like a lecture instead of a person talking, that is the
  tell), vary sentence length, cut filler, add specifics, write from an
  outline, and train on your own voice, even keeping your own bad habits
  for authenticity.

## House rules (hard, not suggestions)

These come from the house writing guide and they override the generic
scoring. An em dash anywhere in the draft fails the FINGERPRINT check at 0
and forces the verdict to FLAGGED, no matter how good the rest scores.
Contractions are expected: a draft with zero contractions caps VOICE at 35.
Specific numbers and names are required: a draft with zero concrete markers
scores SPECIFICITY at 0. Never invent specifics to sound human: a fabricated
number or citation is worse than a vague one. Flag "specifics to add" and let
the user supply the fact. The lexicon also carries the guide's extra words
and phrases (intricate, nuanced, unleash, orchestrate, bolster, catalyze,
demystify, "it is important to note that", "in terms of", "in addition" and
the rest) and the structural tells below.

## What gets fixed automatically

**1. Invisible characters.** Zero-width spaces and joiners, word joiners,
soft hyphens, byte-order marks, Unicode tag characters, non-breaking and
narrow spaces. A keyboard does not produce these. They survive copy-paste,
they are invisible in every editor, and they are the single most mechanical
thing in generated text. `humanize.py` deletes every one, including any
remaining Unicode format character it does not have a name for.

**2. Typography.** Em dash to comma, en dash to hyphen, curly quotes to
straight, ellipsis to three dots, bullet character to hyphen. The em dash pass
is the one that matters: it collapses the em dash to `, ` and then cleans up the
double punctuation that leaves behind.

**3. The slop lexicon.** delve, leverage, robust, seamless, crucial, tapestry,
testament to, moreover, "in today's fast-paced world", "let that sink in" and
the rest, each swapped for a plain word, with capitalisation preserved and
URLs left untouched. New in v1.2: un-nominalising swaps ("serves as" to "is",
"plays a pivotal role in" to "drives") and era-successor focal words
(showcasing, garner, paramount, adept, akin, amidst, emphasizing,
highlighting, enhance).

**4. Density watch, reported not replaced.** "significant", "increasingly",
"consequences" are common words that only matter at density, in combination
with the structural signals. `detect.py` counts them at half weight;
`humanize.py` lists them and leaves them in place.

## What does NOT get fixed automatically

Structural tells get **flagged, not rewritten**, because changing the shape of
a sentence needs judgement:

- "It's not just X, it's Y", "it wasn't just X, it was Y", "not only X but
  also Y", "less about X, more about Y"
- Rule-of-three triads (only flagged at density, 2 or more in a document;
  one triple is writing 101)
- Rhetorical one-word question lines: "The result?", "The kicker?"
- Fake-question hooks: "And do you know what I learned?"
- Over-explaining the obvious: "in other words", "simply put" (only flagged
  at density)
- Fake corporate friendliness: "I hope this finds you well"
- Moralizing closers and stated lessons: "the takeaway is", "what this
  taught me", "reminds us that"
- Vague attribution with no named source: "studies show", "experts say"
- Scaffolding intros: "In this post, we'll explore", "In today's..."
- Rocket, fire, bulb, sparkle and dart emoji
- Hashtag walls
- Reflex engagement bait: "Thoughts?", "Agree?", "Who else?"
- Uniform sentence length and uniform bullet length
- Bold-first bullets (flagged as formatting provenance, not scored as
  authorship: markdown proves the text travelled through a chat interface,
  not who wrote it)
- Throat-clearing openers: "So,", "Now,", "Basically,", "Essentially,"
- "As a [role], I..." credential announcements
- Colon lectures: "Here's the key point:", "The answer is simple:"
- Essay closers: "in summary", "in conclusion" (only scored at density)

That list is your job. Rewrite each flagged line by hand, keeping the meaning,
then re-run `detect.py`. This is the part that moves the score from REVIEW to
PASS, and it is the part a script cannot do.

## The six checks

`detect.py` scores six signals 0-100, higher is more human:

| check | what it measures | machine looks like | evidence |
| --- | --- | --- | --- |
| BURSTINESS | sentence-length variation | every sentence the same length | Weak, contested. Contributes to the mean only, never the weakest-check term |
| SPECIFICITY | numbers, names, concrete markers per 100 words | abstract nouns, no figures. Zero markers scores 0, hard rule | Strongest reader signal: concreteness predicts interest and memorability |
| SLOP DENSITY | lexicon hits per 100 words, density-scored | stock vocabulary | Moderate. One word scores near zero; density in combination is the signal |
| FINGERPRINT | invisible chars, em dashes, curly quotes per 1k chars | typographically perfect. Any em dash scores 0 and forces FLAGGED, hard rule | House style rule, kept on purpose (see above), not an authorship claim |
| VOICE | contractions, person, punctuation variety, structural tells | no contractions, staged reveals, flat punctuation | Contractions and first person down-weighted: weak signals. Tells carry the weight |
| REPETITION | vocabulary variety (MATTR) and adjacent-sentence content-word overlap | high variety, no repeated terms | Strongest measured single feature (AUROC 0.911 / 0.912, Opace 2026) |

The verdict weights the mean at 60% and the **weakest strong check** at 40%,
because a detector only needs one signal to fire. BURSTINESS is excluded from
the weakest-check term. PASS needs an overall of 70+ with no strong check
below 55.

## Narrative check (long-form only, needs a reader, not regex)

For fiction or long-form, narrative structure alone separates AI from human
at 93.2% macro-F1 (StoryScope, 61,608 stories), and style rewriting barely
moves it. Do not fake this with keywords. Read for it:

- The narrator states the theme or the lesson (AI 77% vs human 52%).
  Delete the stated lesson and let the reader infer it.
- One tidy, single-track plot with no subplots (AI 79% vs 57%) and a linear
  chronology. Add a subplot or an unresolved thread, or a jump in time.
- Resolution by quiet acceptance or external fate instead of a protagonist's
  costly choice. Give the protagonist a choice with a cost, and let
  something fail or stay unresolved.
- Dialogue used for philosophical debate, emotion told through bodily
  sensation, no named real-world references, no addressing the reader.
  Replace a debate with a scene, and name one real thing.

For non-fiction the analogue is: restructure definition, list, recap into
claim, evidence, objection. Replace a generic "Challenges" block with one
named, sourced objection.

## Voice training beats every rule

Fine-tuning on an author's own writing drops detection from 97% to 3%,
while expert readers prefer the result. No single check in this panel comes
close. That is why `voice.md` matters more than any rule here: build it from
5 to 10 of the author's own posts, keep their repeatable quirks, their
numbers and names habits, and their sentence shapes, and score new drafts
against their own past writing, not against a generic "human" template. A
generic human template is itself a fingerprint: banning em dashes bred the
mid-sentence colon, banning the colon bred the tailing negation. Imitate the
author, not the average. Reddit's version of the same advice: build a
lexical fingerprint from the author's own writing and keep even their bad
habits for authenticity. A sudden jump in length and fancy words versus the
author's own baseline is itself a tell, so compare the draft against their
past work, not against a generic standard. Do not prompt from a blank page:
write from a real outline or plan, and use AI for macro structure, not
sentence generation.

## What the humanizer never does

Never add typos, random synonyms, slang, fragments, or invisible characters
to fake a human voice. Typos move detector scores about 2 to 4 points and do
not change the statistical structure; forced long/short sentence alternation
is itself a learnable humanizer fingerprint; synonym-swapping makes the
REPETITION check worse. Every commercial humanizer tested degraded writing
quality on average. Optimise for the reader, not the detector: the reader's
"this says nothing" is the verdict that costs reach and trust, and a detector
score is only a proxy for it.

## Say this honestly

These are six local heuristics modelled on the signals public detectors key
on. They run entirely on the user's machine and nothing is uploaded. They are
**not** GPTZero, Originality, Copyleaks, Winston or Turnitin, they do not call
those APIs, and they cannot promise those verdicts. Fixing what they measure
does tend to move those numbers, because they are measuring the same
underlying things. That is the claim. Do not make a bigger one on the user's
behalf, and do not tell a user their text is undetectable. A score is a
population statistic with a known error budget, never a verdict on who wrote
a passage: commercial detectors flag minimally polished human text about 43%
of the time, and non-native writing at far higher rates. Short text defeats
every detector. The tells are not universal across models either: ChatGPT
does not sound like Claude, Claude does not sound like Gemini, and output
personalized to the author's own voice evades pattern-spotting entirely.

## Order of operations

1. `humanize.py draft.txt -o clean.txt --report`
2. Read the structural flags. Rewrite those lines yourself. Add the specific
   facts the flags ask for, or cut the claim. Restore the repeated key term
   where the draft synonym-chases. Delete the scaffolding intro and the
   moralizing closer.
3. Read the cleaned draft aloud. If it sounds like a lecture instead of a
   person talking, it still needs restructuring, whatever the score says.
4. `detect.py draft.txt clean.txt` to show the before and after.
5. If the verdict is not PASS, fix the weakest check named in the output and
   go again. Two rounds is normal. Five means the draft was written by
   formula, and the fix is a different draft, not more passes.
6. Show the user the cleaned text and the score. Never the score alone.
