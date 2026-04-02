# clawhip 학습 가이드

> *events in, messages out.*

clawhip은 **daemon-first notification router** 입니다. Git, GitHub, tmux, OMC/OMX 같은 운영 이벤트를 받아 **typed event pipeline** 으로 정규화하고, router → renderer → sink 흐름으로 Discord/Slack 같은 채널에 전달합니다.

이 가이드는 원본 저장소 `clawhip`을 직접 대조해서, 설치법만이 아니라 **왜 이 도구가 필요한지 / 내부에서 무엇이 어떻게 움직이는지 / 실제 운영에선 어떻게 써야 하는지**를 학습용으로 다시 정리한 문서입니다.

> 버전 기준
> - upstream 확인 커밋: `098ecf6b01d7`
> - Cargo package version: `0.5.0`
> - 중요한 해석 포인트:
>   - README / Cargo.toml 기준 최신 릴리스 축은 `v0.5.0`
>   - `ARCHITECTURE.md`는 아직 `v0.4.0` 기준 설명이 남아 있어서, 학습 시 **문서 버전 드리프트**를 감안해야 함

---

## clawhip을 한 문장으로 말하면

clawhip은 **“이벤트를 사람이 읽기 쉬운 운영 메시지로 바꿔 채널에 안정적으로 보내는 라우팅 런타임”** 이다.

조금 더 풀면:

- **daemon-first** — 사용자가 매번 직접 전송하지 않아도, 백그라운드 데몬이 계속 살아서 처리한다
- **typed event pipeline** — 들어온 입력을 내부 event contract로 정규화한다
- **router / renderer / sink 분리** — 어디로 보낼지, 어떻게 그릴지, 어떤 채널로 전달할지를 나눠서 관리한다
- **운영 통합 지향** — Git/GitHub/tmux/OMC/OMX/OpenClaw 같은 운영 표면과 자연스럽게 붙는다

즉 “Discord 알림 보내는 스크립트”가 아니라, **운영 이벤트 전달 계층**에 가깝다.

---

## clawhip이 해결하는 문제

실제 운영에서는 이런 문제가 자주 생긴다.

- git commit, PR 변경, tmux 에러, 세션 완료 같은 이벤트가 여기저기 흩어져 있음
- 각 도구가 직접 Slack/Discord를 쏘면 포맷도 들쭉날쭉하고 mention 정책도 제각각임
- 특정 repo / issue / worker / tmux session 에 대해서만 라우팅하고 싶은데 필터가 불안정함
- 봇/에이전트가 직접 메시지를 보내면 운영 로직과 delivery 로직이 뒤엉킴

clawhip은 이걸 이렇게 정리한다.

1. **입력은 이벤트로 통일**
2. **이벤트는 typed contract로 정규화**
3. **라우팅은 clawhip이 전담**
4. **포맷/mention/채널 정책도 clawhip이 전담**
5. 상위 런타임(OMC/OMX/OpenClaw)은 **이벤트만 내보내면 됨**

이게 핵심 가치다.

---

## 핵심 개념 6개

### 1. daemon-first

사용자가 매번 CLI로 수동 전송하지 않아도, daemon이 계속 떠 있으면서 이벤트를 받아 처리한다.

### 2. typed event pipeline

외부 입력을 그대로 쓰지 않고, 내부적으로 의미가 정리된 event family로 변환해서 처리한다.

예:
- `git.commit`
- `github.issue-opened`
- `github.pr-status-changed`
- `tmux.keyword`
- `session.started`
- `session.finished`

### 3. extracted sources

이벤트 생산이 source 모듈로 분리되어 있다.

- git source
- GitHub source
- tmux source

### 4. router / renderer / sink split

- **router** — 어떤 이벤트를 어디로 보낼지 결정
- **renderer** — 사람에게 보일 메시지 형태로 바꿈
- **sink** — 실제 Discord/Slack 전송

### 5. native session contract

OMC/OMX 같은 상위 런타임에서 오는 이벤트는 이제 `agent.*`보다 `session.*` 계열이 권장된다.

### 6. live verification

설치만 됐다고 끝이 아니다. issue / PR / git / tmux / install 흐름이 실제로 채널까지 가는지 **실제 이벤트로 검증**하는 운영 철학이 강하다.

---

## clawhip이 특히 잘 맞는 조합

원본 README가 강하게 밀고 있는 조합은 이거다.

### 1) OMC / OMX + tmux

예시:

```bash
clawhip tmux new -s issue-123 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,PR created,complete" \
  -- 'source ~/.zshrc && omx --madmax'
```

또는:

```bash
clawhip tmux watch -s issue-123 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,PR created,complete"
```

의미:
- 세션 시작은 OMC/OMX가 함
- 감시/알림은 clawhip이 함
- 포맷/mention/채널 정책도 clawhip이 맡음

### 2) cron → clawhip send → Discord dev channel → bot follow-up

원본 README의 recipe 핵심은, 스케줄링과 라우팅과 액션을 분리하는 것이다.

```text
system cron -> clawhip send -> Discord dev channel -> Clawdbot/OpenClaw follow-up
```

즉:
- 시간 관리: cron
- 전달 관리: clawhip
- 실제 후속 행동: bot/agent

깔끔하다.

---

## 최신 버전에서 봐야 할 포인트

README와 Cargo 기준으로 최신은 `0.5.0`이다.

최근 커밋/릴리스 흐름상 학습자가 특히 알아야 할 건:

- **Discord retry resilience** 강화
- **batched CI notifications** 추가
- **stable ingress identifiers** 보존 개선
- **private repo GitHub polling** 수정
- **native event contract polish**

즉 최근 clawhip은 “새 기능 대폭 추가”보다, **운영 신뢰성 / 안정적 ingress / CI/notification robustness** 쪽으로 성숙해지고 있다.

---

## 설치 표면 이해

clawhip은 설치 경로가 여러 개다.

### 1. crates.io

```bash
cargo install clawhip
```

Rust toolchain이 있는 사람에게 가장 직접적이다.

### 2. prebuilt installer

```bash
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/Yeachan-Heo/clawhip/releases/latest/download/clawhip-installer.sh | sh
```

Rust 없이 설치하기 좋은 경로다.

### 3. repo-local install

```bash
./install.sh
./install.sh --systemd
```

이건 clone-local operator workflow에 특히 맞는다.

### 4. runtime lifecycle commands

```bash
clawhip install
clawhip update --restart
clawhip uninstall
```

이 표면은 단순 설치보다, **운영 lifecycle** 전체를 다루는 표면으로 보는 게 맞다.

---

## 설치 후 제일 먼저 이해해야 하는 명령

```bash
clawhip                 # start daemon
clawhip status          # daemon health
clawhip send ...        # custom event thin client
clawhip github ...      # github thin client
clawhip git ...         # git thin client
clawhip agent ...       # legacy/native lifecycle emit
clawhip tmux ...        # tmux wrapper / watch / alert surface
clawhip plugin list     # installed plugins 확인
clawhip memory init     # memory scaffold 생성
clawhip memory status   # memory scaffold 상태 확인
```

학습자는 이걸 기능 목록으로 외우기보다, 아래 4분류로 보는 게 좋다.

| 분류 | 명령 |
|------|------|
| daemon/lifecycle | `clawhip`, `status`, `install`, `update`, `uninstall` |
| thin client ingress | `send`, `github`, `git`, `agent` |
| monitoring wrapper | `tmux` |
| runtime scaffolds | `plugin`, `memory` |

---

## 내부 구조를 어떻게 읽어야 하나

원본 repo에서 중요한 디렉토리는 아래다.

| 경로 | 의미 |
|------|------|
| `src/main.rs` | daemon 진입점 |
| `src/cli.rs` | CLI 표면 |
| `src/daemon.rs` | daemon 실행 계층 |
| `src/dispatch.rs` | dispatcher |
| `src/router.rs` | route resolution |
| `src/render/` | message rendering |
| `src/sink/` | Discord/Slack delivery |
| `src/source/` | git/GitHub/tmux sources |
| `src/event/` | typed event / compat normalization |
| `src/lifecycle.rs` | install/update/uninstall/status 관련 lifecycle |
| `src/memory.rs` | filesystem memory scaffold 관련 |
| `plugins/` | tool-specific shell bridge |
| `integrations/` | git/tmux integration scripts |
| `docs/` | contract/runbook/architecture 문서 |
| `skills/` | OMC/OMX/memory-offload skill assets |

### 읽기 추천 순서

1. `README.md`
2. `ARCHITECTURE.md`
3. `docs/native-event-contract.md`
4. `docs/live-verification.md`
5. `docs/memory-offload-guide.md`
6. `src/cli.rs`
7. `src/main.rs` → `src/daemon.rs`
8. `src/source/*` → `src/dispatch.rs` → `src/router.rs` → `src/render/*` → `src/sink/*`

---

## 학습자가 꼭 알아야 하는 문서 드리프트

여기서 헷갈릴 수 있는 포인트가 하나 있다.

- `Cargo.toml` version: `0.5.0`
- 최근 커밋도 `release: clawhip v0.5.0`
- 그런데 `ARCHITECTURE.md` 제목은 아직 **v0.4.0** 기준 설명

이 말은:
- 아키텍처의 큰 구조는 여전히 유효할 가능성이 높지만
- 세부 운영 포인트는 README / Cargo / 최근 커밋을 더 우선해야 한다는 뜻이다

그래서 이 guide는 **아키텍처 설명은 참고하되, 현재 동작 이해는 README와 최근 릴리스 문맥 기준**으로 정리한다.

---

## 운영 관점에서 중요한 철학

### 1. routing/formatting/delivery는 clawhip이 맡아야 한다

원본 README도 말한다.

> Direct Slack/Discord notifications inside OMC/OMX should be treated as deprecated; emit native events and let clawhip own routing, mention policy, and formatting.

이게 아주 중요하다.

즉:
- 상위 런타임이 직접 채널에 메시지 쏘지 말고
- 이벤트만 내보내고
- 채널/mention/format 정책은 clawhip에 위임하라는 철학이다

### 2. live verification이 설치만큼 중요하다

clawhip은 “설치됨”보다 “실제 preset event family가 다 흐른다”가 더 중요하다.

### 3. memory offload도 clawhip의 운영 철학 일부다

`MEMORY.md`를 hot pointer로 두고 상세 기억을 파일 shard로 넘기는 패턴이, 단순 문서 팁이 아니라 하나의 운영 모델로 정리돼 있다.

---

## 이 가이드 문서 구성

```text
clawhip-guide/
├── README.md
├── 01-learning-paths.md
├── 02-glossary.md
├── 03-repo-blueprint.md
├── 00_Home/
├── 01_Foundations/
├── 02_Runtime-Internals/
├── 03_Operations/
├── 04_Labs/
├── 05_Resources/
├── sections/
├── examples/
└── tools/
```

### 추천 읽기 순서

1. `README.md` — 전체 그림
2. `01-learning-paths.md` — 내 목적에 맞는 학습 순서 결정
3. `02-glossary.md` — 용어 모를 때 즉시 참조
4. `01_Foundations/` — 입문
5. `02_Runtime-Internals/` — 구조
6. `03_Operations/` — 실전 운영
7. `04_Labs/` — 직접 검증

---

## 가장 짧은 실습 루프

### 실습 1 — daemon 상태 보기

```bash
clawhip status
```

### 실습 2 — custom event 보내기

```bash
clawhip send --channel YOUR_CHANNEL_ID --message "hello from clawhip"
```

### 실습 3 — tmux watch 붙이기

```bash
clawhip tmux watch -s issue-123 \
  --channel YOUR_CHANNEL_ID \
  --mention "<@your-user-id>" \
  --keywords "error,complete"
```

### 실습 4 — native contract 문서 읽기

- `docs/native-event-contract.md`

### 실습 5 — live verification runbook 보기

- `docs/live-verification.md`
- `scripts/live-verify-default-presets.sh`

---

## 관련 원본 자료

- GitHub: <https://github.com/Yeachan-Heo/clawhip>
- crates.io: <https://crates.io/crates/clawhip>
- `ARCHITECTURE.md`
- `docs/native-event-contract.md`
- `docs/live-verification.md`
- `docs/memory-offload-architecture.md`
- `docs/memory-offload-guide.md`

<!-- GUIDE_SYNC:START -->
## 자동 동기화 상태

- origin repo: `clawhip`
- latest source commit: `098ecf6b01d7`
- sync mode: `no-change`
- 영향 분류: 일반 변경

### 이번 반영 포인트

이번 싸이클에서는 origin 변경이 없어 guide 본문은 유지했고, 동기화 기준점만 재확인했습니다.

### 최근 upstream 커밋

- `098ecf6 release: clawhip v0.5.0`
- `fbb3998 Implement Discord retry resilience and batched CI notifications (#88)`
- `f2b61ed chore: bump version to 0.5.0`
- `90ca553 Preserve stable ingress identifiers across normalization and enqueue responses (#82)`
- `0c18f1e Fix GitHub polling for private repos (#81)`
- `2462cb1 Merge pull request #79 from Yeachan-Heo/feat/issue-65-native-event-contract-polish`

### 변경 파일 샘플

- 이번 싸이클에서는 신규 변경 파일이 없습니다.

> 이 블록은 guide sync가 자동 갱신합니다.
<!-- GUIDE_SYNC:END -->
