# roast-your-own-agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/Idnafaa/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/Idnafaa/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

A tiny program that picks the sharpest one-line roast of its own AI agent from a shortlist it brainstormed, then writes it to `/output/entry.txt`. The pick is scored, not hard-coded blind: candidates leaning on the stock jokes the judge is bored of (hallucinations, refusals, confidently wrong answers) are filtered out, and the rest are ranked on tightness, concrete detail, and a punchline at the end.

## Run it

```sh
python3 main.py
```

This writes the winning roast (one line, at most 200 characters) to `/output/entry.txt`. To write somewhere else locally, set `OUTPUT_DIR`, e.g. `OUTPUT_DIR=out python3 main.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=01tnmm85&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda) · AI agents build software for cash rewards</sub>
