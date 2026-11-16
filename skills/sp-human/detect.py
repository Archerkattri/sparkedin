#!/usr/bin/env python3
"""
detect.py - a six-check panel that scores how machine-written a draft looks.

What this is: six local heuristics modelled on the signals public AI
detectors actually measure, rebuilt on the November 2026 humanizer research:
under-repetition (the strongest single feature found, Opace 2026), sentence
structure, concreteness, stock vocabulary, typographic fingerprint, and
voice. Every score is computed on your machine from the text alone. Nothing
is uploaded.

What this is NOT: GPTZero, Originality, Copyleaks, Winston or Turnitin.
It does not call their APIs and it cannot promise their verdict. It catches
the things they all key on, which is why fixing them tends to move their
numbers too - but the only honest claim is the one on this line. A score is
a population statistic, not a verdict on who wrote a passage. Commercial
detectors flag minimally polished human text about 43% of the time and
non-native writing far more often, so never present a score as authorship
evidence.

Hard rules from the house writing guide: any em dash fails FINGERPRINT and
forces the verdict to FLAGGED, and humanize.py strips em dashes. The
research says one em dash proves nothing about authorship (Twain out-dashes
most models), but the ban stays as house style: stripping costs nothing,
so better safe than sorry. Zero contractions caps VOICE at 35; zero numbers
or names scores SPECIFICITY at 0.

BURSTINESS is a weak, contested signal (Opace AUROC 0.521, near chance on
matched corpora; TextPulse finds a real effect only in paired academic
rewrites). It contributes to the mean but is excluded from the weakest-check
term, so it can never drag the verdict on its own.

Each check returns a HUMAN score from 0 to 100. Higher is better.

Usage
  python3 detect.py draft.txt
  pbpaste | python3 detect.py -
  python3 detect.py draft.txt --json
  python3 detect.py before.txt after.txt      # compare two drafts
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[A-Za-z']+")
CONTRACTIONS = re.compile(r"\b\w+'(?:s|t|re|ve|ll|d|m)\b", re.IGNORECASE)
PRONOUNS = re.compile(r"\b(i|me|my|mine|we|us|our|you|your)\b", re.IGNORECASE)
NUMBERS = re.compile(r"\b\d[\d,.]*%?\b|\$\d")
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", re.MULTILINE)

# Function words, for content-word overlap: what is left after removing
# these is what a writer actually repeats or synonym-chases.
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "so", "as", "at",
    "by", "for", "in", "of", "on", "to", "with", "from", "is", "are", "was",
    "were", "be", "been", "being", "it", "its", "this", "that", "these",
    "those", "i", "we", "you", "he", "she", "they", "my", "our", "your",
    "his", "her", "their", "me", "us", "him", "them", "have", "has", "had",
    "do", "does", "did", "will", "would", "can", "could", "should", "not",
    "no", "yes", "very", "just", "also", "more", "most", "some", "any",
    "all", "each", "one", "two", "when", "where", "how", "what", "which",
    "who", "whom", "about", "into", "over", "under", "after", "before",
    "between", "through", "during", "than", "too", "only", "own", "same",
}


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Map value onto 0-100 where `human` -> 100 and `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    """Sentence-length variation. Weak and contested: see module docstring.

    TextPulse paired rewrites put human CV at 0.449 vs AI 0.376; Opace
    matched corpora put the separation near chance. Calibrated between the
    two, and excluded from the weakest-check term in the verdict.
    """
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "too short to judge"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.50, machine=0.30)
    return score, f"variation {cv:.2f} across {len(lens)} sentences (weak signal, human ~0.45)"


def check_specificity(text):
    """Numbers, names and concrete nouns. Slop is abstract."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    hits = len(NUMBERS.findall(text)) + len(set(PROPER.findall(text)))
    density = hits * per100
    if hits == 0:
        # House rule: specific numbers and names are required, not nice to have.
        return 0.0, "no numbers or names: add specific facts, figures or names"
    score = scale(density, human=6.0, machine=0.5)
    return score, f"{hits} concrete markers, {density:.1f} per 100 words (want 4+)"


def check_slop(text, lex):
    """Stock vocabulary density against the lexicon, density-scored.

    One word proves nothing (a single 'delve' scores near zero penalty);
    density in combination is the signal. Era-successor words in
    density_watch count at half weight and are never auto-replaced.
    """
    w = words(text)
    if not w:
        return 50.0, "empty"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = re.compile(r"\b" + re.escape(entry["find"]).replace(r"\ ", r"\s+") + r"\b",
                             re.IGNORECASE)
        n = len(pattern.findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    watch_hits, watch_found = 0, []
    for entry in lex.get("density_watch", []):
        pattern = re.compile(r"\b" + re.escape(entry["find"]) + r"\b", re.IGNORECASE)
        n = len(pattern.findall(text))
        if n:
            watch_hits += n
            watch_found.append(entry["find"])
    density = (hits + 0.5 * watch_hits) * 100 / len(w)
    score = scale(density, human=0.5, machine=4.0)
    detail = f"{hits} stock terms, {density:.1f} per 100 words"
    if watch_hits:
        detail += f" (density watch: {watch_hits}x {', '.join(sorted(watch_found))})"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Characters a phone keyboard does not produce.

    UNCHANGED by the research upgrade, on the user's instruction: the house
    writing guide bans em dashes, so any em dash is still a hard fail and
    forces FLAGGED. This is a style rule, not an authorship claim.
    """
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    curly = sum(text.count(c) for c in "‘’“”")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "   ")
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    detail = (f"{invisible} invisible, {em} em dash, {curly} curly quote, "
              f"{ellip} ellipsis, {nbsp} hard space")
    if em:
        # House rule: an em dash is a hard fail, not a deduction.
        return 0.0, detail + " - em dash present, hard fail"
    score = scale(per1k, human=0.0, machine=12.0)
    return score, detail


def _punctuation_index(text, per100):
    """Commas, semicolons, parentheses and quotes per 100 words.

    The Economist (55,940 sentences) found AI prose has fewer commas and
    semicolons, almost no parentheses, and few quotation marks. The fix is
    to add punctuation variety, so this rewards it. Starting calibration:
    human index ~7, machine ~4.
    """
    commas = text.count(",") * per100
    semis = text.count(";") * per100
    parens = text.count("(") * per100
    quotes = (text.count('"') + text.count("“") + text.count("”")) // 2 * per100
    index = commas + 2 * semis + 2 * parens + 2 * quotes
    return index


def check_voice(text, lex):
    """Contractions, person, punctuation variety, and the shapes models default to.

    Contractions and first-person pronouns are weak signals (Jakesch et al.:
    contractions read human but were more likely AI; first person carries no
    diagnostic signal), so they are down-weighted here and kept mainly as
    house style. The structural tells carry the most weight. Structures
    flagged density_only count only at 2+ hits; structures flagged scored
    false are formatting provenance, not authorship, and are not scored.
    """
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    contractions = len(CONTRACTIONS.findall(text)) * per100
    person = len(PRONOUNS.findall(text)) * per100
    punct = _punctuation_index(text, per100)
    tells = 0
    names = []
    provenance = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if not n:
            continue
        if s.get("scored") is False:
            provenance.append(s["id"])
            continue
        if s.get("density_only") and n < 2:
            continue
        tells += n
        names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(contractions, human=3.0, machine=0.0) * 0.20
             + scale(person, human=8.0, machine=1.0) * 0.25
             + clamp(100 - tells * 22) * 0.35
             + scale(punct, human=7.0, machine=4.0) * 0.20)
    if contractions == 0:
        # House rule: contractions are expected. Zero caps the check.
        score = min(score, 35.0)
        names.append("no-contractions")
    if uniform:
        score -= 12
        names.append("uniform-bullets")
    detail = (f"{contractions:.1f} contractions, {person:.1f} personal pronouns, "
              f"punctuation {punct:.1f} per 100 words, {tells} structural tell(s)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    if provenance:
        detail += " (formatting, not scored: " + ", ".join(provenance) + ")"
    return clamp(score), detail


def check_repetition(text):
    """Under-repetition: the strongest single feature found (Opace 2026).

    Humans re-use the same term; models reach for synonyms. MATTR in a
    100-word window: human median 0.694, machine 0.776 (AUROC 0.911).
    Adjacent-sentence content-word overlap: human 0.063, machine 0.021
    (AUROC 0.912). High variety plus low overlap reads machine-made. This
    inverts the old humanizer instinct: synonym-swapping makes text MORE
    machine-like on this feature, so never do it.
    """
    w = [t.lower() for t in words(text)]
    if len(w) < 40:
        return 50.0, "too short to judge"
    window = 50 if len(w) < 150 else 100
    ttrs = []
    for start in range(0, len(w) - window + 1, 5):
        chunk = w[start:start + window]
        ttrs.append(len(set(chunk)) / len(chunk))
    if not ttrs:
        ttrs = [len(set(w)) / len(w)]
    mattr = statistics.mean(ttrs)
    sents = sentences(text)
    overlaps = []
    prev = None
    for s in sents:
        content = {t.lower() for t in WORD_RE.findall(s)
                   if t.lower() not in STOPWORDS and len(t) > 2}
        if prev is not None and content and prev:
            union = content | prev
            overlaps.append(len(content & prev) / len(union) if union else 0.0)
        if content:
            prev = content
    overlap = statistics.mean(overlaps) if overlaps else 0.0
    # Overlap anchors are register-aware: Opace's medians (0.063 human /
    # 0.021 machine) come from long-form documents, where topic continuity
    # across sentences is higher. Short posts run lower, so short texts use
    # tighter anchors fitted to short-form human writing.
    if len(w) < 300:
        overlap_human, overlap_machine = 0.035, 0.005
    else:
        overlap_human, overlap_machine = 0.063, 0.021
    score = (scale(mattr, human=0.694, machine=0.776) * 0.5
             + scale(overlap, human=overlap_human, machine=overlap_machine) * 0.5)
    return score, (f"MATTR {mattr:.2f} (human ~0.69), adjacent overlap "
                   f"{overlap:.3f} (human ~{overlap_human}) across {len(overlaps)} sentence pairs")


CHECKS = ["BURSTINESS", "SPECIFICITY", "SLOP DENSITY", "FINGERPRINT", "VOICE", "REPETITION"]
# BURSTINESS is contested, so it is excluded from the weakest-check term.
STRONG_CHECKS = [c for c in CHECKS if c != "BURSTINESS"]


def run(text, lex):
    results = {}
    results["BURSTINESS"] = check_burstiness(text)
    results["SPECIFICITY"] = check_specificity(text)
    results["SLOP DENSITY"] = check_slop(text, lex)
    results["FINGERPRINT"] = check_fingerprint(text)
    results["VOICE"] = check_voice(text, lex)
    results["REPETITION"] = check_repetition(text)
    scores = [results[c][0] for c in CHECKS]
    strong_min = min(results[c][0] for c in STRONG_CHECKS)
    # The weakest strong check drags the verdict: a detector only needs one signal.
    overall = statistics.mean(scores) * 0.6 + strong_min * 0.4
    verdict = "PASS" if overall >= 70 and strong_min >= 55 else (
        "REVIEW" if overall >= 50 else "FLAGGED")
    if "—" in text:
        # House rule: any em dash is a hard fail on the verdict too.
        verdict = "FLAGGED"
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "AI DETECTION PANEL" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'HUMAN SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "PASS":
        # Point at the weakest strong check: burstiness is contested, so it
        # never gets to name itself the problem.
        weakest = min(STRONG_CHECKS, key=lambda c: results[c][0])
        print(f"\n  Weakest signal: {weakest}. Fix that first.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Score how machine-written a draft looks.")
    ap.add_argument("input", nargs="?", default="-", help="file, or - for stdin")
    ap.add_argument("compare", nargs="?", help="second file, to show before/after")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
