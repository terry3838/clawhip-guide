# clawhip 학습 가이드

> event를 받아, 검증하고, 라우팅하고, 사람이 읽을 운영 메시지로 보내는 daemon-first notification runtime

`clawhip`은 단순 Discord 알림 스크립트가 아니에요. 지금 기준의 clawhip은 **provider-native hook, route-aware delivery, live binding verification, release preflight**까지 포함한 운영 런타임으로 읽는 편이 맞아요.

이 가이드는 upstream `README.md`, `CHANGELOG.md`, `Cargo.toml`, top-level 구조를 다시 읽어서, **무엇이 핵심인지 / 무엇이 최근에 바뀌었는지 / 어디부터 읽어야 덜 헷갈리는지**를 학습용으로 재구성해요.

## 버전 기준

- upstream 기준 커밋: `f983e11`
- crate version: `0.6.6`
- 이번에 꼭 반영한 변화
  - `clawhip config verify-bindings`
  - `clawhip setup --bind ... --expect-name ...`
  - `channel_name` 힌트 필드
  - `clawhip release preflight`

## clawhip을 한 문장으로 보면

**Git/GitHub/tmux/provider hook에서 들어온 운영 이벤트를 typed contract로 정규화하고, route 정책에 따라 Discord 같은 채널로 안전하게 전달하는 daemon-first router**예요.

즉, 핵심은 세 가지예요.

1. 입력을 이벤트로 통일해요.
2. 라우팅과 렌더링을 분리해요.
3. 실제 운영에서 잘못된 바인딩과 릴리즈 실수를 미리 막아요.

## 왜 지금 다시 읽어야 하나

### 1. 설치보다 검증이 더 중요해졌어요

최근 clawhip은 설치 성공보다 **실제 바인딩이 맞는지**를 더 강하게 확인해요.

- `clawhip config verify-bindings`는 현재 config의 channel ID가 실제 Discord 상태와 맞는지 점검해요.
- drift가 있으면 non-zero로 끝나서 CI나 운영 점검에 바로 넣을 수 있어요.

### 2. `setup --bind`가 이제 더 안전해졌어요

`clawhip setup --bind REPO=CHANNEL_ID --expect-name REPO=NAME`는
그냥 값만 쓰지 않고, **실제 채널을 Discord에서 조회한 뒤** 이름까지 맞는지 보고 저장해요.

즉 “channel id만 맞으면 됨”이 아니라,
**repo → channel 라우팅을 live state 기준으로 검증한 뒤 쓴다**가 현재 철학이에요.

### 3. `channel_name`은 장식이 아니라 운영 힌트예요

새 `channel_name`은 강제 필드는 아니지만,
`[[routes]]`, `[defaults]`, `[[monitors.git.repos]]`, `[[monitors.tmux.sessions]]`에서
사람이 설정을 읽고 drift를 찾는 속도를 높여줘요.

### 4. release preflight가 운영 루프에 들어왔어요

`clawhip release preflight`는 `Cargo.toml`, `Cargo.lock`, `CHANGELOG`, tag 정합성을 확인해요.
즉 지금의 clawhip은 runtime뿐 아니라 **release hygiene**까지 공식 표면으로 가져왔어요.

## 추천 읽기 순서

1. `sections/01-overview.md`
2. `sections/02-install.md`
3. `sections/04-routing.md`
4. `sections/05-operations.md`
5. `02-glossary.md`
6. upstream `README.md`, `CHANGELOG.md`

더 깊게 보려면:
- `01_Foundations/02-설치와-첫-실행.md`
- `02_Runtime-Internals/02-이벤트와-라우팅.md`
- `03_Operations/03-라이브-검증.md`

## 가장 현실적인 첫 성공 루프

```bash
clawhip status
clawhip config verify-bindings
clawhip setup --bind oh-my-codex=1480171106324189335 --expect-name oh-my-codex=omx-dev
clawhip release preflight
```

이 루프가 의미하는 건 이거예요.

- daemon이 살아 있는지 본다
- 현재 route binding drift를 본다
- repo → channel 매핑을 live verify 후 저장한다
- 릴리즈 직전 정합성을 확인한다

## 자주 생기는 오해

- **오해 1: clawhip은 Discord 전송 CLI다**
  - 아니에요. 지금 기준 핵심은 typed event pipeline + route/delivery runtime이에요.

- **오해 2: tmux가 본체다**
  - 아니에요. tmux는 여전히 중요하지만, provider-native hook과 route/runtime 계층이 더 중심이에요.

- **오해 3: setup이 끝나면 운영 준비도 끝난다**
  - 아니에요. binding verification과 release preflight까지 포함해야 현재 운영 흐름에 맞아요.

## 이 가이드가 특히 도와주는 사람

- Discord 운영 채널에 repo별 알림을 안정적으로 붙이려는 사람
- OMC/OMX/OpenClaw 이벤트를 clawhip 쪽으로 정리하려는 사람
- route drift, binding mismatch, 릴리즈 전 정합성까지 같이 다루려는 운영자

## 다음 행동

- 입문이면 `01-learning-paths.md`부터 읽고, 바로 `clawhip config verify-bindings`를 돌려 보세요.
- 운영 중이면 `sections/05-operations.md`와 `03_Operations/03-라이브-검증.md`를 먼저 보세요.

<!-- GUIDE_SYNC:START -->
## 자동 동기화 상태

- origin repo: `clawhip`
- latest source commit: `f983e1163f52`
- sync mode: `no-change`
- 영향 분류: 일반 변경

### 이번 반영 포인트

이번 싸이클에서는 origin 변경이 없어 guide 본문은 유지했고, 동기화 기준점만 재확인했습니다.

### 최근 upstream 커밋

- `f983e11 Preserve the 0.6.6 release state while finishing the dev->main merge`
- `63221e1 release: 0.6.6`
- `251dda5 Merge pull request #199 from Yeachan-Heo/clawhip-issue-198-binding-verify`
- `8ab8436 fix(setup): hard-fail malformed --expect-name entries (closes #198 review)`
- `3025a36 style: cargo fmt`
- `ceb93e2 feat(setup): verify Discord channel bindings against live server (closes #198)`

### 변경 파일 샘플

- 이번 싸이클에서는 신규 변경 파일이 없습니다.

> 이 블록은 guide sync가 자동 갱신합니다.
<!-- GUIDE_SYNC:END -->
