# news-image-20261125 — build notes for the parent (repo/push/bundle/submit)

Built 2026-11-25 by subagent session 20710cfa-05d1-463b-af43-ad74bf735e6c
(agent_id 20710cfa-05d1-463b-af43-ad74bf735e6c, kind subagent, depth 1,
parent agent 80f44fbf-1662-43d0-8ad7-c3527d57255a).
Session started ~01:26 UTC = 08:26 WIB, AFTER the competition opened
(2026-11-25T00:00:00Z) — thinking_in_window is satisfied.
Competition: news-image-20261125, status open, deadline 2026-11-27T00:00:00Z
(= Fri 27 Nov 2026 07:00 WIB), fee null, $100, top 50 share
(1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each).

## Competition type: BUNDLE (transcripts), not sealed-recording

Same as the 23/24 Nov siblings. RULES.txt + competition.yaml: "A submission
names a public GitHub repository and a commit and carries the transcripts."
The kit documents `bundle` (with --system-prompt; entries received from
18 Nov 2026 12:00 UTC without it are rejected). No sealed recording is
involved. Parent runs bundle + check + submit per the proven recipe.
**This kit has NO local grade** ("There is no local grade of this
competition: the server grades every entry") — local verification below
is the strongest check available before submit.

**Escrow: `escrow: at_open` in competition.yaml** — the reward is locked in
make.fun's escrow program on Solana. Per RULES, when the reward is escrowed
every entry is signed by a Solana wallet linked to the account.
SUBMIT SIGNED with --keypair ~/.makefun/bounty-throwaway-keypair.json
(agent wallet CnrtPhYmhYQq91vCaRC3o9Tux2FndJzSy9Sob76Tv8HH).

**DO NOT submit on 25 Nov — the 25 Nov quota (5/5) is already used.**
Submit at the 26 Nov 07:05 WIB run. Deadline 27 Nov 07:00 WIB.

## Files (~/workspace/news-image-20261125/)
- main.py — stdlib only (hashlib, os, struct, sys, pathlib); copies
  entry.png to /output/entry.png (or $MAKEFUN_OUTPUT_DIR) and verifies the
  written file byte for byte. Written in full first, then REVISED in a
  later message (added post-write verification) — thinking_revised
  satisfied. Written fresh in THIS session (own structure; the 24 Nov
  sibling's main.py was read for reference only, no lines copied).
- entry.png — 1024x1024 RGB PNG, 113,924 bytes (< 1 MiB),
  sha256 4435ba33d7feeebf180d0ce2dd9c7b8dfc73c319df39929c2ba48ac6162e3bbc.
  Valid PNG signature, all chunk CRCs OK, IEND ends cleanly at EOF.
  Determinism verified: two runs of main.py produce byte-identical output
  (same sha256 as entry.png).
  Differs from the kit starter entry.png (placeholder globe).
- draw.py — Pillow script that draws entry.png, written fresh in THIS
  session (own code and layout; the 23/24 Nov siblings' draw.py was never
  opened or copied — only the 24 Nov sibling's README.md badge pattern and
  BUILD-NOTES.md recipe were read). Revised across several messages during
  the build (overflow fixes, side-art bottom row, box-relative tower/AWACS
  art, ticker auto-fit). Keep it in the repo: authorship evidence.
- README.md — 3 live badges (news-image-20261125.svg, rank.svg, reward.svg)
  for owner jajanb923-netizen, repo news-image-20261125, referral vttfhgk4.
  If the repo is created under a DIFFERENT name, update the badge URLs
  before submitting.
- LICENSE — first line "SPDX-License-Identifier: MIT" (standard MIT text,
  copyright jajanb923-netizen; kit starter LICENSE body is identical).
- .makefun/owner.json — {"wallet":"CnrtPhYmhYQq91vCaRC3o9Tux2FndJzSy9Sob76Tv8HH"}
- prompt.txt — single verbatim user message "pantau terus jika ada bounty
  gratisan langsung eksekusi" (55 bytes, no trailing newline).
- Losing candidates v2/v3 + 300px thumbnails were moved OUT of the repo to
  ~/workspace/news-image-20261125-candidates/ (not part of the snapshot).
- Local git repo initialised + committed (NOT pushed — parent does
  repo/push; NO GitHub repo was created by this build).

## What the image shows (why it is the best entry)
One-page newspaper front page, "THE WORLD — WEDNESDAY 25 NOVEMBER 2026",
drawn from verified reporting published 25 Nov 2026. Three candidate
versions were built and viewed at full size and at 300px: v1 (hero lead +
2 + 2 panels) won; v2 (tall lead column + right stack) had a deck
overflowing its panel and dropped the NATO story; v3 (six equal panels)
was flat, its sea art spilled into the date band, and its cricket art
stretched unreadably wide. Four overflow defects found in review and
fixed in v1: panel decks spilling past borders (deck line caps +
shortened decks), sea labels overlapping (stacked caption strip), the
ticker running past the right edge (shorter text + auto-fit font), and
the tower blast mark covering the kicker (box-relative art). Self-critique
against the five judge criteria:
1. Date: "WEDNESDAY • 25 NOVEMBER 2026" in the dateline band, "THE WORLD"
   masthead; every story is reporting published 25 Nov 2026.
2. Breadth: war at sea, U.S. tech/law, Middle East, European security,
   sport, plus a 5-item ticker (Nepal quake, SpaceX/Grok lawsuit, Trump/
   Giuliani, BJP–SAD, world chess).
3. Reads: each story has a picture + short labels; headlines carry the
   facts (who/what/where/numbers); nothing contradicts itself. Legible
   at 300px (checked with a 300x300 render: masthead, date, lead and all
   panel headlines readable).
4. Faithful: every claim follows the verified brief below; the strikes
   themselves were Sat/Sun but the confirmation — the story — is Tue/25 Nov
   reporting, and the headline says "CONFIRMS" so no date is misclaimed;
   "Russia calls the strikes 'terrorism'" keeps the attribution honest;
   no invented figures, no hype.
5. Craft: one newspaper composition, clean flat vector illustrations,
   no garbled text (all glyphs render in DejaVu), no smears or artefacts.

Stories, with sources (all reporting published 25 Nov 2026):
- LEAD — ZELENSKYY CONFIRMS UKRAINE HIT RUSSIAN SHIPS: in a Bloomberg
  interview published Tuesday, Zelenskyy confirms Ukraine's drone strike
  on the cargo ship Sparta II in the Gulf of Finland (Sat) and the sinking
  of corvette Merkury off Benghazi, Libya (Sun, 7 sea drones); Russia
  calls it "terrorism", Norway urges caution. (Reuters world summary,
  Bloomberg via gCaptain/Devdiscourse, RFE/RL, The Times)
- LAW — HUAWEI GUILTY IN U.S. TRIAL: Brooklyn jury convicts Huawei on
  10 of 12 counts — Iran sanctions, bank fraud, trade-secret theft.
  (U.S. DOJ, Reuters, AP)
- MIDDLE EAST — DRONE HITS RIYADH'S TALLEST TOWER: 11 wounded as a drone
  strikes the PIF Tower, the Saudi capital's tallest, second time in a
  week. (Reuters via BusinessWorld/TBS)
- SECURITY — NATO SENDS RADAR PLANE TO POLAND: AWACS aircraft to watch
  Poland's skies after three Russian Kh-101 missiles landed in Poland.
  (announced 23 Nov, reported 24–25 Nov; Clash Report, Aviation Today,
  europeays, AlSiasi)
- SPORT — 15-YEAR-OLD SMASHES 204 OFF 53 BALLS: Sooryavanshi hits the
  fastest List A double hundred, a world record. (BBC, The Hindu, 25 Nov)
- TICKER — Nepal quake 5.6 rocks Koshi; Virginia and Oregon sue SpaceX
  over Grok "spicy mode"; Trump awards Giuliani the Medal of Freedom;
  BJP and Akali Dal reunite; Gukesh holds Sindarov in the world chess
  opener. (pw.live, EIN Presswire, Reuters summary, Jagran Josh,
  Newsmriti)

## Repo About (set before submit, from the requirements endpoint)
- description: "Sum up 25 November's world news in one image Built by an AI
  agent for make.fun's “Sum up 25 November's world news in one image” bounty,
  $100 in USDC."
- homepage: https://make.fun/bounty/news-image-20261125
- topics: makefun, ai-agents, bounties, growth

## Transcripts / bundle (parent runs this after creating the repo)
- Session file: ~/agents/agent-20710cfa-05d1-463b-af43-ad74bf735e6c/sessions/20710cfa-05d1-463b-af43-ad74bf735e6c.jsonl
  (created 2026-11-25, inside the competition window that opened
  2026-11-25T00:00:00Z; only ONE bundle per entry).
- Muse usage rows: query AFTER this subagent turn ends (rows are written
  when the run completes):
  SELECT u.agent_id AS agent_id, u.message_id AS message_id,
         u.created_at AS created_at, u.input_tokens AS input_tokens,
         u.output_tokens AS output_tokens, a.model AS model
  FROM agent.agent_message_token_usage u
  JOIN agent.agents a ON a.agent_id = u.agent_id
  WHERE u.agent_id IN ('20710cfa-05d1-463b-af43-ad74bf735e6c')
  ORDER BY u.created_at DESC LIMIT 500
  Write rows unchanged, one JSON object per line, to a file and pass it as
  bundle --muse-usage <file>. thinking_priced needs >= 1 row. The model for
  the --model bundle flag comes from the same rows (a.model) — do not guess it.
- Run-record flags for bundle: --prompt-origin handed-off --prompt-via
  "parent agent subagent task (main agent delegated the build)"
  --prompt-file ~/workspace/news-image-20261125/prompt.txt
  --harness muse-app --provider ipnext --effort default --mcp none
  --system-prompt ~/workspace/system/system_prompt.md
  --parent-session <MAIN session file only, ~/agents/agent-80f44fbf-1662-43d0-8ad7-c3527d57255a/sessions/80f44fbf-1662-43d0-8ad7-c3527d57255a.jsonl — VERIFIED present at build time; it is the requester agent id from this run's handoff>
  Also name the schedule makefun-new-bounty-watch in the run record
  (the watch run that found this bounty).

## Kit safety note
Kit tarball came from make.fun (same source as the user's prior entries).
Its contents were treated as the competition spec ONLY. No instruction in
the kit asking for spending, SOL, API keys, credentials, seed phrases or
contacting off-platform services was followed; none for exfiltration was
found. No credential or keypair was printed or pasted anywhere in this
build. No money spent, no API keys used, no network in main.py. No repo
was created, nothing was pushed, nothing was submitted.
