# CLI와 설정

## 먼저 볼 파일

- `clawhip/src/cli.rs`
- `clawhip/src/config.rs`
- `clawhip/README.md`의 config 예시

## 명령 분류

- daemon lifecycle: `start`, `status`
- ingress helpers: `send`, `emit`, `git`, `github`, `agent`, `tmux`
- operator surface: `install`, `update`, `uninstall`, `config`
- runtime extensions: `plugin`, `memory`

## 학습 목표

- 어떤 명령이 daemon client를 호출하는지 설명
- `[providers.discord]`와 legacy `[discord]`의 관계 이해
- route rule에 `sink`, `channel`, `mention`, `format`이 어떻게 연결되는지 이해
