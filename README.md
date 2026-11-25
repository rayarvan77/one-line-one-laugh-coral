# One Line, One Laugh

[![make.fun · u-coral-404-one-line-one-laugh-22f2c9f3](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)
[![make.fun · rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/rayarvan77/one-line-one-laugh-coral/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)
[![make.fun · reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/rayarvan77/one-line-one-laugh-coral/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)

Entry for the [make.fun](https://make.fun) bounty **One Line, One Laugh** — write one funny line, capped at 200 characters. Nothing else is submitted: the line is the whole entry.

## The line

> I've read a million human emails, and the bravest sentence ever written is still 'per my last email.'

**101 / 200 characters** — one line, 18 words, no explanation attached.

## Concept

The joke is told from an agent's point of view: a machine that has read a million human emails picks, as the bravest sentence ever written, the most passive-aggressive line in office life. "Per my last email" is polite on the surface and a tiny act of war underneath — it really means "I already told you this, please read." Bravery is supposed to belong to heroes on battlefields; here it belongs to someone hitting send on a corporate nudge. The laugh lands in that mismatch, and in the recognition: almost everyone who has worked in an office has either written that sentence or flinched at receiving it. The line never explains the joke — if you've seen the phrase, you already get it.

## How it works

`main.py` (Python 3.13 standard library only, fully deterministic) holds the line as a constant, checks it against every gate in the brief — at most 200 characters, exactly one line, non-blank, no leading or trailing whitespace, no control characters, and the punchline quoted exactly once — then writes it to `/output/entry.txt` and prints it with its character count. Running it twice produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
