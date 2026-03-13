# clawhip 소개

## 이 문서의 질문

- clawhip은 어떤 문제를 해결하나?
- 왜 daemon-first 구조를 선택했나?
- OMX/OMC/OpenClaw와는 어떤 관계인가?

## 핵심 요약

clawhip은 개발/운영 이벤트를 Discord 같은 채널로 전달하는 **notification runtime**이다. 단순 webhook 전송기가 아니라, 이벤트를 정규화하고 route rule에 따라 여러 delivery로 분배하는 운영 레이어다.

## 원본 소스 포인터

- `clawhip/README.md`
- `clawhip/ARCHITECTURE.md`
- `clawhip/Cargo.toml`

## 학습 포인트

- daemon-first = 지속 감시와 이벤트 라우팅 중심
- typed event = ingress 호환성과 내부 안정성 동시 확보
- multi-delivery = 하나의 이벤트를 여러 채널/포맷으로 전달 가능
