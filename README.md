# One Word From Grandma

Entry for the [make.fun bounty "One Word From Grandma"](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16): send exactly one word — the single word a grandma would text about AI.

## The word

**witchcraft**

When a grandchild shows their grandma a chatbot that answers in full
sentences, she does not reach for a brand name or a film reference — she
calls it what it feels like to her. "Witchcraft" is warm, a little baffled,
funny in one word, and unmistakably her verdict on the machine. It carries
the whole story: a grandma, a phone, and a machine doing something she is
half delighted and half suspicious about.

## How it works

`main.py` (pure Python standard library, no network, no randomness) scores a
shortlist of candidate words against the judge's five criteria, in the
judge's own priority order — grandma-voice, warm-and-baffled, funny in one
word, tied to AI, fresh — and writes the winner to `/output/entry.txt`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is deterministic: the same word on every run.

## License

MIT — see [LICENSE](LICENSE).
