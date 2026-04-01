# Upstream Snapshot — clawhip

- source repo: `https://github.com/Yeachan-Heo/clawhip.git`
- synced commit: `098ecf6b01d743a68a60d1ec77c0539b64e2f16a`
- guide repo: `clawhip-guide`

## 원본 한줄 요약

<p align="center"> <img src="assets/clawhip-mascot.jpg" width="400" alt="clawhip mascot" /> </p>

## top-level structure

- `.omx/`
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
```

See [`skills/omx/`](skills/omx/) for ready-to-use scripts.
Native OMC/OMX routing now prefers the normalized [`session.*` contract](docs/native-event-contract.md); legacy `agent.*` wrapper emits remain supported for compatibility.

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

## Recipes
```
