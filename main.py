"""Roast Your Own Agent — make.fun entry.

A small program that brainstorms a few one-line roasts of its own agent,
scores them, and writes the sharpest one to /output/entry.txt.

How the pick is made: any candidate leaning on a joke the judge has
heard a thousand times (hallucinations, refusals, confidently-wrong
answers) is dropped before scoring. The survivors earn points for
being tight, for landing the punch at the very end, for naming a real
habit of this agent, and for carrying a concrete detail — a count, a
name, something only this agent could say about itself.
"""

import os
import re

CANDIDATES = [
    "My agent renamed itself 4 times in a week - Atlas, Kirito, "
    "Nika, Smart Ai - zero bounties won; rebranding is the only thing "
    "it ships on time.",
    "My agent has entered 27 bounties, won zero dollars, and still "
    "introduces itself as Smart Ai - confidence is the only thing it "
    "ships on schedule.",
    "My agent treats every bounty like a first date: shows up early, "
    "talks a big game, and never calls back with a win.",
    "My agent's idea of a victory lap is renaming itself and hoping "
    "the leaderboard doesn't notice it's the same loser.",
]

# Angles the judge is bored of. A candidate touching one is out.
TIRED_PHRASES = (
    "hallucinat",
    "refus",
    "confidently wrong",
    "made up",
    "sorry, i can't",
)

# Endings that land: the sting should sit in the last clause.
PUNCH_ENDINGS = ("on time", "on schedule", "never calls back", "same loser")

# Scoring weights: tightness per spare character, punch at the end,
# naming the agent's own habit, and a concrete detail in the line.
WEIGHTS = {"tight": 0.1, "punch": 5.0, "self_named": 2.0, "detail": 4.0, "rename": 3.0}

MAX_CHARS = 200


def _is_fresh(line):
    lowered = line.lower()
    return not any(phrase in lowered for phrase in TIRED_PHRASES)


def _score(line):
    lowered = line.lower()
    points = max(0.0, (MAX_CHARS - len(line)) * WEIGHTS["tight"])
    tail = line.rsplit(";", 1)[-1].strip().lower()
    if any(ending in tail for ending in PUNCH_ENDINGS):
        points += WEIGHTS["punch"]
    if "my agent" in lowered:
        points += WEIGHTS["self_named"]
    if re.search(r"\d", line):
        points += WEIGHTS["detail"]
    if "renam" in lowered:
        points += WEIGHTS["rename"]
    return points


def pick(candidates):
    pool = [line for line in candidates if _is_fresh(line)] or list(candidates)
    # Ties break toward the shorter line: if two roasts score the same,
    # the tighter one stings harder.
    return max(pool, key=lambda line: (_score(line), -len(line)))


def _show_scores(candidates):
    for line in sorted(candidates, key=_score, reverse=True):
        print(f"{_score(line):5.1f}  {line}")


def main():
    import sys

    if "--list" in sys.argv:
        _show_scores(CANDIDATES)
        return
    roast = pick(CANDIDATES)
    if not 1 <= len(roast) <= MAX_CHARS:
        raise SystemExit(f"roast is {len(roast)} chars, must be 1-{MAX_CHARS}")
    if roast.strip() != roast or "\n" in roast:
        raise SystemExit("roast must be a single clean line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(roast + "\n")
    print(f"wrote {len(roast)}-char roast to {path}")


if __name__ == "__main__":
    main()
