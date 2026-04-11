# clawhip 용어집

## binding verification

현재 config에 들어 있는 Discord channel binding이 실제 서버 상태와 맞는지 확인하는 점검 단계예요.
대표 명령은 `clawhip config verify-bindings`예요.

## `setup --bind`

repo를 특정 Discord 채널에 연결하는 setup surface예요.
지금 버전에서는 단순 기록이 아니라 **실제 채널 조회 + 이름 검증**까지 포함해요.

## `channel_name`

channel ID 옆에 남기는 사람이 읽기 쉬운 힌트예요.
라우팅 엔진의 필수 키는 아니지만, 운영자가 drift를 찾거나 설정을 검토할 때 매우 유용해요.

## release preflight

릴리즈 직전에 `Cargo.toml`, `Cargo.lock`, `CHANGELOG`, tag 정합성을 확인하는 점검 단계예요.
현재 clawhip 운영 흐름에서는 runtime과 release hygiene가 분리되지 않아요.

## daemon-first

사용자가 매번 직접 전송하지 않아도, daemon이 계속 살아 있으면서 이벤트를 받아 처리하는 운영 모델이에요.

## typed event pipeline

Git, GitHub, tmux, provider hook 같은 여러 입력을 내부 event contract로 정규화해서 처리하는 구조예요.

## route / renderer / sink

- route: 어떤 이벤트를 어디로 보낼지 결정해요
- renderer: 사람이 읽을 메시지 형태로 바꿔요
- sink: 실제 채널로 전송해요

## live verification

설치 완료보다 실제 알림 흐름이 end-to-end로 동작하는지 확인하는 운영 습관이에요.
지금 clawhip은 이 검증 철학이 강해요.
