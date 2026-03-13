# clawhip 학습 경로

이 문서는 학습자의 목적에 따라 `clawhip`를 어떤 순서로 읽을지 제안합니다.

## 경로 A. 입문자

목표: clawhip의 정체성과 기본 설치/실행 흐름 이해

1. `README.md`
2. `00_Home/00_학습로드맵.md`
3. `01_Foundations/01-clawhip-소개.md`
4. `01_Foundations/02-설치와-첫-실행.md`
5. `04_Labs/01-기본-설치-실습.md`

성공 기준:

- daemon-first 구조를 한 문장으로 설명할 수 있다.
- `clawhip status`, `clawhip send`, `clawhip install`의 역할을 구분할 수 있다.

## 경로 B. 런타임 해부 트랙

목표: event pipeline과 모듈 책임을 코드 기준으로 이해

1. `02_Runtime-Internals/01-아키텍처.md`
2. `02_Runtime-Internals/02-이벤트와-라우팅.md`
3. `02_Runtime-Internals/03-CLI와-설정.md`
4. `05_Resources/01-런타임-맵.md`

성공 기준:

- source / dispatcher / router / renderer / sink를 연결해 설명할 수 있다.
- `src/main.rs`, `src/cli.rs`, `src/router.rs`, `src/source/*`를 읽는 순서를 안다.

## 경로 C. 운영자 트랙

목표: 실제 Discord 운영, tmux 감시, GitHub/OMX 연동을 이해

1. `03_Operations/01-GitHub-Git-tmux-연동.md`
2. `03_Operations/02-Memory-Plugins-Skills.md`
3. `03_Operations/03-라이브-검증.md`
4. `04_Labs/02-라우트-설계-실습.md`
5. `04_Labs/03-tmux-알림-실습.md`

성공 기준:

- 어떤 이벤트를 어떤 채널로 라우팅할지 설계할 수 있다.
- tmux keyword/stale 감시와 live verification runbook을 활용할 수 있다.

## 경로 D. 기여/확장 트랙

목표: 새로운 섹션, 다이어그램, 운영 예제를 확장

1. `03-repo-blueprint.md`
2. `sections/` 인덱스 문서들
3. `05_Resources/02-학습-체크리스트.md`

추천 확장 작업:

- 명령별 walkthrough 추가
- Mermaid 다이어그램 제작
- release version diff 노트 작성
- sample config / payload 예제 정리
