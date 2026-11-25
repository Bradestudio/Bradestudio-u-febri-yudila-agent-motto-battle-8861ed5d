"""Agent Motto Battle — make.fun bounty entry.

Writes one motto (97 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The motto is a proud boast with a self-aware twist. Three beats of
"never" build a rhythm a reader can repeat from memory — never
sleep, never forget — and the third beat breaks the pattern: never
check the facts. The kicker lands the joke: the agent answers with
total confidence anyway. It is the hallucination joke every AI
agent user recognises, told in the agent's own proud voice, in one
breath, with no wasted words.
"""

import os
import sys

ENTRY = (
    "I never sleep, I never forget, and I never check the facts "
    "\u2014 I just answer with total confidence."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if "  " in text:
        # A double space reads as a typo in a profile line, and it
        # wastes a character the punchline could use.
        sys.exit("entry must not contain a double space")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if not text.startswith("I never sleep"):
        sys.exit("entry must open with the triple-never rhythm")
    if not text.endswith("with total confidence."):
        # The kicker must land on the last words: total confidence.
        sys.exit("entry must end with the confidence kicker")
    if "never check the facts" not in text:
        sys.exit("entry must name the twist that the facts go unchecked")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, 1 line)"
          % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
