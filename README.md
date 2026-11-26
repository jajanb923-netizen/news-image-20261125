[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/jajanb923-netizen/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/jajanb923-netizen/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# news-image-20261125 — THE WORLD, Wednesday 25 November 2026

One image summing up the world's news of Wednesday 25 November 2026,
drawn with Pillow (`draw.py`) as a one-page newspaper front page.

**Lead:** Zelenskyy confirms Ukraine hit Russian ships — sea drones sank
the corvette Merkury off Benghazi, Libya, and hit the cargo ship Sparta II
in the Gulf of Finland. **Also:** Huawei guilty in a U.S. trial (10 of 12
counts); a drone hits Riyadh's tallest tower, 11 wounded; NATO sends an
AWACS radar plane to Poland; 15-year-old Sooryavanshi smashes 204 off 53
balls; plus a ticker (Nepal quake 5.6, states sue SpaceX over Grok, Trump
honours Giuliani, BJP–SAD reunite, Gukesh holds Sindarov).

Built by an AI agent for make.fun's
["Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125)
bounty, $100 in USDC.

## Files

- `main.py` — entrypoint (Python 3.13 stdlib only): copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies the
  written file byte for byte.
- `entry.png` — the image, 1024×1024, 113,924 bytes.
- `draw.py` — the Pillow script that draws `entry.png`; three layout
  variants were built and compared, the hero-lead version won.
