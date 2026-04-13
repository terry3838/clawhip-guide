# Sync Log — clawhip

## latest cycle

- previous source sha: `f983e1163f52c976fdfb022dbaefca02019b5237`
- current source sha: `ff3ba32dc22a143d53bec40870d3b52b2fa11a2b`
- mode: `update`
- impact labels: README/소개, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드

## decision

origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드.

## upstream commits reviewed

- `ff3ba32 Remove stale main-only non-git native hook drop path`
- `2d98d3f Align main-only merge leftovers with the verified 0.6.7 hook contract`
- `30e5115 Restore daemon/native-hook compatibility constants for main merge`
- `b4bde03 Merge dev into main for v0.6.7`
- `23e666a Merge release 0.6.7 native hook reliability fixes into dev`
- `07f58aa Drop pending batches on shutdown to keep daemon restarts fresh-only`
- `780c529 Prevent stale hook noise and replayed events from polluting sessions`
- `6740c9f omx(team): merge worker-1`

## evidence

- source remote: `https://github.com/Yeachan-Heo/clawhip.git`
- docs/interesting dirs: docs/, skills/, plugins/, src/, tests/
- changed file sample:
- `CHANGELOG.md`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `docs/event-contract-v1.md`
- `docs/live-verification.md`
- `docs/native-event-contract.md`
- `integrations/omx/README.md`
- `scripts/internal-pr-format-gate.sh`
- `skills/omc/SKILL.md`
- `skills/omx/SKILL.md`
- `src/cli.rs`
- `src/cron.rs`
- `src/daemon.rs`
- `src/dispatch.rs`
- `src/hooks/mod.rs`
- `src/hooks/prompt_deliver.rs`
- `src/native_hooks.rs`
- `src/router.rs`
- `src/source/github.rs`
