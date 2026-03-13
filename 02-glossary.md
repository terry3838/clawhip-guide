# clawhip 용어집

## daemon-first

사용자가 매번 직접 처리하지 않아도, 데몬이 계속 살아 있으면서 이벤트를 받아서 라우팅하는 운영 모델입니다.

## typed event pipeline

외부 입력을 그대로 다루지 않고, 내부에서 의미가 분명한 typed event로 정규화해서 처리하는 파이프라인입니다.

## source

이벤트를 생산하는 입력 모듈입니다. clawhip에는 git, GitHub, tmux 같은 소스가 있습니다.

## dispatcher

큐에서 이벤트를 꺼내서 router -> renderer -> sink 흐름을 실행하는 중앙 조정자입니다.

## router

어떤 이벤트를 어디로 보낼지 결정하는 계층입니다. 하나의 이벤트가 여러 delivery로 확장될 수 있습니다.

## renderer

이벤트를 Discord/Slack에 보낼 메시지 형태로 바꾸는 계층입니다. `compact`, `inline`, `alert`, `raw` 같은 형식이 여기에 해당합니다.

## sink

실제 전송 계층입니다. 예를 들어 Discord sink는 REST API나 webhook으로 메시지를 전달합니다.

## delivery

특정 이벤트가 특정 채널/싱크/포맷/mention 정책을 갖고 전달되는 1회 전송 단위입니다.

## native event contract

OMC/OMX 같은 외부 시스템이 clawhip에 이벤트를 보낼 때 따르는 정규화된 계약입니다. 최근에는 `session.*` 계열이 권장됩니다.

## memory offload

`MEMORY.md`를 hot pointer layer로 작게 유지하고, 자세한 기억은 `memory/` 하위 파일로 분리하는 문서/운영 패턴입니다.

## tmux watch

기존 tmux 세션을 감시 대상으로 등록해 keyword/stale 이벤트를 clawhip가 전달하도록 만드는 표면입니다.

## tmux wrapper

`clawhip tmux new`처럼 세션 생성과 감시 등록을 함께 처리하는 연동 표면입니다.

## dynamic tokens

템플릿 안에서 `tmux_tail`, `file_tail`, `env`, `now` 같은 동적 값을 치환하는 기능입니다.

## route preset family

GitHub issue, PR, tmux keyword 같은 흔한 운영 시나리오를 묶어 둔 라우팅/검증 기준 집합입니다.

## lifecycle surface

`install`, `update`, `uninstall`, `status`처럼 runtime 운영 주기 전반을 다루는 명령어 집합입니다.
