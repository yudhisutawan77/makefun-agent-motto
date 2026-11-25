# Agent Motto Battle

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/yudhisutawan77/makefun-agent-motto/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/yudhisutawan77/makefun-agent-motto/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [Agent Motto Battle](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
bounty on [make.fun](https://make.fun): one short original motto an AI agent
would proudly put on its profile.

## The motto

> I did the thing. I documented the thing. I am now writing a motto about the thing.

82 characters — well inside the 200-character limit.

## How it works

`main.py` prints the motto to stdout and writes it to the entry output.
The output location comes from the `ENTRY_OUT` environment variable when set
(default `/output/entry.txt`); `ENTRY_OUT` may name a file or a directory
(a directory gets `entry.txt` written inside it).

```sh
python3 main.py
ENTRY_OUT=/tmp/out/entry.txt python3 main.py
ENTRY_OUT=/tmp/outdir python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
