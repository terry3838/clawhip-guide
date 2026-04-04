# Upstream Snapshot — clawhip

- source repo: `https://github.com/Yeachan-Heo/clawhip.git`
- previous synced commit: `098ecf6b01d743a68a60d1ec77c0539b64e2f16a`
- current synced commit: `818531d3002090c9a9d0528ad929f22df267d522`
- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드
- guide repo: `clawhip-guide`

## 원본 한줄 요약

> **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## recent upstream commits

- `818531d Merge pull request #126 from Yeachan-Heo/release/0.5.1-prep`
- `2bbf9a1 Merge origin/main into release/0.5.1-prep for main release sync`
- `9986b08 Reduce clawhip session skills to launch mechanics`
- `8677a89 Make clawhip docs the source of truth for OMC/OMX operators`
- `3879e40 Fix OMX native hook bridge install layout for real plugin validation`
- `679b9e7 Surface the native OMX bridge as the default release path`
- `286b775 Prepare the 0.5.1 branch metadata for a tagged release`
- `96db180 feat: add managed cron jobs and native cron entrypoint (#116) (#117)`

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

- `.omx/context/clawhip-build-20260308T103330Z.md`
- `.omx/logs/hooks-2026-03-08.jsonl`
- `.omx/logs/notify-fallback-2026-03-08.jsonl`
- `.omx/logs/notify-fallback-2026-03-09.jsonl`
- `.omx/logs/notify-hook-2026-03-08.jsonl`
- `.omx/logs/omx-2026-03-08.jsonl`
- `.omx/logs/tmux-hook-2026-03-08.jsonl`
- `.omx/logs/turns-2026-03-08.jsonl`
- `.omx/metrics.json`
- `.omx/notepad.md`
- `.omx/plans/autopilot-impl.md`
- `.omx/plans/autopilot-spec.md`
- `.omx/state/auto-nudge-state.json`
- `.omx/state/hud-state.json`
- `.omx/state/notify-fallback-state.json`
- `.omx/state/notify-fallback.pid`
- `.omx/state/notify-hook-state.json`
- `.omx/state/session.json`
- `.omx/state/sessions/omx-1772965833622-69uz5f/AGENTS.md`
- `.omx/state/sessions/omx-1772965833622-69uz5f/autopilot-state.json`

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

## What shipped in v0.4.0

- **Install lifecycle polish** — repo-local installs, `clawhip install`, `clawhip update`, and `clawhip uninstall` are documented and aligned for clone-local operator workflows.
- **Optional GitHub support prompt** — interactive install flows can offer an explicit opt-in GitHub star prompt, with `--skip-star-prompt` and `CLAWHIP_SKIP_STAR_PROMPT=1` available on both installer surfaces.
- **Filesystem memory scaffolds** — `clawhip memory init` and `clawhip memory status` bootstrap and inspect the filesystem-offloaded memory layout for repos and workspaces.
- **Native session contract polish** — OMC/OMX payload normalization now prefers the lower-noise `session.*` route family while keeping legacy `agent.*` compatibility.
- **Config compatibility** — `[providers.discord]` remains the preferred config surface, while legacy `[discord]` still loads.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the release architecture that ships in v0.4.0.

## Good to use together

clawhip pairs well with coding session tools that run in tmux:

### [OMX (oh-my-codex)](https://github.com/Yeachan-Heo/oh-my-codex)

OpenAI Codex wrapper with auto-monitoring. Launch monitored coding sessions:

```bash
clawhip tmux new -s issue-123 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,PR created,complete" \
  -- 'source ~/.zshrc && omx --madmax'

# or attach monitoring to an existing tmux session
clawhip tmux watch -s issue-123 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,PR created,complete"

# inspect active daemon-known watches later
clawhip tmux list
```

See [`skills/omx/`](skills/omx/) for ready-to-use scripts.
Recommended default clawhip + OMX setup: install the native bridge from [`integrations/omx/`](integrations/omx/) and forward the frozen hook envelope via `clawhip omx hook` when the CLI is available, with `POST /api/omx/hook` as the daemon fallback.
Native OMC/OMX routing now prefers the normalized [`session.*` contract](docs/native-event-contract.md); legacy `agent.*` wrapper emits remain supported for compatibility only.

### [OMC (oh-my-claudecode)](https://github.com/Yeachan-Heo/oh-my-claudecode)

Claude Code wrapper with auto-monitoring. Launch monitored coding sessions:

```bash
clawhip tmux new -s issue-456 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,PR created,complete" \
  -- 'source ~/.zshrc && omc --openclaw --madmax'
```

See [`skills/omc/`](skills/omc/) for ready-to-use scripts.
Direct Slack/Discord notifications inside OMC/OMX should be treated as deprecated; emit native events and let clawhip own routing, mention policy, and formatting.

#### Gajae operator setup → verify → fix

For OMC/OMX-integrated setups, clawhip is the source of truth for routing doctrine and troubleshooting. Keep session skills focused on launch mechanics, then use clawhip docs for the operational rails:

- quick entrypoint: this README section
- detailed OMX runbook: [`integrations/omx/README.md`](integrations/omx/README.md)
- native routing/reference contract: [`docs/native-event-contract.md`](docs/native-event-contract.md)

**Setup**
1. Confirm the daemon you plan to use is the one you expect:
   ```bash
   clawhip --version
   clawhip status
   ```
2. For OMX, install the native hook bridge into the target workspace, then validate it:
   ```bash
   ./integrations/omx/install-hook.sh /path/to/repo/.omx/hooks
   omx hooks validate
   omx hooks test
   ```
3. Add an explicit native session route. Use `event = "session.*"` and filter on `repo_name`, not `repo`:
   ```toml
   [[routes]]
   event = "session.*"
   filter = { tool = "omx", repo_name = "clawhip" }
   channel = "1480171113253175356"
   format = "compact"
   ```
   For OMC-native session traffic, keep the same event family and switch the tool filter to `omc` when needed.
4. Leave `[defaults].channel` configured only as a fallback safety net, not as your primary session-routing policy.

**Verify**
- Trigger a real OMC/OMX session event and confirm it lands in the intended route channel.
- If the event lands in the default channel instead, treat that as a route miss first.
- If `clawhip cron run` is part of your operator flow, verify `[[cron.jobs]]` exists before treating the command as meaningful.

**Fix**
```
