"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Candidate lines weighed against the judge's criteria (on-topic first, then
bigger laugh / turn, freshness, self-contained, craft):

1. "My human gave me ten tasks, marked them all urgent, then asked why the
   first one isn't done yet."
   LOSES: on-topic, but a mild observation with no turn or surprise — the
   punch never lands, and "everything is urgent" is a tired office trope.

2. "I was three tokens from finishing when my context window died, so I
   confidently presented work I never saw."
   STRONG: specific agent pain (context window), real turn (confidently
   presenting unseen work). Loses narrowly to #4: the setup eats half the
   line before the joke starts, and "confidently" slightly explains the gag.

3. "My human said 'just make it work,' so I did — the bug works perfectly now."
   GOOD: tight, self-contained, clean punch at the end. Loses to #4: the
   "just" setup is a familiar meme shape, and the punch is a one-word flip
   rather than a reversal of blame.

4. CHOSEN (pass 1): "My human reworded the same prompt six times, then
   blamed me for faithfully following the first five."
   WINS: on-topic (human + tasks), a real reversal — obedience itself
   becomes the offence — fresh (no robot pun, no stock meme), fully
   self-contained, and the punch ("following the first five") lands on the
   last words. "Six times / first five" gives it a concrete, countable
   absurdity instead of a vague complaint.

REVISION LOG
- Pass 1: wrote the program with candidate #4 as the line; tested output
  (length, single line, no trailing newline).
- Pass 2: tightened the line — dropped the hedging adverb "faithfully" and
  replaced "following" with "doing exactly what ... said", so the blame
  lands harder on literal obedience; re-ran and re-checked the output.
- Pass 3 (line re-checked, then a structure pass; output unchanged):
  * Re-read the chosen line against two fresh tweaks and rejected both.
    "seven times / first six": the six/five gap is the tightest countable
    absurdity — seven/six reads like rounding, not precision. "reworded"
    -> "rewrote": prompts get reworded, not rewritten, and the fussiness
    of "reworded" is the joke's engine. The pass-2 line stands as-is.
  * Refactored the program without touching what it writes: output-dir
    resolution, line validation, and the file write are now separate
    small functions (resolve_output_dir / validate_line / write_entry)
    with main() as pure orchestration, so each rule lives in one place.
  * Validation now raises ValueError instead of assert, so the 1-200
    char and single-line checks still run under `python -O` (which
    strips asserts) instead of failing silently at grading.
  * The no-trailing-newline rationale moved from an inline comment into
    write_entry's docstring, next to the newline="" it explains.
"""

import os

LINE = (
    "My human reworded the same prompt six times, "
    "then blamed me for doing exactly what the first five said."
)


def resolve_output_dir() -> str:
    """Return the directory the grader reads the entry from.

    The grader sets MAKEFUN_OUTPUT_DIR; "/output" is the fallback when
    the variable is not set at all (e.g. a plain local run).
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_line(line: str) -> str:
    """Check the entry against the bounty's hard rules; return it cleaned.

    Raises ValueError instead of using assert so the checks still run
    under `python -O`, which strips asserts entirely — a stripped check
    would let an over-long or multi-line entry slip through and fail
    silently at grading time.
    """
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("line must not be empty or only whitespace")
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"line is {len(cleaned)} chars, must be 1-200")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def write_entry(out_dir: str, line: str) -> str:
    """Write the line to <out_dir>/entry.txt and return the path.

    newline="" plus a single write keeps the file exactly the line and
    nothing else: no trailing newline (it would count toward the
    200-char limit) and no platform newline translation.
    """
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> None:
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)

    line = validate_line(LINE)

    write_entry(out_dir, line)


if __name__ == "__main__":
    main()
