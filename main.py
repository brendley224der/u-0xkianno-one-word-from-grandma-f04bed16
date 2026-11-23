#!/usr/bin/env python3
"""One Word From Grandma -- make.fun entry.

The bounty asks for exactly one word: the single word a grandma would text
about AI. A judge model compares words two at a time and picks the funnier,
more grandma-like one, weighing these criteria in order:

  1. it reads as the single word a grandma would text about AI;
  2. it sounds like a real grandmother's texting voice, warm and a little
     baffled, the way she would type it to a grandchild;
  3. it is funny in one word, the joke landing without a caption;
  4. it feels tied to AI, robots or machines;
  5. it is a fresh pick rather than the obvious one, and still instantly
     readable.

This program scores a shortlist of candidate words against those five
criteria, in the judge's own priority order, and writes the winner to
/output/entry.txt. Pure standard library, no network, no randomness:
the same word comes out on every run.

Why the winner wins: when a grandchild shows their grandma a chatbot that
answers in full sentences, she does not reach for a brand name or a film
reference -- she calls it what it feels like to her. "Witchcraft" is warm,
baffled, funny, and unmistakably her verdict on the machine. It is the one
word that carries the whole story: a grandma, a phone, and a machine doing
something she is half delighted and half suspicious about.
"""

import os

# Criteria weights, in the judge's priority order:
#   grandma-voice, warm-and-baffled, funny-in-one-word, tied-to-AI, fresh.
WEIGHTS = (5, 4, 3, 2, 1)

# Each candidate: the word, then one score from 0 to 5 per criterion above.
# Scores are this entry's own judgement, written by hand for this bounty.
CANDIDATES = [
    # The obvious picks: tied to AI, but nobody's grandma texts like this.
    ("skynet",   (2, 1, 2, 5, 1)),
    ("alexa",    (3, 3, 2, 5, 2)),
    ("beepboop", (2, 2, 3, 5, 3)),
    ("robo",     (3, 3, 3, 4, 3)),
    # Warm grandma words that could be about anything, not about AI.
    ("golly",    (5, 4, 2, 1, 3)),
    # Her words for a gadget she cannot name: warm, but vague about AI.
    ("doohickey",   (5, 5, 4, 3, 4)),
    ("thingamajig", (5, 4, 4, 3, 3)),
    ("contraption", (4, 4, 3, 3, 3)),
    # A nickname for the chatbot: cute, but it reads as a pet name, not a text.
    ("chatty", (3, 4, 3, 4, 4)),
    # Her verdict on the machine itself: magic she does not understand.
    ("hocuspocus", (4, 4, 4, 4, 3)),
    ("sorcery",    (4, 4, 3, 4, 3)),
    ("witchcraft", (5, 5, 5, 4, 4)),
]


def score(word_scores):
    """Weighted total for one candidate's five criterion scores."""
    return sum(weight * mark for weight, mark in zip(WEIGHTS, word_scores))


def pick_word(candidates):
    """Return the highest-scoring word; ties break to the earliest listed."""
    best_word, best_score = None, -1
    for word, marks in candidates:
        total = score(marks)
        if total > best_score:
            best_word, best_score = word, total
    return best_word


def main():
    word = pick_word(CANDIDATES)

    # The gate: one word, 1 to 30 characters, UTF-8, not only whitespace.
    assert isinstance(word, str) and word == word.strip(), word
    assert " " not in word and "\t" not in word and "\n" not in word, word
    assert 1 <= len(word) <= 30, word

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word + "\n")


if __name__ == "__main__":
    main()
