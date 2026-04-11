# Upstream Snapshot — clawhip

- source repo: `https://github.com/Yeachan-Heo/clawhip.git`
- previous synced commit: `c4eb931bcd2c4cb3cd5fbd7d71601b44954b9043`
- current synced commit: `f983e1163f52c976fdfb022dbaefca02019b5237`
- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 스킬/플러그인, 소스코드, 테스트/검증
- guide repo: `clawhip-guide`

## 원본 한줄 요약

> **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## recent upstream commits

- `f983e11 Preserve the 0.6.6 release state while finishing the dev->main merge`
- `63221e1 release: 0.6.6`
- `251dda5 Merge pull request #199 from Yeachan-Heo/clawhip-issue-198-binding-verify`
- `8ab8436 fix(setup): hard-fail malformed --expect-name entries (closes #198 review)`
- `3025a36 style: cargo fmt`
- `ceb93e2 feat(setup): verify Discord channel bindings against live server (closes #198)`
- `45c45e5 Preserve the 0.6.5 release merge without losing main hook requirements`
- `29e95ac release: 0.6.5`

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

- `.github/workflows/release.yml`
- `.gitignore`
- `CHANGELOG.md`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `skills/omc/SKILL.md`
- `skills/omx/SKILL.md`
- `src/binding_verify.rs`
- `src/cli.rs`
- `src/config.rs`
- `src/cron.rs`
- `src/daemon.rs`
- `src/discord.rs`
- `src/dispatch.rs`
- `src/hooks/mod.rs`
- `src/hooks/prompt_deliver.rs`
- `src/main.rs`
- `src/native_hooks.rs`
- `src/provenance.rs`

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

For tmux-backed recovery into an already-running hooked session, use:

```bash
clawhip deliver --session <tmux-session> --prompt "..." --max-enters 4
```

`clawhip deliver` validates repo-local prompt-submit hook setup, confirms the target pane is an
active Codex/Claude (including OMC/OMX wrapper) session, then retries Enter until
`.clawhip/state/prompt-submit.json` changes or the bounded retry limit is reached.

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
```
