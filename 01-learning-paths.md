# clawhip 학습 경로

clawhip은 지금 **설치형 알림 도구**로 배우면 금방 헷갈려요.
먼저 **runtime**, 그 다음 **binding 검증**, 그 다음 **release hygiene** 순서로 보는 편이 맞아요.

## 빠른 입문 트랙

목표:
- clawhip을 daemon-first router로 이해해요
- `verify-bindings`와 `setup --bind`의 의미를 잡아요

읽는 순서:
1. `README.md`
2. `sections/01-overview.md`
3. `sections/02-install.md`
4. `02-glossary.md`

실습:
```bash
clawhip status
clawhip config verify-bindings
```

성공 기준:
- `send tool`이 아니라 runtime이라고 설명할 수 있어요
- binding drift를 왜 먼저 봐야 하는지 설명할 수 있어요

## 운영자 트랙

목표:
- repo/channel binding을 안전하게 관리해요
- live verification과 route hygiene를 운영 루프에 넣어요

읽는 순서:
1. `sections/04-routing.md`
2. `sections/05-operations.md`
3. `03_Operations/03-라이브-검증.md`
4. upstream `CHANGELOG.md`

실습:
```bash
clawhip setup --bind oh-my-codex=1480171106324189335 --expect-name oh-my-codex=omx-dev
clawhip config verify-bindings --json
```

성공 기준:
- `channel_name`이 왜 도움이 되는지 설명할 수 있어요
- repo → channel binding을 live state 기준으로 검증할 수 있어요

## 릴리즈 담당 트랙

목표:
- runtime 운영과 release hygiene를 같이 봐요

읽는 순서:
1. `sections/05-operations.md`
2. upstream `CHANGELOG.md`
3. `UPSTREAM-SNAPSHOT.md`

실습:
```bash
clawhip release preflight
```

성공 기준:
- `Cargo.toml`, `Cargo.lock`, `CHANGELOG`, tag 정합성이 왜 중요한지 설명할 수 있어요
- release preflight를 로컬/CI 앞단에 넣을 수 있어요

## 추천 읽기 순서 요약

- 처음 배우기: `README.md` → `sections/01-overview.md` → `sections/02-install.md`
- 운영 붙이기: `sections/04-routing.md` → `sections/05-operations.md`
- 검증/출시: `03_Operations/03-라이브-검증.md` → `CHANGELOG.md`
