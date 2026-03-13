# Memory · Plugins · Skills

## 다룰 범위

- filesystem-offloaded memory pattern
- codex / claude-code plugin bridge
- OMX/OMC skill 연동 포인트

## 원본 소스 포인터

- `clawhip/docs/memory-offload-guide.md`
- `clawhip/skills/memory-offload/SKILL.md`
- `clawhip/plugins/*`
- `clawhip/skills/omx/`
- `clawhip/skills/omc/`

## 학습 포인트

- `MEMORY.md`와 `memory/` shard의 역할 분리
- plugin은 도구별 bridge, integration은 환경 연결 스크립트라는 점
- clawhip이 알림 정책의 단일 소유자가 되도록 하는 설계 철학
