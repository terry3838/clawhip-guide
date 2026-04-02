# Obsidian Vault Map

이 문서는 `clawhip-guide` 의 repo guide 문서를 Obsidian note pack과 어떻게 대응시키는지 정리한다.

## 출력 모드

- mode: `hybrid`
- repo guide: `clawhip-guide/`
- repo-local note pack: `obsidian/clawhip Guide/`
- live vault target: `unset`
- live sync status: `not applied`

## 안전 원칙

- repo-local pack이 정본이다.
- live vault sync는 **의도된 vault target이 명시적으로 확인된 뒤에만** 수행한다.
- default vault나 CLI 반환값은 참고 정보일 뿐, 목적지 확정 근거가 아니다.

## 매핑

| repo guide | note pack |
|---|---|
| `README.md` | `clawhip Guide/clawhip Guide - MOC.md` |
| `01-learning-paths.md` | `clawhip Guide/02 Learning Paths.md` |
| `02-glossary.md` | `clawhip Guide/03 Glossary.md` |
| `03-repo-blueprint.md` | `clawhip Guide/Deep Dives/Repo blueprint.md` |
| `sections/01-overview.md` | `clawhip Guide/01 Overview.md` |
| `sections/02-install.md` | `clawhip Guide/Concepts/Install.md` |
| `sections/03-architecture.md` | `clawhip Guide/Concepts/Architecture.md` |
| `sections/04-routing.md` | `clawhip Guide/Concepts/Routing.md` |
| `sections/05-operations.md` | `clawhip Guide/Concepts/Operations.md` |
| `sections/06-labs.md` | `clawhip Guide/Concepts/Labs.md` |
| `00_Home/00_학습로드맵.md` | `clawhip Guide/Home/학습로드맵.md` |
| `01_Foundations/01-clawhip-소개.md` | `clawhip Guide/Foundations/Clawhip 소개.md` |
| `01_Foundations/02-설치와-첫-실행.md` | `clawhip Guide/Foundations/설치와 첫 실행.md` |
| `02_Runtime-Internals/01-아키텍처.md` | `clawhip Guide/Runtime Internals/아키텍처.md` |
| `02_Runtime-Internals/02-이벤트와-라우팅.md` | `clawhip Guide/Runtime Internals/이벤트와 라우팅.md` |
| `02_Runtime-Internals/03-CLI와-설정.md` | `clawhip Guide/Runtime Internals/CLI와 설정.md` |
| `03_Operations/01-GitHub-Git-tmux-연동.md` | `clawhip Guide/Operations/GitHub Git tmux 연동.md` |
| `03_Operations/02-Memory-Plugins-Skills.md` | `clawhip Guide/Operations/Memory Plugins Skills.md` |
| `03_Operations/03-라이브-검증.md` | `clawhip Guide/Operations/라이브 검증.md` |
| `04_Labs/01-기본-설치-실습.md` | `clawhip Guide/Labs/기본 설치 실습.md` |
| `04_Labs/02-라우트-설계-실습.md` | `clawhip Guide/Labs/라우트 설계 실습.md` |
| `04_Labs/03-tmux-알림-실습.md` | `clawhip Guide/Labs/Tmux 알림 실습.md` |
| `05_Resources/01-런타임-맵.md` | `clawhip Guide/Resources/런타임 맵.md` |
| `05_Resources/02-학습-체크리스트.md` | `clawhip Guide/Resources/학습 체크리스트.md` |
| `examples/README.md` | `clawhip Guide/Examples/README.md` |

## note map 의도

- MOC가 frontdoor 역할을 한다.
- Learning Paths / Glossary가 기본 3축이 된다.
- deep dive는 source-backed reading surface로 붙인다.
- References와 Workflows는 길찾기/증거를 붙잡아 둔다.
