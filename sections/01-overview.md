# clawhip 개요

## 원본 저장소 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- latest synced commit: `f983e1163f52`
- summary: > **⭐ Optional support:** the interactive repo-local install paths (`./install.sh` and `clawhip install` from a clone) can offer to star this repo after a successful install when `gh` is installed and authenticated. Skip it with `--skip-star-prompt` or `CLAWHIP_SKIP_STAR_PROMPT=1`.

## 이번 싸이클 판단

- sync mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 스킬/플러그인, 소스코드, 테스트/검증
- 판단: origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 스킬/플러그인, 소스코드, 테스트/검증.

## 최근 upstream 커밋

- `f983e11 Preserve the 0.6.6 release state while finishing the dev->main merge`
- `63221e1 release: 0.6.6`
- `251dda5 Merge pull request #199 from Yeachan-Heo/clawhip-issue-198-binding-verify`
- `8ab8436 fix(setup): hard-fail malformed --expect-name entries (closes #198 review)`
- `3025a36 style: cargo fmt`
- `ceb93e2 feat(setup): verify Discord channel bindings against live server (closes #198)`

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
