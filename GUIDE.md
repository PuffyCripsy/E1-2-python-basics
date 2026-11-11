# E1-2 단계별 실습 및 커밋 가이드 (VS Code 실전 워크북)

> **안내**: 이 문서는 컴퓨터 VS Code에서 직접 코드를 작성하고 Git 커밋, 브랜치 병합, 파일 영속성(`state.json`), 보너스 과제(랜덤 출제) 및 clone/pull 실습까지 손쉽게 완성할 수 있도록 돕는 실습 가이드입니다.
> 
> VS Code 화면 한쪽에 이 가이드를 띄워두고, 단계별 코드 블록과 터미널 명령어를 확인하며 따라 하실 수 있습니다.

---

## 🎯 전체 실습 흐름 한눈에 보기

| 단계 | 작업 내용 | Git 브랜치 | 주요 구현 내용 |
| :---: | :--- | :---: | :--- |
| **0단계** | 작업 준비 및 저장소 동기화 | `main` | `git pull origin main`으로 최신 상태 가져오기 |
| **1단계** | `Quiz` 클래스 생성 | `main` | 영어 문장, `1~4`번 보기, 정답 번호를 담는 부품 설계 |
| **2단계** | 기본 5형식 문제 및 정답 검증 | `main` | 1형식~5형식 기본 문제 5문항 및 입력 예외 처리 |
| **3단계** | `QuizGame` 클래스 및 메인 메뉴 | `main` | 1~5번 메뉴 반복 인터페이스 및 안전 종료 구현 |
| **4단계** | **[브랜치 실습]** 퀴즈 풀기 구현 | `feature/quiz-play` | 점수 계산, 정답/오답 판정 및 브랜치 병합(`merge`) |
| **5단계** | 새로운 퀴즈 추가 기능 | `main` | 영어 문장 및 보기 빈 값 방지 검증 후 목록 추가 |
| **6단계** | 등록된 퀴즈 목록 조회 | `main` | 전체 등록된 퀴즈 문제와 선택지, 정답 번호 출력 |
| **7단계** | 최고 점수 확인 기능 | `main` | 역대 최고 점수(`best_score`) 단독 조회 |
| **8단계** | `state.json` 영속 저장 및 복구 | `main` | 종료 후에도 유지되는 JSON 저장 및 손상 시 자동 복구 |
| **9단계** | **[보너스]** 퀴즈 랜덤 출제 | `main` | `random.sample`을 통한 문제 순서 무작위 셔플 |
| **10단계** | 저장소 복제 실습 (`clone` & `pull`) | `main` | 미션 13번 별도 폴더 복제 및 동기화 실습 |

---

## 💻 0단계: VS Code 작업 준비

1. 컴퓨터에서 VS Code를 열고 상단 메뉴 **[터미널] → [새 터미널]** (`Ctrl + ~`)을 실행합니다.
2. 아래 명령어로 저장소 최신 상태를 동기화합니다:
   ```bash
   git pull origin main
   ```
3. 탐색기에서 `main.py` 파일이 열려 있는지 확인합니다.

---

## 💻 1단계: `Quiz` 클래스 정의

개별 퀴즈 문제 데이터를 캡슐화하는 기본 객체 지향(OOP) 클래스를 선언합니다.

### ① 코드 작성 (`main.py` 상단)
```python
class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question      # 영어 문장
        self.choices = choices        # 1~4번 선택지 리스트
        self.answer = answer          # 정답 번호 (1~4 정수)
```

### ② 터미널 커밋
```bash
git add main.py
git commit -m "Feat: Quiz 클래스 및 문제 출력 기능 구현"
```

---

## 💻 2단계: 기본 퀴즈 5문항 구성

중학교 3학년 영어 교과 과정에 맞추어 1형식부터 5형식까지의 대표 예문 5문항을 `Quiz` 인스턴스로 생성합니다.

### ① 코드 작성
```python
quizzes = [
    Quiz(
        "The birds sing sweetly in the trees.",
        ["1형식", "2형식", "3형식", "4형식"],
        1
    ),
    Quiz(
        "This soup smells delicious.",
        ["1형식", "2형식", "3형식", "4형식"],
        2
    ),
    Quiz(
        "She solved the difficult math problem.",
        ["2형식", "3형식", "4형식", "5형식"],
        2
    ),
    Quiz(
        "My grandmother sent me a wonderful present.",
        ["1형식", "3형식", "4형식", "5형식"],
        3
    ),
    Quiz(
        "The coach encouraged the players to do their best.",
        ["2형식", "3형식", "4형식", "5형식"],
        4
    )
]
```

---

## 💻 3단계: `QuizGame` 클래스 및 메인 메뉴 인터페이스 구현

1번부터 5번까지의 메뉴 인터페이스와 사용자 입력 반복 루프(`while True`)를 구성합니다.

### ① 코드 작성
```python
class QuizGame:
    """퀴즈 게임 전체 흐름을 제어하는 클래스"""

    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.score = 0
        self.best_score = 0

    def show_menu(self):
        while True:
            print("\n===== 영어 문장 형식 퀴즈 =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 문제 추가")
            print("3. 퀴즈 문제 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")

            choice = input("메뉴를 선택하세요 (1~5): ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_best_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")
```

### ② 터미널 커밋
```bash
git add main.py
git commit -m "Feat: Add main menu and exit functionality"
```

---

## 💻 4단계: [브랜치 실습] 퀴즈 출제 및 채점 로직 구현

과제 필수 요건인 **Git 브랜치 생성 및 병합(`checkout`, `merge`)**을 실습합니다.

### ① 새 브랜치 생성 및 이동
```bash
git checkout -b feature/quiz-play
```

### ② `QuizGame` 내부에 `play_quiz` 메서드 구현
```python
    def play_quiz(self):
        self.score = 0
        # [보너스] random.sample을 활용한 문제 무작위(랜덤) 출제
        shuffled_quizzes = random.sample(self.quizzes, len(self.quizzes))

        for quiz_number, quiz in enumerate(shuffled_quizzes, start=1):
            print(f"\n문제 {quiz_number}. {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            while True:
                user_input = input("정답 번호를 입력하세요 (1~4): ").strip()

                if user_input in ["1", "2", "3", "4"]:
                    user_answer = int(user_input)
                    break

                print("잘못된 입력입니다. 1~4 중에서 선택하세요.")

            if user_answer == quiz.answer:
                print("정답입니다!")
                self.score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(
            f"\n퀴즈 종료! 총 {len(self.quizzes)}문제 중 "
            f"{self.score}문제를 맞혔습니다."
        )

        if self.score > self.best_score:
            self.best_score = self.score
            print("새로운 최고 점수입니다!")
            self.save_state()
```

### ③ 커밋 후 `main` 브랜치로 병합
```bash
git add main.py
git commit -m "Feat: 정답 입력 검증 및 점수 계산 기능 구현"

# main 브랜치로 복귀 후 병합
git checkout main
git merge feature/quiz-play
```

---

## 💻 5단계: 새로운 퀴즈 추가 기능 구현 (`add_quiz`)

빈 문자열 방지 루프와 정답 번호(`1~4`) 유효성 검증을 거쳐 새 퀴즈를 목록에 등록합니다.

### ① 코드 작성
```python
    def add_quiz(self):
        print("\n===== 새로운 퀴즈 추가 =====")

        question = input("영어 문장을 입력하세요: ").strip()

        while not question:
            print("문제를 비워 둘 수 없습니다.")
            question = input("영어 문장을 입력하세요: ").strip()

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 보기를 입력하세요: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("보기를 비워 둘 수 없습니다.")

        while True:
            answer = input("정답 번호를 입력하세요 (1~4): ").strip()

            if answer in ["1", "2", "3", "4"]:
                answer = int(answer)
                break

            print("잘못된 입력입니다. 1~4 중에서 선택하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print("새로운 퀴즈가 추가되었습니다!")
```

### ② 터미널 커밋
```bash
git add main.py
git commit -m "Feat: Add quiz creation functionality and screenshots"
```

---

## 💻 6단계: 퀴즈 문제 목록 및 최고 점수 확인 구현

### ① 코드 작성
```python
    def show_quizzes(self):
        print("\n===== 등록된 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for quiz_number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {quiz_number}. {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            print(f"정답: {quiz.answer}번")

        print(f"\n총 {len(self.quizzes)}개의 문제가 등록되어 있습니다.")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print(f"현재 최고 점수: {self.best_score}점")
```

### ② 터미널 커밋
```bash
git add main.py
git commit -m "Feat: Add quiz list display functionality"
git commit -m "Feat: Add best score tracking and display"
```

---

## 💻 7단계: `state.json` 영속 저장 및 자동 복구 로직 구현

프로그램이 종료되어도 데이터가 보존되도록 `json` 모듈을 활용하여 저장(`save_state`) 및 불러오기(`load_state`)를 완성합니다.

### ① 코드 작성
```python
    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }

        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터가 저장되었습니다.")

        except OSError as error:
            print(f"데이터 저장 중 오류가 발생했습니다: {error}")

    def load_state(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            best_score = data["best_score"]
            saved_quizzes = data["quizzes"]

            if not isinstance(best_score, int) or best_score < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            if not isinstance(saved_quizzes, list):
                raise ValueError("퀴즈 목록 데이터가 올바르지 않습니다.")

            loaded_quizzes = []

            for item in saved_quizzes:
                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(isinstance(c, str) and c.strip() for c in choices)
                    or type(answer) is not int
                    or answer not in [1, 2, 3, 4]
                ):
                    raise ValueError("저장된 퀴즈 데이터가 올바르지 않습니다.")

                loaded_quizzes.append(Quiz(question, choices, answer))

            self.best_score = best_score
            self.quizzes = loaded_quizzes
            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
```

### ② 실행 진입부 (`main.py` 하단)
`Ctrl+C`(`KeyboardInterrupt`) 입력 시에도 데이터가 유실되지 않도록 `try-except-finally` 블록을 구성합니다:

```python
game = QuizGame(quizzes)

try:
    game.load_state()
    game.show_menu()

except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되어 프로그램을 종료합니다.")

finally:
    game.save_state()
```

### ③ 터미널 커밋
```bash
git add main.py
git commit -m "Feat: Add JSON persistence, random quiz order, and test screenshots"
```

---

## 💻 8단계: 미션 13번 저장소 복제 실습 (`clone` & `pull`)

두 개발자가 협업하는 과정을 내 컴퓨터 안에서 흉내 내는 미션 필수 실습입니다:

```bash
# 1. 원격 저장소 최신 변경사항 동기화 (pull 실습)
git pull origin main

# 2. 상위 폴더로 이동 후 복제본 생성 (clone 실습)
cd ..
git clone https://github.com/PuffyCripsy/E1-2-python-basics.git E1-2-clone-practice
```

---

## 💻 9단계: 과제 제출 스크린샷 12종 확인

`docs/screenshots/` 폴더에 아래 12종의 스크린샷이 정상적으로 배치되어 있는지 확인합니다:

1. `01_quiz_list.png`: 기본 퀴즈 목록 조회 (메뉴 3번)
2. `02_quiz_add.png`: 새로운 퀴즈 추가 (메뉴 2번)
3. `03_quiz_list_updated.png`: 추가된 퀴즈가 반영된 목록 조회 (메뉴 3번)
4. `04_quiz_result.png`: 퀴즈 풀기 진행 및 최종 점수 결과 (메뉴 1번)
5. `05_random_quiz.png`: [보너스] 퀴즈 무작위(랜덤) 출제 검증
6. `06_best_score.png`: 최고 점수 확인 (메뉴 4번)
7. `07_json_saved.png`: `state.json` 파일 영속 저장 확인
8. `08_quiz_reload.png`: 프로그램 재실행 후 퀴즈 목록 자동 복원 검증
9. `09_best_score_reload.png`: 프로그램 재실행 후 최고 점수 복원 검증
10. `10_invalid_input.png`: 메뉴 및 정답 입력 예외 처리 검증
11. `11_git_pull.PNG`: 원격 변경사항 가져오기(`git pull`) 검증
12. `12_git_clone.PNG`: 별도 디렉터리 저장소 복제(`git clone`) 검증

---

## 📄 부록: `main.py` 최종 완성 코드 전문

아래 코드는 모든 필수 요구사항과 보너스 과제(랜덤 출제), 예외 처리가 반영된 실제 동작 코드입니다:

```python
import json
import random

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.score = 0
        self.best_score = 0

    def play_quiz(self):
        self.score = 0
        shuffled_quizzes = random.sample(self.quizzes, len(self.quizzes))

        for quiz_number, quiz in enumerate(shuffled_quizzes, start=1):
            print(f"\n문제 {quiz_number}. {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            while True:
                user_input = input(
                    "정답 번호를 입력하세요 (1~4): "
                ).strip()

                if user_input in ["1", "2", "3", "4"]:
                    user_answer = int(user_input)
                    break

                print("잘못된 입력입니다. 1~4 중에서 선택하세요.")

            if user_answer == quiz.answer:
                print("정답입니다!")
                self.score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(
            f"\n퀴즈 종료! 총 {len(self.quizzes)}문제 중 "
            f"{self.score}문제를 맞혔습니다."
        )

        if self.score > self.best_score:
            self.best_score = self.score
            print("새로운 최고 점수입니다!")
            self.save_state()

    def show_menu(self):
        while True:
            print("\n===== 영어 문장 형식 퀴즈 =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 문제 추가")
            print("3. 퀴즈 문제 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")

            choice = input("메뉴를 선택하세요 (1~5): ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_best_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")

    def add_quiz(self):
        print("\n===== 새로운 퀴즈 추가 =====")

        question = input("영어 문장을 입력하세요: ").strip()

        while not question:
            print("문제를 비워 둘 수 없습니다.")
            question = input("영어 문장을 입력하세요: ").strip()

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 보기를 입력하세요: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("보기를 비워 둘 수 없습니다.")

        while True:
            answer = input("정답 번호를 입력하세요 (1~4): ").strip()

            if answer in ["1", "2", "3", "4"]:
                answer = int(answer)
                break

            print("잘못된 입력입니다. 1~4 중에서 선택하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print("새로운 퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        print("\n===== 등록된 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for quiz_number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {quiz_number}. {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            print(f"정답: {quiz.answer}번")

        print(f"\n총 {len(self.quizzes)}개의 문제가 등록되어 있습니다.")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print(f"현재 최고 점수: {self.best_score}점")

    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }

        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터가 저장되었습니다.")

        except OSError as error:
            print(f"데이터 저장 중 오류가 발생했습니다: {error}")

    def load_state(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            best_score = data["best_score"]
            saved_quizzes = data["quizzes"]

            if not isinstance(best_score, int) or best_score < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            if not isinstance(saved_quizzes, list):
                raise ValueError("퀴즈 목록 데이터가 올바르지 않습니다.")

            loaded_quizzes = []

            for item in saved_quizzes:
                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(isinstance(c, str) and c.strip() for c in choices)
                    or type(answer) is not int
                    or answer not in [1, 2, 3, 4]
                ):
                    raise ValueError("저장된 퀴즈 데이터가 올바르지 않습니다.")

                loaded_quizzes.append(Quiz(question, choices, answer))

            self.best_score = best_score
            self.quizzes = loaded_quizzes
            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")


quizzes = [
    Quiz(
        "The birds sing sweetly in the trees.",
        ["1형식", "2형식", "3형식", "4형식"],
        1
    ),
    Quiz(
        "This soup smells delicious.",
        ["1형식", "2형식", "3형식", "4형식"],
        2
    ),
    Quiz(
        "She solved the difficult math problem.",
        ["2형식", "3형식", "4형식", "5형식"],
        2
    ),
    Quiz(
        "My grandmother sent me a wonderful present.",
        ["1형식", "3형식", "4형식", "5형식"],
        3
    ),
    Quiz(
        "The coach encouraged the players to do their best.",
        ["2형식", "3형식", "4형식", "5형식"],
        4
    )
]

game = QuizGame(quizzes)

try:
    game.load_state()
    game.show_menu()

except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되어 프로그램을 종료합니다.")

finally:
    game.save_state()
```
