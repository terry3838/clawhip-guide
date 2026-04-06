# Sync Log — clawhip

## latest cycle

- previous source sha: `818531d3002090c9a9d0528ad929f22df267d522`
- current source sha: `f22fb28a61051798dababea058045ad578a6a8df`
- mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증

## decision

origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증.

## upstream commits reviewed

- `f22fb28 Merge remote-tracking branch 'origin/dev'`
- `04d3335 chore: prepare 0.5.4 release`
- `4f57245 Merge remote-tracking branch 'origin/dev'`
- `d5e4f70 Merge pull request #149 from Yeachan-Heo/clawhip-issue-148-clean-embedded-state`
- `931cf47 fix: remove embedded worktree and local agent state from repo`
- `8c7e881 Merge pull request #144 from Yeachan-Heo/feat/omc-omx-hooks-dev`
- `8a842dc fix: satisfy fmt and clippy for native hooks launch PR`
- `3ac8e01 fix: custom event channel takes precedence over route/default channel (#145)`

## evidence

- source remote: `https://github.com/Yeachan-Heo/clawhip.git`
- docs/interesting dirs: docs/, skills/, plugins/, src/, tests/
- changed file sample:
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
