from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "01-learning-paths.md",
    "02-glossary.md",
    "03-repo-blueprint.md",
    "00_Home/00_학습로드맵.md",
    "01_Foundations/01-clawhip-소개.md",
    "01_Foundations/02-설치와-첫-실행.md",
    "02_Runtime-Internals/01-아키텍처.md",
    "02_Runtime-Internals/02-이벤트와-라우팅.md",
    "02_Runtime-Internals/03-CLI와-설정.md",
    "03_Operations/01-GitHub-Git-tmux-연동.md",
    "03_Operations/02-Memory-Plugins-Skills.md",
    "03_Operations/03-라이브-검증.md",
    "04_Labs/01-기본-설치-실습.md",
    "04_Labs/02-라우트-설계-실습.md",
    "04_Labs/03-tmux-알림-실습.md",
    "05_Resources/01-런타임-맵.md",
    "05_Resources/02-학습-체크리스트.md",
    "sections/01-overview.md",
    "sections/02-install.md",
    "sections/03-architecture.md",
    "sections/04-routing.md",
    "sections/05-operations.md",
    "sections/06-labs.md",
]

required_phrases = {
    "README.md": ["권장 폴더 구조", "섹션 리스트", "학습 흐름", "콘텐츠 제작 계획"],
    "01-learning-paths.md": ["경로 A. 입문자", "경로 B. 런타임 해부 트랙", "경로 C. 운영자 트랙"],
    "02-glossary.md": ["daemon-first", "typed event", "memory offload"],
    "00_Home/00_학습로드맵.md": ["Phase 1.", "Phase 5."],
}

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    print("Missing files:")
    for path in missing:
        print(f"- {path}")
    sys.exit(1)

for rel, phrases in required_phrases.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            print(f"Missing phrase '{phrase}' in {rel}")
            sys.exit(1)

print("Guide structure/content verification: PASS")
