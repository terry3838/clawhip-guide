# Sync Log — clawhip

## latest cycle

- previous source sha: `f22fb28a61051798dababea058045ad578a6a8df`
- current source sha: `c4eb931bcd2c4cb3cd5fbd7d71601b44954b9043`
- mode: `update`
- impact labels: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증

## decision

origin 변경 파일을 기준으로 guide 문서의 관련 섹션을 다시 읽고 반영했습니다. 핵심 영향 영역: README/소개, 설치/설정, CLI/명령어, 문서 구조, 스킬/플러그인, 소스코드, 테스트/검증.

## upstream commits reviewed

- `c4eb931 Bring 0.6.0 onto main so release consumers can use the provider-native hook path`
- `66ba2a2 Prepare 0.6.0 so provider-native hooks can ship cleanly`
- `a539942 omx(team): auto-checkpoint worker-2 [unknown]`
- `adf39fe omx(team): auto-checkpoint worker-2 [unknown]`
- `5556636 omx(team): auto-checkpoint worker-2 [unknown]`
- `26f2124 omx(team): auto-checkpoint worker-2 [unknown]`
- `3ae80a1 omx(team): auto-checkpoint worker-2 [unknown]`
- `b06cc87 omx(team): auto-checkpoint worker-2 [unknown]`

## evidence

- source remote: `https://github.com/Yeachan-Heo/clawhip.git`
- docs/interesting dirs: docs/, skills/, plugins/, src/, tests/
- changed file sample:
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
