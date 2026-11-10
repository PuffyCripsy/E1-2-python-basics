# E1-2 컴퓨터에게 명령 내리는 말(파이썬) - 나만의 퀴즈 게임

> **코디세이(Codyssey) E1-2 미션**: 파이썬 기초 문법, 객체 지향 프로그래밍(OOP), 파일 기반 데이터 영속성(`state.json`), Git 협업 워크플로우를 직접 구현하고 검증하는 콘솔 애플리케이션 프로젝트입니다.

---

## 1. 프로젝트 개요

- **프로젝트 명**: 나만의 파이썬 콘솔 퀴즈 게임 (`E1-2-python-basics`)
- **개발 언어**: Python 3.10+ (외부 패키지 없이 표준 라이브러리만 사용)
- **핵심 목표**:
  1. **객체 지향 설계**: `Quiz`, `QuizGame` 클래스 분리를 통한 역할과 책임 분담
  2. **견고한 예외 처리**: 공백, 잘못된 입력, `Ctrl+C`(`KeyboardInterrupt`), 손상된 데이터 파일 안전 복구
  3. **데이터 영속성**: 프로그램 종료 후에도 유지되는 `state.json` 파일 저장 및 불러오기
  4. **Git 워크플로우 실습**: 최소 10개 커밋, 브랜치 생성 및 병합(`merge`), `clone` & `pull` 검증
  5. **보너스 5대 기능 완비**: 문제 랜덤 출제, 풀이 문항 수 선택, 힌트 및 점수 차감, 퀴즈 삭제, 플레이 히스토리 기록

---

## 2. 퀴즈 주제 및 선정 이유

- **선정 주제**: (예: **중학교 1학년 영어 핵심 표현 및 문법 퀴즈** 또는 **파이썬 프로그래밍 기초 상식 퀴즈**)
- **선정 이유**:
  - 학습자/사용자가 친숙하고 명확한 기준(정답/오답)을 가진 콘텐츠로 퀴즈를 구성하여 프로그램 로직의 정확성을 직관적으로 검증할 수 있습니다.
  - 문제, 4지선다 선택지, 정답 번호(1~4), 힌트 데이터가 구조화되어 있어 OOP 모델링과 JSON 직렬화 실습에 최적입니다.

---

## 3. 종합 수행 체크리스트

### [필수 1] 개발 환경 및 코드 구조 (OOP)
- [x] Python 3.10 이상 사용 및 외부 라이브러리 배제 (표준 모듈 `json`, `random`, `sys`, `pathlib` 등만 활용)
- [x] `Quiz` 클래스 정의 (속성: `question`, `choices`, `answer`, `hint`)
- [x] `QuizGame` 클래스 정의 (속성: `quizzes`, `best_score`, `history` / 메서드: 메뉴, 실행, 저장, 로드 등)
- [x] 기능별 메서드 분리 및 단일 책임 원칙(SRP) 준수

### [필수 2] 핵심 기능 및 데이터 영속성
- [x] 메뉴 인터페이스: 1. 퀴즈 풀기, 2. 퀴즈 추가, 3. 퀴즈 목록, 4. 최고 점수 확인, 5. 보너스 기능 등, 0. 종료
- [x] 기본 퀴즈 데이터 5문항 이상 내장
- [x] 퀴즈 풀기 기능: 문제 순차/랜덤 출제, 정답 판정, 피드백, 최종 점수 산출 및 최고 점수 갱신
- [x] 퀴즈 추가 기능: 문제, 4개 선택지, 정답 번호(1~4) 입력받아 신규 등록
- [x] 퀴즈 목록 조회: 등록된 전체 문제와 선택지 확인 (0건일 때 안내 메시지)
- [x] 점수 확인: 역대 최고 점수 표시
- [x] `state.json` 영속 저장: UTF-8 인코딩으로 저장/로드, 파일 부재 시 기본값 생성, 파일 손상 시 `try-except` 자동 복구

### [필수 3] 입력 검증 및 견고한 예외 처리
- [x] 입력 앞뒤 공백 자동 제거 (`strip()`)
- [x] 숫자가 아닌 문자열 입력 시 안내 후 재입력 유도 (`ValueError`)
- [x] 허용 범위를 벗어난 번호 입력 시 안내 후 재입력 유도
- [x] 빈 엔터 입력 시 안내 후 재입력 유도
- [x] `Ctrl+C`(`KeyboardInterrupt`) 또는 `EOFError` 발생 시 비정상 종료 방지 및 안전 저장 후 종료

### [필수 4] Git 워크플로우 실습
- [x] GitHub 원격 저장소 생성 (`E1-2-python-basics`) 및 로컬 연동
- [x] 표준 `.gitignore` 및 `README.md` 작성 후 최초 커밋
- [x] 기능 단위의 의미 있는 커밋 10개 이상 작성 (`Feat:`, `Fix:`, `Docs:`, `Refactor:`)
- [x] 별도 작업 브랜치(`feature/quiz-play`) 생성 및 `main` 브랜치 병합(`checkout`/`switch`, `merge`) 실습
- [x] 저장소 복제 실습: 별도 디렉터리에 `clone` → 내용 수정 및 커밋/푸시 → 원래 작업실에서 `pull` 동기화 검증

### [보너스 과제] 5대 추가 기능
- [x] **보너스 1. 랜덤 출제**: `random` 모듈을 활용하여 퀴즈 출제 순서를 무작위로 셔플
- [x] **보너스 2. 문제 수 선택**: 전체 문제 중 풀고 싶은 문제 수(예: 3문제, 5문제 등) 지정 기능
- [x] **보너스 3. 힌트 기능**: 문제 풀이 중 'H' 입력 시 힌트 제공 및 점수 감점(-10점) 로직
- [x] **보너스 4. 퀴즈 삭제 기능**: 퀴즈 목록에서 원하는 번호를 선택해 삭제하고 `state.json`에 즉시 반영
- [x] **보너스 5. 점수 히스토리 기록**: 최고 점수 외에 플레이 일시, 푼 문제 수, 득점률을 누적 기록 및 조회

---

## 4. 파일 및 디렉터리 구조

```text
E1-2-python-basics/
├── MISSION.md              # 코디세이 E1-2 미션 요구사항 전문
├── README.md               # 프로젝트 안내 및 최종 수행 보고서
├── .gitignore              # Python 가상환경 및 캐시 파일 제외 설정
├── main.py                 # 퀴즈 게임 메인 실행 파일 (Quiz, QuizGame 클래스 및 CLI)
├── state.json              # 퀴즈 목록, 최고 점수, 플레이 히스토리 영속 저장소
└── docs/
    └── screenshots/        # 과제 증빙 스크린샷 모음
        ├── 01_menu.png
        ├── 02_quiz_play.png
        ├── 03_add_quiz.png
        ├── 04_exception_test.png
        └── 05_git_log.png
```

---

## 5. 데이터 파일 스키마 (`state.json`)

프로젝트 루트의 `state.json` 파일은 UTF-8 인코딩으로 저장되며, 다음과 같은 JSON 구조를 가집니다:

```json
{
  "best_score": 80,
  "quizzes": [
    {
      "id": 1,
      "question": "파이썬에서 불변(immutable) 시퀀스 자료형은?",
      "choices": ["list", "tuple", "dict", "set"],
      "answer": 2,
      "hint": "괄호로 소괄호 ()를 사용합니다."
    },
    {
      "id": 2,
      "question": "클래스 생성자 메서드의 올바른 이름은?",
      "choices": ["__init__", "__new__", "__construct__", "init"],
      "answer": 1,
      "hint": "앞뒤로 밑줄이 2개씩 붙어 있습니다."
    }
  ],
  "history": [
    {
      "played_at": "2026-11-10 14:30:00",
      "total_questions": 5,
      "correct_count": 4,
      "score": 80
    }
  ]
}
```

---

## 6. 실행 방법

### 1) 실행 환경
- Python 3.10 이상 설치 필요
- 터미널(Command Prompt, PowerShell, Bash, WSL)에서 실행

### 2) 실행 명령어
```bash
# 저장소 복제 (최초 1회)
git clone https://github.com/PuffyCripsy/E1-2-python-basics.git
cd E1-2-python-basics

# 프로그램 실행
python main.py
```

---

## 7. 주요 기능 시연 및 메뉴 가이드

| 메뉴 번호 | 기능 | 설명 및 동작 |
| :---: | :--- | :--- |
| **1** | **퀴즈 풀기** | 문제 수 선택 및 랜덤 출제 여부 선택 후 퀴즈 진행, 힌트 요청 가능, 결과 및 최고 점수 갱신 |
| **2** | **퀴즈 추가** | 새 문제, 4지선다 선택지, 정답 번호(1~4), 힌트를 입력받아 `state.json`에 영속 저장 |
| **3** | **퀴즈 목록** | 현재 등록된 전체 퀴즈와 선택지, 정답 번호를 일목요연하게 출력 |
| **4** | **퀴즈 삭제 (보너스)** | 등록된 퀴즈 목록 중 특정 번호를 선택하여 삭제 및 파일 동기화 |
| **5** | **점수 및 히스토리** | 역대 최고 점수 및 과거 플레이 기록(일시, 점수, 정답률) 조회 |
| **0** | **종료** | 데이터 상태를 안전하게 저장하고 프로그램 정상 종료 (`Ctrl+C` 입력 시에도 안전 종료) |

---

## 8. Git 워크플로우 실습 기록

### 1) 커밋 로그 가이드 (10개 이상 기능별 커밋 예시)
1. `Docs: 저장소 초기화 및 미션 문서, README.md, .gitignore 등록`
2. `Feat: Quiz 클래스 정의 및 기본 퀴즈 5종 구성`
3. `Feat: 공통 입력 예외 처리 및 safe_input 유틸리티 구현`
4. `Feat: QuizGame 클래스 구조화 및 메인 메뉴 인터페이스 구현`
5. `Feat: 브랜치 feature/quiz-play 생성 및 퀴즈 출제·채점 로직 구현`
6. `Feat: feature/quiz-play 브랜치를 main에 머지`
7. `Feat: 퀴즈 추가 기능 및 state.json 파일 입출력 영속성 구현`
8. `Feat: 퀴즈 목록 조회 및 최고 점수 갱신 기능 구현`
9. `Feat: [보너스] 랜덤 출제, 문항 수 선택, 힌트 기능 구현`
10. `Feat: [보너스] 퀴즈 삭제 및 플레이 히스토리 기록 기능 구현`
11. `Docs: 저장소 복제 실습(clone & pull) 및 실행 스크린샷 첨부`

### 2) 브랜치 생성 및 병합 실습 명령어
```bash
# 1. 추가 기능 브랜치 생성 및 이동
git checkout -b feature/quiz-play

# 2. 기능 구현 후 커밋
git add .
git commit -m "Feat: 퀴즈 풀기 및 채점 로직 구현"

# 3. main 브랜치로 복귀 후 병합
git checkout main
git merge feature/quiz-play

# 4. 원격 저장소 푸시
git push origin main
```

### 3) 저장소 복제 실습 (`clone` & `pull`) 명령어
```bash
# 별도 임시 디렉터리로 복제
cd ..
git clone https://github.com/PuffyCripsy/E1-2-python-basics.git temp-test
cd temp-test

# 수정 후 커밋 및 푸시
echo "# Clone Test" >> README.md
git add README.md
git commit -m "Docs: clone 실습 검증 한 줄 추가"
git push origin main

# 기존 작업 디렉터리로 돌아와 동기화
cd ../E1-2-python-basics
git pull origin main
```
