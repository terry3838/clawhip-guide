# clawhip 개요

## 원본 저장소 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- latest synced commit: `818531d30020`
- summary: > **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## 이번 싸이클 판단

- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드
- 판단: origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드.

## 최근 upstream 커밋

- `818531d Merge pull request #126 from Yeachan-Heo/release/0.5.1-prep`
- `2bbf9a1 Merge origin/main into release/0.5.1-prep for main release sync`
- `9986b08 Reduce clawhip session skills to launch mechanics`
- `8677a89 Make clawhip docs the source of truth for OMC/OMX operators`
- `3879e40 Fix OMX native hook bridge install layout for real plugin validation`
- `679b9e7 Surface the native OMX bridge as the default release path`

## 확인한 원본 구조

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

## guide 업데이트 포인트

- README 관리 블록 갱신
- `UPSTREAM-SNAPSHOT.md` 갱신
- `SYNC-LOG.md` 갱신
- 개요 문서 재작성

## 변경 파일 샘플

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
