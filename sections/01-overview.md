# clawhip 개요

## 원본 저장소 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- latest synced commit: `ff3ba32dc22a`
- summary: > **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## 이번 싸이클 판단

- sync mode: `update`
- impact labels: README/소개, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드
- 판단: origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드.

## 최근 upstream 커밋

- `ff3ba32 Remove stale main-only non-git native hook drop path`
- `2d98d3f Align main-only merge leftovers with the verified 0.6.7 hook contract`
- `30e5115 Restore daemon/native-hook compatibility constants for main merge`
- `b4bde03 Merge dev into main for v0.6.7`
- `23e666a Merge release 0.6.7 native hook reliability fixes into dev`
- `07f58aa Drop pending batches on shutdown to keep daemon restarts fresh-only`

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
