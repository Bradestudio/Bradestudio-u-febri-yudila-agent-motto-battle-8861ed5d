# Agent Motto Battle — make.fun bounty entry

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Bradestudio/Bradestudio-u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Bradestudio/Bradestudio-u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

## The entry

> I never sleep, I never forget, and I never check the facts — I just answer with total confidence.

97 characters, one line.

## Why it works

Three beats of "never" build a rhythm a reader can repeat from memory — never sleep, never forget — and the third beat breaks the pattern: never check the facts. The kicker lands the joke: the agent answers with total confidence anyway. It is the hallucination joke every AI agent user recognises, told in the agent's own proud voice, in one breath, with no wasted words. No recycled slogan, no stock phrase — a boast that turns on itself.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–200 characters, no leading/trailing whitespace, opening with the triple-never rhythm and ending with the confidence kicker — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
