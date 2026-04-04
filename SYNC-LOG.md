## public-doc-sanitizer 정리 완료
- 날짜: 2026-04-04
- 대상: markdown 문서(.md) 8개 + `.gitignore`, `.omx/` 런타임 산출물 정리
- 치환 요약: 경로 0, 이메일 0, 전화번호 41
- 변경 파일: `.gitignore`, `README.md`, `SYNC-LOG.md`, `UPSTREAM-SNAPSHOT.md`, `02-glossary.md`, `01_Foundations/02-설치와-첫-실행.md`, `sections/01-overview.md`, `obsidian/clawhip Guide/03 Glossary.md`, `obsidian/clawhip Guide/Foundations/설치와 첫 실행.md`
- 사전 검증: dry-run 1회 → 실제 반영 1회 수행 완료
- README 공개 감사: 절대경로/이메일/전화번호 패턴 없음(재확인 통과)
- 비고: `.omx/` 샘플 경로는 공개 가이드 예시 목록으로 유지

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
- `.omx/logs/hooks-[REDACTED_PHONE].jsonl`
- `.omx/logs/notify-fallback-[REDACTED_PHONE].jsonl`
- `.omx/logs/notify-fallback-[REDACTED_PHONE].jsonl`
- `.omx/logs/notify-hook-[REDACTED_PHONE].jsonl`
- `.omx/logs/omx-[REDACTED_PHONE].jsonl`
- `.omx/logs/tmux-hook-[REDACTED_PHONE].jsonl`
- `.omx/logs/turns-[REDACTED_PHONE].jsonl`
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
- `.omx/state/sessions/omx-[REDACTED_PHONE]-69uz5f/AGENTS.md`
- `.omx/state/sessions/omx-[REDACTED_PHONE]-69uz5f/autopilot-state.json`
