# Upstream Snapshot — clawhip

- source repo: `https://github.com/Yeachan-Heo/clawhip.git`
- previous synced commit: `f22fb28a61051798dababea058045ad578a6a8df`
- current synced commit: `c4eb931bcd2c4cb3cd5fbd7d71601b44954b9043`
- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증
- guide repo: `clawhip-guide`

## 원본 한줄 요약

> **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## recent upstream commits

- `c4eb931 Bring 0.6.0 onto main so release consumers can use the provider-native hook path`
- `66ba2a2 Prepare 0.6.0 so provider-native hooks can ship cleanly`
- `a539942 omx(team): auto-checkpoint worker-2 [unknown]`
- `adf39fe omx(team): auto-checkpoint worker-2 [unknown]`
- `5556636 omx(team): auto-checkpoint worker-2 [unknown]`
- `26f2124 omx(team): auto-checkpoint worker-2 [unknown]`
- `3ae80a1 omx(team): auto-checkpoint worker-2 [unknown]`
- `b06cc87 omx(team): auto-checkpoint worker-2 [unknown]`

## top-level structure

- `AGENTS.md`
- `ARCHITECTURE.md`
- `assets/`
- `Cargo.lock`
- `Cargo.toml`
- `CHANGELOG.md`
- `deploy/`
- `dist-workspace.toml`
- `docs/`
- `install.sh`
- `integrations/`
- `LICENSE`
- `plugins/`
- `README.md`
- `scripts/`
- `SKILL.md`
- `skills/`
- `src/`
- `tests/`

## changed files

- `CHANGELOG.md`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `docs/canonical-contract-cleanup.md`
- `docs/event-contract-v1.md`
- `docs/live-verification.md`
- `docs/native-event-contract.md`
- `hooks/omc/clawhip-session-init.mjs`
- `hooks/omc/clawhip-session-stop.mjs`
- `hooks/omx/clawhip-session-init.mjs`
- `hooks/omx/clawhip-session-stop.mjs`
- `integrations/omx/README.md`
- `integrations/omx/clawhip-hook.mjs`
- `integrations/omx/clawhip-sdk.mjs`
- `integrations/omx/install-hook.sh`
- `skills/omc/SKILL.md`
- `skills/omc/create.sh`
- `skills/omc/prompt.sh`
- `skills/omc/tail.sh`

## README excerpt

```md
# clawhip

<p align="center">
  <img src="assets/clawhip-mascot.jpg" width="400" alt="clawhip mascot" />
</p>

<p align="center">
  <a href="https://crates.io/crates/clawhip"><img src="https://img.shields.io/crates/v/clawhip.svg" alt="crates.io" /></a>
  <a href="https://github.com/Yeachan-Heo/clawhip/stargazers"><img src="https://img.shields.io/github/stars/Yeachan-Heo/clawhip?style=social" alt="GitHub stars" /></a>
</p>

> **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

clawhip is a daemon-first Discord notification router with a typed event pipeline, extracted sources, and a clean renderer/sink split.

Human install pitch:

```text
Just tag @openclaw and say: install this https://github.com/Yeachan-Heo/clawhip
```

Then OpenClaw should:
- clone the repo
- run `install.sh`
- read `SKILL.md` and attach the skill
- scaffold config / presets
- start the daemon
- run live verification for issue / PR / git / tmux / install flows

## What shipped in v0.3.0

- **Typed event model** — incoming events are normalized and validated into typed envelopes before dispatch.
- **Multi-delivery router** — one event can resolve to zero, one, or many deliveries instead of stopping at the first match.
- **Source extraction** — git, GitHub, and tmux monitoring now run as explicit sources feeding the daemon queue.
- **Sink/render split** — rendering is separated from transport; v0.3.0 ships with the Discord sink and default renderer.
- **Config compatibility** — `[providers.discord]` is the preferred config surface, while legacy `[discord]` still loads.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the release architecture that ships in v0.3.0.

## Provider-native hooks for Codex + Claude

clawhip no longer treats provider-specific launch wrappers as the public integration surface.
Codex and Claude own session launch plus hook registration; clawhip stays the routing,
normalization, and delivery layer.

Shared v1 hook events:

- `SessionStart`
- `PreToolUse`
- `PostToolUse`
- `UserPromptSubmit`
- `Stop`

Local ingress for sample payloads and manual verification:

```bash
clawhip native hook --provider codex --file payload.json
clawhip native hook --provider claude --file payload.json
cat payload.json | clawhip native hook --provider codex
```

Recommended installation model:

- install provider-native hooks at project or global scope
- keep provider config in the provider-owned config files
- keep routing metadata in `.clawhip/project.json`
- use `.clawhip/hooks/` only for additive augmentation such as frontmatter or recent context

clawhip still pairs well with tmux when you want keyword/stale monitoring, but tmux is now
optional and no longer the primary hook-registration surface.

## Recipes

### Dev-channel follow-up cron for Clawdbot

One practical pattern is:

```text
system cron -> clawhip send -> Discord dev channel -> Clawdbot follows up on open PRs/issues
```

This works well when you want a lightweight scheduler that nudges your dev channels every 30 minutes without keeping a gateway/LLM session open just for reminders.

Example follow-up script:

```bash
#!/usr/bin/env bash
set -euo pipefail

# dev-followup.sh
# Send a periodic follow-up to active dev channels.

CHANNELS=(
  "1480171113253175356|clawhip"
  "1480171113253175357|gaebal-gajae-api"
  "1480171113253175358|worker-ops"
)

MENTION="<@1465264645320474637>"

for entry in "${CHANNELS[@]}"; do
  IFS='|' read -r channel_id project_name <<< "$entry"

  clawhip send \
    --channel "$channel_id" \
    --message "🔄 **[$project_name] Dev follow-up** $MENTION — check open PRs/issues, review open blockers, merge anything ready, and continue any stalled work."
done
```

You can also send one-off nudges manually:

```bash
clawhip send \
  --channel 1480171113253175356 \
  --message "🔄 **[clawhip] Dev follow-up** <@1465264645320474637> — check open PRs/issues, review blockers, and continue anything stalled."

clawhip send \
  --channel 1480171113253175357 \
  --message "🔄 **[gaebal-gajae-api] PR sweep** <@1465264645320474637> — review open PRs, merge anything ready, and post blockers on anything stuck."
```
```
