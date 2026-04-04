# clawhip 용어집

이 문서는 clawhip을 읽을 때 자주 나오는 용어를 **운영자/학습자 관점**에서 짧고 명확하게 정리한 사전이다.

---

## A

### agent.*

**정의:** clawhip에서 오래전부터 쓰이던 agent lifecycle 이벤트 family.

예:
- `agent.started`
- `agent.blocked`
- `agent.finished`
- `agent.failed`

**현재 위치:**
여전히 지원되지만, OMC/OMX native routing에선 `session.*`가 새 기본 계약에 가깝다.

---

## C

### clawhip

**정의:** daemon-first notification router.

**한 줄 설명:**
여러 운영 이벤트를 받아 정규화하고, 라우팅/렌더링/전송까지 맡는 runtime.

---

### custom event

**정의:** 특정 source(git/GitHub/tmux)가 아닌, 사용자가 직접 보내는 임의 이벤트.

**대표 명령:**
```bash
clawhip send --channel <id> --message "text"
```

**의미:**
가장 단순한 thin client ingress다.

---

## D

### daemon-first

**정의:** CLI가 매번 직접 일을 끝내는 방식이 아니라, 백그라운드 daemon이 중심이 되어 이벤트를 계속 받아 처리하는 운영 모델.

**왜 중요하나:**
clawhip의 본질이 단발성 메시지 전송이 아니라 지속 라우팅 runtime이라는 걸 보여준다.

---

### delivery

**정의:** 특정 이벤트가 특정 route에 매칭되어 실제 전송 대상으로 풀린 1회 단위 결과.

**중요 포인트:**
이벤트 하나가 0개, 1개, 혹은 여러 delivery로 fan-out될 수 있다.

---

### dispatcher

**정의:** queue에서 이벤트를 받아 route를 찾고, render하고, sink로 넘기는 중앙 조정자.

**쉽게 말하면:**
clawhip의 실질적인 traffic controller.

---

### dynamic tokens

**정의:** 템플릿 안에서 이벤트 외 추가 정보를 동적으로 삽입하는 기능.

예:
- `{repo}`
- `{number}`
- `{session}`
- `{tmux_tail:session:lines}`
- `{file_tail:/path:lines}`
- `{env:NAME}`
- `{now}`

**안전장치:**
route-level opt-in, allowlist, timeout, output cap이 있다.

---

## E

### event family

**정의:** 비슷한 타입의 이벤트를 묶는 이름 공간.

예:
- `github.*`
- `git.*`
- `tmux.*`
- `session.*`
- `agent.*`

**왜 중요하나:**
route 작성이 이 family 단위로 이뤄지는 경우가 많다.

---

### extracted sources

**정의:** git/GitHub/tmux 같은 입력 생산 계층이 각 source 모듈로 분리된 구조.

**의미:**
모니터링 로직과 라우팅/전송 로직이 덜 엉킨다.

---

## F

### filesystem-offloaded memory

**정의:** `MEMORY.md`를 작은 hot pointer/index 레이어로 두고, 상세 기억을 `memory/` 파일들로 분리하는 운영 패턴.

**clawhip에서의 위치:**
단순 문서 팁이 아니라, `clawhip memory init/status`와 docs/skills로 제공되는 운영 모델이다.

---

## G

### GitHub polling source

**정의:** GitHub webhook만이 아니라 polling 방식으로 issue/PR 변화를 감시하는 source.

**최근 포인트:**
private repo polling 관련 수정이 최근 upstream에 포함됐다.

---

## I

### ingress

**정의:** 이벤트가 clawhip로 들어오는 입력 지점.

예:
- CLI thin client
- webhook
- git source
- GitHub source
- tmux source

---

### install lifecycle

**정의:** 설치뿐 아니라 `install`, `update`, `uninstall`, `status`까지 포함한 운영 lifecycle 표면.

**관련 명령:**
```bash
clawhip install
clawhip update --restart
clawhip uninstall
clawhip status
```

---

## L

### live verification

**정의:** 설치 후 실제 preset event family가 end-to-end로 동작하는지 실 이벤트로 검증하는 운영 runbook.

**왜 중요하나:**
clawhip에선 “설치됨”보다 “실제 채널까지 흐름이 간다”가 더 중요하다.

---

### lifecycle surface

**정의:** runtime의 생성/업데이트/상태 확인/제거를 다루는 명령 집합.

즉 단순 기능 명령이 아니라 운영 주기 전체를 다루는 표면이다.

---

## M

### memory offload

**정의:** filesystem-offloaded memory 패턴의 줄임 표현.

**관련 명령:**
```bash
clawhip memory init ...
clawhip memory status ...
```

---

### mpsc queue

**정의:** source들이 생산한 이벤트를 dispatcher가 소비하기 전까지 쌓아두는 비동기 큐.

**의미:**
여러 source를 느슨하게 연결하는 핵심 구조.

---

## N

### native event contract

**정의:** OMC/OMX 등 외부 시스템이 clawhip로 이벤트를 보낼 때 따르는 정규화 계약.

**현재 핵심:**
새로운 native routing은 `session.*` family를 우선 사용한다.

**문서:**
- `docs/native-event-contract.md`

---

## O

### OMC / OMX routing

**정의:** oh-my-claudecode / oh-my-codex 같은 상위 런타임이 직접 채널에 메시지를 보내지 않고, clawhip로 event를 emit해서 라우팅/포맷팅/mention 정책을 위임하는 방식.

**철학:**
상위 도구는 event producer, clawhip는 routing/delivery owner.

---

## P

### plugin architecture

**정의:** tool-specific bridge를 plugin 단위로 다루는 구조.

보통 각 plugin은:
- `plugin.toml`
- `bridge.sh`

로 구성된다.

**예시:**
- `plugins/codex/`
- `plugins/claude-code/`

---

### preset family

**정의:** 자주 쓰는 이벤트 시나리오를 event family/preset 단위로 묶어 이해하는 방법.

예:
- GitHub issue family
- PR family
- tmux keyword/stale family
- session lifecycle family

---

## R

### renderer

**정의:** 이벤트를 사람이 읽을 메시지 형태로 바꾸는 계층.

예:
- `compact`
- `alert`
- `inline`
- `raw`

**의미:**
전송 계층(sink)과 포맷 계층이 분리된다.

---

### repo-local install

**정의:** clone한 저장소 안에서 `./install.sh` 또는 `clawhip install`을 통해 설치하는 운영자 친화적 설치 경로.

**언제 좋나:**
- local clone을 유지하며 운영할 때
- systemd / local workflow까지 같이 관리할 때

---

### route

**정의:** 특정 event family와 filter가 매칭될 때, 어떤 sink/channel/format/mention/template를 적용할지 정의하는 규칙.

**예시:**
```toml
[[routes]]
event = "github.*"
filter = { repo = "clawhip" }
sink = "discord"
channel = "[REDACTED_PHONE]"
format = "compact"
```

---

### router

**정의:** 이벤트에 대해 어떤 route들이 맞는지 계산하고 delivery 목록을 만드는 계층.

**중요 포인트:**
first-match 하나만 찾는 게 아니라 여러 매칭을 만들 수 있다.

---

## S

### session.*

**정의:** OMC/OMX native routing에서 권장되는 session lifecycle 이벤트 family.

예:
- `session.started`
- `session.blocked`
- `session.finished`
- `session.failed`
- `session.pr-created`

**현재 위치:**
신규 native routing에선 `agent.*`보다 우선 추천된다.

---

### sink

**정의:** 실제 메시지를 외부 채널로 전달하는 transport 계층.

현재 대표 예:
- Discord sink
- Slack sink

---

### source

**정의:** 이벤트를 생산하는 입력 모듈.

예:
- `GitSource`
- `GitHubSource`
- `TmuxSource`

---

## T

### thin client

**정의:** 복잡한 로직 없이 daemon에 이벤트를 전달하는 얇은 CLI 표면.

예:
- `clawhip send`
- `clawhip github ...`
- `clawhip git ...`
- `clawhip agent ...`

---

### tmux watch

**정의:** 이미 존재하는 tmux 세션을 감시 대상으로 등록하는 표면.

**예시:**
```bash
clawhip tmux watch -s issue-123 --channel ... --keywords "error,complete"
```

---

### tmux wrapper

**정의:** tmux 세션 생성과 감시 등록을 함께 다루는 표면.

**예시:**
```bash
clawhip tmux new -s issue-123 --channel ... -- 'source ~/.zshrc && omx --madmax'
```

---

### typed event pipeline

**정의:** 들어오는 다양한 입력을 의미가 분명한 내부 typed event로 변환하고, 그 후 라우팅/렌더링/전송으로 넘기는 구조.

**clawhip 핵심 정체성 중 하나다.**

---

## 빠른 참조 표

| 용어 | 짧은 의미 |
|------|-----------|
| clawhip | daemon-first notification router |
| daemon-first | 백그라운드 daemon 중심 운영 모델 |
| typed event pipeline | 입력을 typed event로 정규화하는 구조 |
| source | 이벤트 생산자 |
| dispatcher | 중앙 조정자 |
| router | route resolution 계층 |
| renderer | 메시지 포맷 계층 |
| sink | 실제 채널 전송 계층 |
| delivery | route 매칭 결과로 나온 1회 전송 단위 |
| thin client | daemon으로 이벤트를 보내는 얇은 CLI |
| session.* | 신규 native routing 권장 family |
| agent.* | 레거시 호환 family |
| native event contract | 외부 런타임과의 정규화 계약 |
| tmux watch | 기존 tmux 세션 감시 등록 |
| tmux wrapper | 세션 생성+감시 통합 표면 |
| live verification | 실전 이벤트 기반 end-to-end 검증 |
| memory offload | filesystem-based memory 운영 패턴 |
| plugin architecture | tool-specific bridge 확장 구조 |
