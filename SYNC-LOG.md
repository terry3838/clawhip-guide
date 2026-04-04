# Sync Log — clawhip

## latest cycle

- previous source sha: `098ecf6b01d743a68a60d1ec77c0539b64e2f16a`
- current source sha: `818531d3002090c9a9d0528ad929f22df267d522`
- mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드

## decision

origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드.

## upstream commits reviewed

- `818531d Merge pull request #126 from Yeachan-Heo/release/0.5.1-prep`
- `2bbf9a1 Merge origin/main into release/0.5.1-prep for main release sync`
- `9986b08 Reduce clawhip session skills to launch mechanics`
- `8677a89 Make clawhip docs the source of truth for OMC/OMX operators`
- `3879e40 Fix OMX native hook bridge install layout for real plugin validation`
- `679b9e7 Surface the native OMX bridge as the default release path`
- `286b775 Prepare the 0.5.1 branch metadata for a tagged release`
- `96db180 feat: add managed cron jobs and native cron entrypoint (#116) (#117)`

## evidence

- source remote: `https://github.com/Yeachan-Heo/clawhip.git`
- docs/interesting dirs: docs/, skills/, plugins/, src/, tests/
- changed file sample:
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
