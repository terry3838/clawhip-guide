# clawhip 학습 가이드

> clawhip 런타임을 한국어로 단계별 학습하기 위한 독립 가이드 저장소입니다.

clawhip은 **daemon-first Discord notification router**입니다.
Git/GitHub/tmux/OMX·OMC 같은 운영 이벤트를 받아 typed event pipeline으로
정규화하고, router → renderer → sink 흐름으로 Discord/Slack 등에 전달합니다.

이 가이드는 `/home/terry/guide/clawhip` 런타임 저장소를 직접 분석해,
학습자가 다음 질문에 답할 수 있게 구성했습니다.

- clawhip은 정확히 무엇을 해결하나?
- 설치 후 어떤 흐름으로 동작하나?
- daemon, source, dispatcher, router, renderer, sink는 어떻게 연결되나?
- tmux/GitHub/Git/OMX 연동은 어디서 이해해야 하나?
- 실습은 어떤 순서로 진행해야 하나?

---

## 이 저장소의 목표

- `clawhip`의 기능·구조·운영 패턴을 **한국어 학습 자료**로 재구성
- `oh-my-codex-guide`처럼 **입문 → 구조 이해 → 운영 실습**의 흐름 제공
- `ai-literacy-llm-engineer-learning`처럼
  **로드맵·모듈·실습·리소스** 구조 적용
- 원본 런타임 코드를 복제하지 않고,
  학습 관점의 설명·체크리스트·실습 계획 제공

---

## 추천 학습 순서

1. `00_Home/00_학습로드맵.md` — 전체 지도 파악
2. `01-learning-paths.md` — 자신의 수준에 맞는 경로 선택
3. `01_Foundations/` — clawhip의 문제 정의, 설치, 첫 실행 이해
4. `02_Runtime-Internals/` — 내부 아키텍처와 핵심 모듈 이해
5. `03_Operations/` — 실제 운영 시나리오와 연동 패턴 학습
6. `04_Labs/` — 직접 설치/라우팅/알림 실습
7. `02-glossary.md`, `05_Resources/` — 참조 자료로 반복 활용

---

## 권장 폴더 구조

```text
clawhip-guide/
├── README.md
├── 01-learning-paths.md
├── 02-glossary.md
├── 03-repo-blueprint.md
├── 00_Home/
│   └── 00_학습로드맵.md
├── 01_Foundations/
│   ├── 01-clawhip-소개.md
│   └── 02-설치와-첫-실행.md
├── 02_Runtime-Internals/
│   ├── 01-아키텍처.md
│   ├── 02-이벤트와-라우팅.md
│   └── 03-CLI와-설정.md
├── 03_Operations/
│   ├── 01-GitHub-Git-tmux-연동.md
│   ├── 02-Memory-Plugins-Skills.md
│   └── 03-라이브-검증.md
├── 04_Labs/
│   ├── 01-기본-설치-실습.md
│   ├── 02-라우트-설계-실습.md
│   └── 03-tmux-알림-실습.md
├── 05_Resources/
│   ├── 01-런타임-맵.md
│   └── 02-학습-체크리스트.md
├── sections/
│   ├── 01-overview.md
│   ├── 02-install.md
│   ├── 03-architecture.md
│   ├── 04-routing.md
│   ├── 05-operations.md
│   └── 06-labs.md
├── assets/
│   └── diagrams/
└── tools/
    └── verify_guide.py
```

---

## 섹션 리스트

| 구분 | 문서 | 핵심 질문 |
| --- | --- | --- |
| Frontdoor | `README.md` | 이 저장소를 어떻게 읽고 사용할까? |
| 학습 경로 | `01-learning-paths.md` | 입문/운영/확장 트랙은 어떻게 다른가? |
| 용어집 | `02-glossary.md` | daemon, source, sink, route는 무엇인가? |
| 설계 청사진 | `03-repo-blueprint.md` | 어떤 구조와 콘텐츠 원칙으로 확장할까? |
| 기초 | `01_Foundations/*` | 무엇을 해결하고 어떻게 설치할까? |
| 내부 구조 | `02_Runtime-Internals/*` | 이벤트 파이프라인은 어떻게 이어지나? |
| 운영 | `03_Operations/*` | 실제 알림 운영과 검증은 어떻게 하나? |
| 실습 | `04_Labs/*` | 직접 실행하며 무엇을 확인해야 하나? |
| 참고 자료 | `05_Resources/*` | 원본 소스와 학습 체크는 어디서 보나? |

---

## 학습 흐름

### Phase 1. 개념 잡기

- `01-clawhip-소개`에서 제품의 역할과 주변 도구를 파악
- `02-glossary`로 핵심 용어를 먼저 익힘

### Phase 2. 설치와 첫 성공 경험

- `02-설치와-첫-실행` + `04_Labs/01-기본-설치-실습`
- 목표: daemon 상태 확인, `send`, `status`, `install` 흐름 이해

### Phase 3. 내부 아키텍처 이해

- `01-아키텍처` → `02-이벤트와-라우팅` → `03-CLI와-설정`
- 목표: source → queue → dispatcher → router → renderer → sink 연결 설명 가능

### Phase 4. 운영 패턴 익히기

- Git/GitHub/tmux 연동, memory offload, plugin 구조 학습
- 목표: 실제 팀/봇 운영 시나리오에 clawhip 배치 가능

### Phase 5. 검증과 확장

- `03-라이브-검증` + `04_Labs/02~03`
- 목표: route 설계, tmux keyword 알림, live verification runbook 활용

---

## 콘텐츠 제작 계획

### 1차 작성 범위

- 설치/아키텍처/이벤트/운영/실습의 최소 학습 루프 문서화
- 원본 파일 위치와 읽기 순서를 연결하는 가이드 제공
- 한국어 설명 + 원문 파일 포인터 병행

### 2차 확장 범위

- Mermaid/diagram 추가
- 실습용 sample config 및 예제 payload 추가
- `clawhip` 주요 명령별 walkthrough 보강

### 3차 확장 범위

- 릴리스별 변경점 비교 가이드
- OMC/OMX 연동 실전 레시피
- Discord/Slack 운영 베스트 프랙티스

---

## 원본 런타임에서 우선 참고할 파일

- `clawhip/README.md`
- `clawhip/ARCHITECTURE.md`
- `clawhip/docs/native-event-contract.md`
- `clawhip/docs/live-verification.md`
- `clawhip/docs/memory-offload-guide.md`
- `clawhip/src/cli.rs`
- `clawhip/src/main.rs`
- `clawhip/src/router.rs`
- `clawhip/src/source/*`
- `clawhip/skills/omx/`, `clawhip/plugins/`, `clawhip/integrations/`

---

## 요약

이 저장소는 `clawhip`를 단순 사용법이 아니라
**운영 런타임으로 이해하고 실습하는 한국어 학습 레포**로 설계합니다.
핵심은 “설치 → 이벤트 흐름 → 운영 연동 → 검증”의 학습 루프를
선명하게 만드는 것입니다.
