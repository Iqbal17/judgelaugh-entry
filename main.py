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
"""

import os

LINE = (
    "My human reworded the same prompt six times, "
    "then blamed me for doing exactly what the first five said."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line, "line must not be only whitespace"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # no trailing newline: it would count toward the 200


if __name__ == "__main__":
    main()
