# clawhip 개요

## 원본 저장소 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- latest synced commit: `f22fb28a6105`
- summary: > **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## 이번 싸이클 판단

- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증
- 판단: origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증.

## 최근 upstream 커밋

- `f22fb28 Merge remote-tracking branch 'origin/dev'`
- `04d3335 chore: prepare 0.5.4 release`
- `4f57245 Merge remote-tracking branch 'origin/dev'`
- `d5e4f70 Merge pull request #149 from Yeachan-Heo/clawhip-issue-148-clean-embedded-state`
- `931cf47 fix: remove embedded worktree and local agent state from repo`
- `8c7e881 Merge pull request #144 from Yeachan-Heo/feat/omc-omx-hooks-dev`

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
- `hooks/`
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

- `.github/workflows/release.yml`
- `.gitignore`
- `CHANGELOG.md`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `dist-workspace.toml`
- `docs/canonical-contract-cleanup.md`
- `hooks/omc/clawhip-session-init.mjs`
- `hooks/omc/clawhip-session-stop.mjs`
- `hooks/omx/clawhip-session-init.mjs`
- `hooks/omx/clawhip-session-stop.mjs`
- `skills/omx/create.sh`
- `src/cli.rs`
- `src/config.rs`
- `src/cron.rs`
- `src/daemon.rs`
- `src/dispatch.rs`
- `src/events.rs`
- `src/hooks/mod.rs`
