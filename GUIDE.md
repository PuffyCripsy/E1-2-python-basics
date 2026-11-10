# E1-2 단계별 실습 및 커밋 가이드 (VS Code 실전 워크북)

> **안내**: 이 문서는 컴퓨터 VS Code에서 직접 코드를 작성하고 Git 커밋 10개, 브랜치 병합, 파일 영속성, 보너스 5대 과제까지 100% 손쉽게 완성할 수 있도록 돕는 실습 가이드입니다.
> 
> VS Code 한쪽에 이 창을 띄워두고, 각 단계의 코드 블록을 `main.py`에 붙여넣은 뒤 터미널 명령어를 입력하세요.

---

## 🎯 전체 실습 흐름 한눈에 보기

| 단계 | 작업 내용 | Git 브랜치 | 실행 명령어 (커밋) |
| :---: | :--- | :---: | :--- |
| **0단계** | 작업 준비 및 저장소 동기화 | `main` | `git pull origin main` |
| **1단계** | `Quiz` 클래스 생성 | `main` | `git commit -m "Feat: Quiz 클래스 정의"` |
| **2단계** | 기본 문장의 형식 퀴즈 5문항 구성 | `main` | `git commit -m "Feat: 기본 문장의 형식 퀴즈 5종 구성"` |
| **3단계** | 안전한 입력 및 예외 처리 함수 구현 | `main` | `git commit -m "Feat: 공통 입력 예외 처리 safe_input 구현"` |
| **4단계** | `QuizGame` 클래스 및 메인 메뉴 구현 | `main` | `git commit -m "Feat: QuizGame 클래스 및 메뉴 인터페이스 구현"` |
| **5단계** | **[브랜치 생성]** 퀴즈 풀기 및 채점 로직 구현 | `feature/quiz-play` | `git commit -m "Feat: 퀴즈 출제 및 채점 로직 구현"` |
| **6단계** | **[브랜치 병합]** `main` 브랜치로 병합 | `main` | `git merge feature/quiz-play` |
| **7단계** | 퀴즈 추가 및 `state.json` 영속 저장 | `main` | `git commit -m "Feat: 퀴즈 추가 및 state.json 파일 저장 구현"` |
| **8단계** | 퀴즈 목록 조회 및 최고 점수 갱신 | `main` | `git commit -m "Feat: 퀴즈 목록 조회 및 최고 점수 확인 기능 구현"` |
| **9단계** | **[보너스 1~3]** 랜덤 출제, 문항 수 선택, 힌트 감점 | `main` | `git commit -m "Feat: [보너스] 랜덤 출제, 문제수 선택, 힌트 감점 구현"` |
| **10단계** | **[보너스 4~5]** 퀴즈 삭제 및 플레이 히스토리 기록 | `main` | `git commit -m "Feat: [보너스] 퀴즈 삭제 및 플레이 히스토리 누적 기록 구현"` |
| **11단계** | 저장소 복제 실습 (`clone` & `pull`) 및 스크린샷 | `main` | `git log --oneline --graph` 스크린샷 캡처 |

---

## 💻 0단계: VS Code 작업 준비

1. 컴퓨터에서 VS Code를 열고 상단 메뉴 **[터미널] → [새 터미널]** (`Ctrl + ~`)을 실행합니다.
2. 아래 명령어로 저장소 최신 상태를 동기화합니다:
   ```bash
   git pull origin main
   ```
3. 탐색기에서 `main.py` 파일을 새로 생성합니다.

---

## 💻 1단계: `Quiz` 클래스 생성

### ① `main.py` 파일에 아래 코드를 붙여넣습니다:
```python
"""
E1-2: 나만의 퀴즈 게임 - 영어 문장의 형식 (1~5형식)
"""

class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question: str, choices: list[str], answer: int, hint: str = ""):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4번 중 정답 번호
        self.hint = hint

    def display(self, number: int) -> None:
        """문제를 터미널에 깔끔하게 출력합니다."""
        print(f"\n[문제 {number}] {self.question}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"  {idx}. {choice}")

    def check_answer(self, user_answer: int) -> bool:
        """사용자 답과 정답을 비교합니다."""
        return self.answer == user_answer

    def to_dict(self) -> dict:
        """JSON 저장을 위해 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        """딕셔너리에서 Quiz 인스턴스를 복원합니다."""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=int(data["answer"]),
            hint=data.get("hint", ""),
        )
```

### ② 터미널에서 커밋 명령어를 실행합니다:
```bash
git add main.py
git commit -m "Feat: Quiz 클래스 정의"
```

---

## 💻 2단계: 기본 문장의 형식 퀴즈 5종 구성

### ① `main.py` 아래쪽에 기본 퀴즈 5문항 데이터를 추가합니다:
```python
DEFAULT_QUIZZES = [
    Quiz(
        question="다음 문장의 형식은? 'The birds sing sweetly in the trees.'",
        choices=["1형식 (S + V)", "2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)"],
        answer=1,
        hint="'sweetly'(부사)와 'in the trees'(전치사구)는 수식어(M)이므로 주어와 동사만으로 이루어진 1형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'This soup smells delicious.'",
        choices=["1형식 (S + V)", "2형식 (S + V + C)", "3형식 (S + V + O)", "5형식 (S + V + O + O.C)"],
        answer=2,
        hint="감각동사(smell) 뒤에 주어의 상태를 설명하는 형용사 주격 보어(delicious)가 온 2형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'She solved the difficult math problem.'",
        choices=["2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)"],
        answer=2,
        hint="'the difficult math problem'이 동사의 직접적인 대상인 목적어(O) 역할을 하는 3형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'My grandmother sent me a wonderful present.'",
        choices=["2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)"],
        answer=3,
        hint="'~에게'(간접목적어 me)와 '~을'(직접목적어 a wonderful present) 2개의 목적어를 취하는 4형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'The coach encouraged the players to do their best.'",
        choices=["3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)", "2형식 (S + V + C)"],
        answer=3,
        hint="'the players'(목적어)가 행동하도록 'to do their best'(to부정사 목적격 보어)를 이끄는 5형식입니다.",
    ),
]
```

### ② 터미널에서 커밋 명령어를 실행합니다:
```bash
git add main.py
git commit -m "Feat: 기본 문장의 형식 퀴즈 5종 구성"
```

---

## 💻 3단계: 공통 입력 및 예외 처리 함수 구현

### ① `main.py` 맨 위에 `sys`를 임포트하고, `safe_input` 함수를 추가합니다:
```python
import sys

def safe_input(prompt: str) -> str:
    """
    공통 입력 처리:
    - 앞뒤 공백을 자동으로 제거(strip)합니다.
    - Ctrl+C(KeyboardInterrupt)나 EOFError 발생 시 비정상 종료 없이 안전하게 종료합니다.
    """
    try:
        user_val = input(prompt)
        return user_val.strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 안전하게 중단되었습니다. 이용해 주셔서 감사합니다.")
        sys.exit(0)
```

### ② 터미널에서 커밋 명령어를 실행합니다:
```bash
git add main.py
git commit -m "Feat: 공통 입력 예외 처리 safe_input 구현"
```

---

## 💻 4단계: `QuizGame` 클래스 및 메인 메뉴 인터페이스 구현

### ① `main.py` 아래쪽에 `QuizGame` 기본 클래스와 메뉴를 추가합니다:
```python
from pathlib import Path
import json

class QuizGame:
    """게임 전체 관리 클래스"""

    DATA_FILE = Path("state.json")

    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []

    def print_menu(self) -> None:
        """메인 메뉴 출력"""
        print("\n" + "=" * 45)
        print("    🎯 중등 영어 문장의 형식 퀴즈 게임 🎯")
        print("=" * 45)
        print("  1. 퀴즈 풀기")
        print("  2. 새로운 퀴즈 추가")
        print("  3. 등록된 퀴즈 목록 보기")
        print("  4. 퀴즈 삭제 (보너스)")
        print("  5. 최고 점수 및 플레이 기록 확인")
        print("  0. 게임 종료")
        print("=" * 45)
```

### ② 터미널에서 커밋 명령어를 실행합니다:
```bash
git add main.py
git commit -m "Feat: QuizGame 클래스 및 메뉴 인터페이스 구현"
```

---

## 💻 5단계: [브랜치 실습] `feature/quiz-play` 브랜치 생성 및 퀴즈 출제 로직 구현

미션 필수 요건인 **'main 이외의 추가 브랜치 생성 및 작업'**을 수행합니다.

### ① 터미널에서 새 브랜치를 생성하고 이동합니다:
```bash
git checkout -b feature/quiz-play
```

### ② `QuizGame` 클래스 내부에 `play_quiz` 메서드를 추가합니다:
```python
    def play_quiz(self) -> None:
        """퀴즈 풀기 기능 (점수 계산 및 최고 점수 비교)"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
            return

        print(f"\n📝 문장의 형식 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("👉 풀이 중 힌트가 필요하시면 'H'를 입력하세요 (힌트 사용 시 문제당 10점 감점)")

        correct_count = 0
        hints_used = 0

        for idx, quiz in enumerate(self.quizzes, start=1):
            quiz.display(idx)

            while True:
                user_choice = safe_input("정답 입력 (1-4) 또는 힌트(H): ").upper()

                if user_choice == "H":
                    print(f"💡 [힌트] {quiz.hint if quiz.hint else '등록된 힌트가 없습니다.'}")
                    hints_used += 1
                    continue

                if user_choice in ["1", "2", "3", "4"]:
                    user_ans = int(user_choice)
                    if quiz.check_answer(user_ans):
                        print("✅ 정답입니다!")
                        correct_count += 1
                    else:
                        print(f"❌ 오답입니다. (정답: {quiz.answer}번)")
                    break
                else:
                    print("⚠️ 잘못된 입력입니다. 1부터 4 사이의 숫자나 H를 입력해 주세요.")

        # 점수 계산 (100점 만점 환산, 힌트 감점)
        raw_score = int((correct_count / len(self.quizzes)) * 100)
        final_score = max(0, raw_score - (hints_used * 10))

        print("\n" + "=" * 45)
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답! (점수: {final_score}점)")
        if hints_used > 0:
            print(f"   (힌트 사용 {hints_used}회로 {hints_used * 10}점 감점 적용)")

        if final_score > self.best_score:
            print(f"🎉 축하합니다! 새로운 최고 점수({final_score}점)를 달성하셨습니다!")
            self.best_score = final_score
        else:
            print(f"📌 현재 최고 점수는 {self.best_score}점입니다.")
        print("=" * 45)

        self.save_data()
```

### ③ `feature/quiz-play` 브랜치에서 커밋합니다:
```bash
git add main.py
git commit -m "Feat: 퀴즈 출제 및 채점 로직 구현"
```

---

## 💻 6단계: [브랜치 병합] `main` 브랜치로 병합 (`git merge`)

### ① 터미널에서 `main` 브랜치로 돌아가 병합합니다:
```bash
git checkout main
git merge feature/quiz-play
```

---

## 💻 7단계: 퀴즈 추가 및 `state.json` 영속 저장 구현

미션 필수 요건인 **`state.json` 파일 저장 및 try/except 자동 복구**를 구현합니다.

### ① `QuizGame` 클래스에 파일 입출력 및 퀴즈 추가 메서드를 추가하고, `__init__`에서 `load_data()`를 호출하도록 연결합니다:
```python
    def load_data(self) -> None:
        """state.json 파일에서 데이터를 불러오며, 없거나 손상 시 기본값으로 복구합니다."""
        if not self.DATA_FILE.exists():
            print("📂 state.json 파일이 없어 기본 5형식 퀴즈 데이터를 로드합니다.")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.history = []
            self.save_data()
            return

        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = int(data.get("best_score", 0))
                self.history = data.get("history", [])
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except (json.JSONDecodeError, KeyError, Exception) as e:
            print(f"⚠️ state.json 파일이 손상되어 기본 데이터로 안전하게 복구합니다. ({e})")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.history = []
            self.save_data()

    def save_data(self) -> None:
        """현재 퀴즈 목록과 최고 점수를 state.json에 안전하게 저장합니다."""
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes],
            "history": self.history,
        }
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 파일 저장 중 오류가 발생했습니다: {e}")

    def add_quiz(self) -> None:
        """새로운 문장의 형식 퀴즈를 입력받아 등록하고 저장합니다."""
        print("\n📌 [새 퀴즈 등록]")
        question = safe_input("문제를 입력하세요: ")
        while not question:
            print("⚠️ 문제는 빈칸으로 둘 수 없습니다.")
            question = safe_input("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            c = safe_input(f"선택지 {i}: ")
            while not c:
                print(f"⚠️ 선택지 {i}번을 입력해 주세요.")
                c = safe_input(f"선택지 {i}: ")
            choices.append(c)

        while True:
            ans_str = safe_input("정답 번호 (1-4): ")
            if ans_str in ["1", "2", "3", "4"]:
                answer = int(ans_str)
                break
            print("⚠️ 정답은 1에서 4 사이의 숫자만 가능합니다.")

        hint = safe_input("문법 힌트 (엔터 시 생략 가능): ")

        new_quiz = Quiz(question=question, choices=choices, answer=answer, hint=hint)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 새 퀴즈가 성공적으로 등록되고 state.json에 저장되었습니다!")
```

### ② 터미널에서 커밋합니다:
```bash
git add main.py
git commit -m "Feat: 퀴즈 추가 및 state.json 파일 저장 구현"
```

---

## 💻 8단계: 퀴즈 목록 조회 및 최고 점수 확인 구현

### ① `QuizGame` 클래스에 목록 보기와 점수 확인 메서드를 추가합니다:
```python
    def list_quizzes(self) -> None:
        """등록된 퀴즈 전체 목록 확인"""
        if not self.quizzes:
            print("\n📋 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 [등록된 문장의 형식 퀴즈 목록 (총 {len(self.quizzes)}개)]")
        print("-" * 45)
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"[{idx}] {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, start=1):
                star = " ★(정답)" if c_idx == quiz.answer else ""
                print(f"    {c_idx}. {choice}{star}")
            if quiz.hint:
                print(f"    💡 힌트: {quiz.hint}")
            print("-" * 45)

    def show_score(self) -> None:
        """최고 점수 확인"""
        print("\n" + "=" * 45)
        print(f"🏆 역대 최고 점수: {self.best_score}점")
        print("=" * 45)
```

### ② 터미널에서 커밋합니다:
```bash
git add main.py
git commit -m "Feat: 퀴즈 목록 조회 및 최고 점수 확인 기능 구현"
```

---

## 💻 9단계: [보너스 1~3] 랜덤 출제, 문항 수 선택, 힌트 감점 로직 강화

### ① `main.py` 맨 위에 `import random`을 추가하고, `play_quiz` 시작부에 아래 로직을 연결합니다:
```python
        # [보너스 1 & 2: 랜덤 출제 및 문항 수 선택]
        quizzes_to_play = list(self.quizzes)
        is_random = safe_input("문제 순서를 무작위로 섞을까요? (Y/N, 기본 N): ").upper() == "Y"
        if is_random:
            random.shuffle(quizzes_to_play)

        count_input = safe_input(f"풀고 싶은 문제 수를 입력하세요 (1~{len(quizzes_to_play)}, 기본 전체): ")
        if count_input.isdigit() and 1 <= int(count_input) <= len(quizzes_to_play):
            quizzes_to_play = quizzes_to_play[:int(count_input)]
```

### ② 터미널에서 커밋합니다:
```bash
git add main.py
git commit -m "Feat: [보너스] 랜덤 출제, 문제수 선택, 힌트 감점 구현"
```

---

## 💻 10단계: [보너스 4~5] 퀴즈 삭제, 플레이 히스토리 기록 및 실행 루프 완성

### ① `delete_quiz` 메서드와 메인 루프 `run()`을 추가하고 스크립트 실행부를 완성합니다:
```python
from datetime import datetime

    def delete_quiz(self) -> None:
        """[보너스 4] 퀴즈 삭제 기능"""
        if not self.quizzes:
            print("\n⚠️ 삭제할 퀴즈가 없습니다.")
            return

        self.list_quizzes()
        idx_str = safe_input("삭제할 퀴즈 번호를 입력하세요 (취소: 0): ")
        if not idx_str.isdigit():
            print("⚠️ 올바른 숫자를 입력하세요.")
            return

        del_idx = int(idx_str)
        if del_idx == 0:
            print("삭제가 취소되었습니다.")
            return

        if 1 <= del_idx <= len(self.quizzes):
            removed = self.quizzes.pop(del_idx - 1)
            self.save_data()
            print(f"🗑️ [{del_idx}]번 퀴즈가 삭제되었습니다.")
        else:
            print("⚠️ 유효한 번호가 아닙니다.")

    def run(self) -> None:
        """메인 실행 루프"""
        while True:
            self.print_menu()
            choice = safe_input("메뉴 선택: ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.delete_quiz()
            elif choice == "5":
                self.show_score()
            elif choice == "0":
                print("\n👋 퀴즈 게임을 종료합니다. 수고하셨습니다!")
                self.save_data()
                break
            else:
                print("⚠️ 잘못된 입력입니다. 0부터 5 사이의 번호를 입력하세요.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()
```

### ② 터미널에서 커밋하고 GitHub에 최종 푸시합니다:
```bash
git add main.py
git commit -m "Feat: [보너스] 퀴즈 삭제 및 플레이 히스토리 누적 기록 구현"
git push origin main
```

---

## 💻 11단계: 저장소 복제 실습 (`clone` & `pull`) 및 과제 제출 스크린샷 캡처

### ① 미션 필수 요건: 터미널에서 복제(`clone`) 및 가져오기(`pull`) 실습
```bash
# 1. 상위 폴더로 잠시 이동
cd ..

# 2. 다른 이름으로 저장소 복제 (clone 실습)
git clone https://github.com/PuffyCripsy/E1-2-python-basics.git clone-test
cd clone-test

# 3. 테스트로 README 한 줄 추가 후 커밋 및 푸시
echo "<!-- Verified by Yunhee -->" >> README.md
git add README.md
git commit -m "Docs: clone 실습 및 정상 동작 검증"
git push origin main

# 4. 원래 작업 디렉터리로 복귀 후 변경사항 가져오기 (pull 실습)
cd ../E1-2-python-basics
git pull origin main
```

### ② 과제 제출용 스크린샷 4장 캡처:
1. `docs/screenshots/01_menu.png`: VS Code에서 `python main.py` 실행 시 메뉴 화면
2. `docs/screenshots/02_quiz_play.png`: 퀴즈 풀기 진행 및 점수 결과 화면
3. `docs/screenshots/03_add_quiz.png`: 새 퀴즈 추가 화면
4. `docs/screenshots/04_git_log.png`: 터미널에서 `git log --oneline --graph` 실행한 10개 이상 커밋 그래프 화면

---

## 📜 [부록] `main.py` 전체 완성본 소스코드 (참고용 전문)

전체 구조를 한눈에 보거나 바로 테스트해 보실 때 사용할 수 있는 완성본 전체 코드입니다:

```python
"""
E1-2: 컴퓨터에게 명령 내리는 말(파이썬) - 나만의 퀴즈 게임
주제: 중학교 영어 문장의 형식 (1~5형식)
기능: OOP(Quiz, QuizGame), state.json 데이터 영속성, 예외 처리, 보너스 5대 과제 포함
"""

import sys
import json
import random
from pathlib import Path
from datetime import datetime


def safe_input(prompt: str) -> str:
    """공통 입력 예외 처리: 공백 제거 및 Ctrl+C/EOF 안전 종료"""
    try:
        user_val = input(prompt)
        return user_val.strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 안전하게 종료되었습니다. 이용해 주셔서 감사합니다.")
        sys.exit(0)


class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question: str, choices: list[str], answer: int, hint: str = ""):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4
        self.hint = hint

    def display(self, number: int) -> None:
        print(f"\n[문제 {number}] {self.question}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"  {idx}. {choice}")

    def check_answer(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=int(data["answer"]),
            hint=data.get("hint", ""),
        )


DEFAULT_QUIZZES = [
    Quiz(
        question="다음 문장의 형식은? 'The birds sing sweetly in the trees.'",
        choices=["1형식 (S + V)", "2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)"],
        answer=1,
        hint="'sweetly'(부사)와 'in the trees'(전치사구)는 수식어(M)이므로 주어와 동사만으로 이루어진 1형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'This soup smells delicious.'",
        choices=["1형식 (S + V)", "2형식 (S + V + C)", "3형식 (S + V + O)", "5형식 (S + V + O + O.C)"],
        answer=2,
        hint="감각동사(smell) 뒤에 주어의 상태를 설명하는 형용사 주격 보어(delicious)가 온 2형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'She solved the difficult math problem.'",
        choices=["2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)"],
        answer=2,
        hint="'the difficult math problem'이 동사의 직접적인 대상인 목적어(O) 역할을 하는 3형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'My grandmother sent me a wonderful present.'",
        choices=["2형식 (S + V + C)", "3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)"],
        answer=3,
        hint="'~에게'(간접목적어 me)와 '~을'(직접목적어 a wonderful present) 2개의 목적어를 취하는 4형식입니다.",
    ),
    Quiz(
        question="다음 문장의 형식은? 'The coach encouraged the players to do their best.'",
        choices=["3형식 (S + V + O)", "4형식 (S + V + I.O + D.O)", "5형식 (S + V + O + O.C)", "2형식 (S + V + C)"],
        answer=3,
        hint="'the players'(목적어)가 행동하도록 'to do their best'(to부정사 목적격 보어)를 이끄는 5형식입니다.",
    ),
]


class QuizGame:
    """게임 전체 관리 클래스"""

    DATA_FILE = Path("state.json")

    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        self.load_data()

    def load_data(self) -> None:
        """state.json 불러오기 및 손상 시 자동 복구"""
        if not self.DATA_FILE.exists():
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.history = []
            self.save_data()
            return

        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = int(data.get("best_score", 0))
                self.history = data.get("history", [])
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
        except Exception:
            print("⚠️ state.json 복구 중: 기본 데이터로 안전하게 초기화합니다.")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.history = []
            self.save_data()

    def save_data(self) -> None:
        """state.json 저장"""
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes],
            "history": self.history,
        }
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 저장 오류: {e}")

    def print_menu(self) -> None:
        print("\n" + "=" * 45)
        print("    🎯 중등 영어 문장의 형식 퀴즈 게임 🎯")
        print("=" * 45)
        print("  1. 퀴즈 풀기")
        print("  2. 새로운 퀴즈 추가")
        print("  3. 등록된 퀴즈 목록 보기")
        print("  4. 퀴즈 삭제 (보너스)")
        print("  5. 최고 점수 및 플레이 기록 확인")
        print("  0. 게임 종료")
        print("=" * 45)

    def play_quiz(self) -> None:
        """퀴즈 풀기 (랜덤 출제, 문항 수 선택, 힌트 감점 포함)"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
            return

        quizzes_to_play = list(self.quizzes)
        is_random = safe_input("문제 순서를 무작위로 섞을까요? (Y/N, 기본 N): ").upper() == "Y"
        if is_random:
            random.shuffle(quizzes_to_play)

        count_input = safe_input(f"풀고 싶은 문제 수를 입력하세요 (1~{len(quizzes_to_play)}, 기본 전체): ")
        if count_input.isdigit() and 1 <= int(count_input) <= len(quizzes_to_play):
            quizzes_to_play = quizzes_to_play[:int(count_input)]

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes_to_play)}문제)")
        print("👉 풀이 중 힌트가 필요하시면 'H'를 입력하세요 (힌트당 10점 감점)")

        correct_count = 0
        hints_used = 0

        for idx, quiz in enumerate(quizzes_to_play, start=1):
            quiz.display(idx)

            while True:
                user_choice = safe_input("정답 입력 (1-4) 또는 힌트(H): ").upper()

                if user_choice == "H":
                    print(f"💡 [힌트] {quiz.hint if quiz.hint else '등록된 힌트가 없습니다.'}")
                    hints_used += 1
                    continue

                if user_choice in ["1", "2", "3", "4"]:
                    user_ans = int(user_choice)
                    if quiz.check_answer(user_ans):
                        print("✅ 정답입니다!")
                        correct_count += 1
                    else:
                        print(f"❌ 오답입니다. (정답: {quiz.answer}번)")
                    break
                else:
                    print("⚠️ 잘못된 입력입니다. 1부터 4 사이의 숫자나 H를 입력하세요.")

        raw_score = int((correct_count / len(quizzes_to_play)) * 100)
        final_score = max(0, raw_score - (hints_used * 10))

        print("\n" + "=" * 45)
        print(f"🏆 결과: {len(quizzes_to_play)}문제 중 {correct_count}문제 정답! (점수: {final_score}점)")
        if hints_used > 0:
            print(f"   (힌트 사용 {hints_used}회로 {hints_used * 10}점 감점 적용)")

        if final_score > self.best_score:
            print(f"🎉 축하합니다! 새로운 최고 점수({final_score}점) 달성!")
            self.best_score = final_score
        else:
            print(f"📌 현재 최고 점수는 {self.best_score}점입니다.")
        print("=" * 45)

        self.history.append({
            "played_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": len(quizzes_to_play),
            "correct_count": correct_count,
            "score": final_score,
        })
        self.save_data()

    def add_quiz(self) -> None:
        """새로운 퀴즈 등록"""
        print("\n📌 [새 문장의 형식 퀴즈 등록]")
        question = safe_input("문제를 입력하세요: ")
        while not question:
            print("⚠️ 문제는 필수 입력입니다.")
            question = safe_input("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            c = safe_input(f"선택지 {i}: ")
            while not c:
                print(f"⚠️ 선택지 {i}번을 입력해 주세요.")
                c = safe_input(f"선택지 {i}: ")
            choices.append(c)

        while True:
            ans_str = safe_input("정답 번호 (1-4): ")
            if ans_str in ["1", "2", "3", "4"]:
                answer = int(ans_str)
                break
            print("⚠️ 정답은 1에서 4 사이 숫자만 가능합니다.")

        hint = safe_input("문법 힌트 (엔터 시 생략 가능): ")

        new_quiz = Quiz(question=question, choices=choices, answer=answer, hint=hint)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 새 퀴즈가 등록되고 state.json에 저장되었습니다!")

    def list_quizzes(self) -> None:
        """퀴즈 전체 목록 확인"""
        if not self.quizzes:
            print("\n📋 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 [등록된 문장의 형식 퀴즈 목록 (총 {len(self.quizzes)}개)]")
        print("-" * 45)
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"[{idx}] {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, start=1):
                star = " ★(정답)" if c_idx == quiz.answer else ""
                print(f"    {c_idx}. {choice}{star}")
            if quiz.hint:
                print(f"    💡 힌트: {quiz.hint}")
            print("-" * 45)

    def delete_quiz(self) -> None:
        """[보너스 4] 퀴즈 삭제"""
        if not self.quizzes:
            print("\n⚠️ 삭제할 퀴즈가 없습니다.")
            return

        self.list_quizzes()
        idx_str = safe_input("삭제할 퀴즈 번호를 입력하세요 (취소: 0): ")
        if not idx_str.isdigit():
            print("⚠️ 올바른 숫자를 입력하세요.")
            return

        del_idx = int(idx_str)
        if del_idx == 0:
            print("삭제가 취소되었습니다.")
            return

        if 1 <= del_idx <= len(self.quizzes):
            removed = self.quizzes.pop(del_idx - 1)
            self.save_data()
            print(f"🗑️ [{del_idx}]번 퀴즈가 삭제되었습니다.")
        else:
            print("⚠️ 유효한 번호가 아닙니다.")

    def show_score(self) -> None:
        """[보너스 5] 점수 및 히스토리 조회"""
        print("\n" + "=" * 45)
        print(f"🏆 역대 최고 점수: {self.best_score}점")
        if self.history:
            print("\n📜 [최근 플레이 기록]")
            for h in self.history[-5:]:
                print(f"  - {h['played_at']}: {h['total_questions']}문제 중 {h['correct_count']}정답 ({h['score']}점)")
        print("=" * 45)

    def run(self) -> None:
        """메인 실행 루프"""
        while True:
            self.print_menu()
            choice = safe_input("메뉴 선택: ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.delete_quiz()
            elif choice == "5":
                self.show_score()
            elif choice == "0":
                print("\n👋 퀴즈 게임을 종료합니다. 수고하셨습니다!")
                self.save_data()
                break
            else:
                print("⚠️ 잘못된 입력입니다. 0부터 5 사이의 번호를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()
```
