# GitHub · Git · tmux 연동

## 왜 중요한가

clawhip의 실전 가치는 여러 운영 소스의 이벤트를 한 채널 정책으로 묶는 데 있다.

## 원본 소스 포인터

- `clawhip/src/source/git.rs`
- `clawhip/src/source/github.rs`
- `clawhip/src/source/tmux.rs`
- `clawhip/integrations/git/*`
- `clawhip/integrations/tmux/*`

## 운영 관점 핵심 질문

- Git commit/branch change는 어떤 팀에 유용한가?
- GitHub issue/PR 상태 변경은 어떤 채널로 보내야 하나?
- tmux keyword/stale 감시는 어떤 운영 피드백 루프를 만드나?
