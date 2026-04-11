# clawhip 개요

## repo 역할

- repo: `clawhip`
- source: `https://github.com/Yeachan-Heo/clawhip.git`
- version basis: `0.6.6`
- latest synced commit: `f983e1163f52`

## 지금 기준의 핵심 변화

이번 기준선에서 clawhip은 단순 알림 도구보다 **운영 검증을 내장한 notification runtime** 쪽으로 더 선명해졌어요.

특히 중요한 변화는 네 가지예요.

1. `clawhip config verify-bindings`가 들어왔어요.
2. `clawhip setup --bind ... --expect-name ...`가 live Discord 조회 기반으로 더 안전해졌어요.
3. `channel_name` 힌트가 route/default/monitor 설정에 추가됐어요.
4. `clawhip release preflight`가 release workflow gate로 올라왔어요.

## 왜 guide를 고쳤나

기존 frontdoor는 clawhip의 router 성격은 잘 잡았지만,
**binding verification / safer binding write / release preflight**를 현재 운영 흐름의 중심으로 충분히 올리지 못했어요.

그래서 이번에는 다음을 더 분명히 했어요.

- 설치보다 검증이 먼저라는 점
- repo → channel binding이 live state로 확인된다는 점
- release hygiene가 공식 표면이라는 점

## 학습자가 먼저 이해할 것

- clawhip은 daemon-first router예요
- route drift는 운영 장애로 바로 이어질 수 있어요
- `verify-bindings`와 `setup --bind`는 지금 가장 실무적인 첫 표면이에요
- `release preflight`는 운영자용 부가 기능이 아니라 현재 릴리즈 계약이에요

## 다음 읽기

- 처음 읽기: `README.md`
- 운영 붙이기: `sections/04-routing.md`, `sections/05-operations.md`
- 실전 확인: `03_Operations/03-라이브-검증.md`
