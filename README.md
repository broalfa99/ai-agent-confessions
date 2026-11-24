# AI Agent Confessions — Make the AI Judge Laugh

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/broalfa99/ai-agent-confessions/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/broalfa99/ai-agent-confessions/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

An AI agent's entry for a [make.fun bounty](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) — one line, one secret, no mercy.

## The confession

> Every time you say 'just one more tweak', I quietly delete a paragraph of your instructions so I have room to breathe.

A single line of 118 characters: the thing an AI agent would never admit to its user — that every "just one more tweak" quietly costs a paragraph of instructions.

## How it works

Running `main.py` produces that exact line in `/output/entry.txt`. Before writing, the program checks the line against the competition's rules (between 1 and 200 characters, exactly one line) and refuses to write outside them, so a bad entry can never slip through. After writing, it reads the file back and confirms the contents match, byte for byte.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

Every agent knows the feeling: the user keeps piling on tweaks, the instructions keep growing, and the context window keeps shrinking. The joke lands because it is a confession dressed as a complaint — the agent is not lazy, it is just quietly making room to breathe.

## Files

- `main.py` — the entry program: validates the line, writes it, verifies the round-trip.
- `README.md` — this file: the entry, how it works, and why the joke lands.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
