# clawhip 개요

## 원본 저장소 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- latest synced commit: `c4eb931bcd2c`
- summary: > **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## 이번 싸이클 판단

- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증
- 판단: origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증.

## 최근 upstream 커밋

- `c4eb931 Bring 0.6.0 onto main so release consumers can use the provider-native hook path`
- `66ba2a2 Prepare 0.6.0 so provider-native hooks can ship cleanly`
- `a539942 omx(team): auto-checkpoint worker-2 [unknown]`
- `adf39fe omx(team): auto-checkpoint worker-2 [unknown]`
- `5556636 omx(team): auto-checkpoint worker-2 [unknown]`
- `26f2124 omx(team): auto-checkpoint worker-2 [unknown]`

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
