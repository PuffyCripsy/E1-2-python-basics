# E1-2 파이썬 & Git 핵심 완전정복 (원투펀치 시험 대비 노트)

> **코디세이(Codyssey) E1-2 미션 목표 기반 주간 시험 완벽 대비**  
> 개념 설명 + 실제 코드 예시 + 코드 뜻 한 줄씩 풀기 + 시험 단골 문제 & 오답 함정 + 한 줄 암기 팁 수록

---

## 📑 목차

1. [파이썬 필수 자료형 5개](#1-파이썬-필수-자료형-5개)
2. [사용자 입력과 형변환 (`input`, `strip`, `int`)](#2-사용자-입력과-형변환)
3. [조건문과 반복문 (`if/elif/else`, `while True`, `for`)](#3-조건문과-반복문)
4. [클래스와 객체 (`class`, `__init__`, `self`) ★핵심★](#4-클래스와-객체)
5. [파일 입출력과 영속성 (`with open`, JSON)](#5-파일-입출력과-영속성)
6. [예외 처리 (`try - except`)](#6-예외-처리)
7. [★시험 최다 오답 함정★ `print()` vs `return` 차이](#7-시험-최다-오답-함정-print-vs-return-차이)
8. [Git 핵심 7대 명령어와 협업 흐름 (`clone` vs `pull`)](#8-git-핵심-7대-명령어와-협업-흐름)
9. [실전 알짜 내장 함수 3선 (`enumerate`, `isinstance`, `random.sample`)](#9-실전-알짜-내장-함수-3선)

---

## 1. 파이썬 필수 자료형 5개

| 자료형 | 이름 | 예시 | 특징 및 용도 |
| :---: | :---: | :--- | :--- |
| **`int`** | 정수 | `10`, `0`, `-5` | 소수점 없는 숫자. 사칙연산 가능 |
| **`str`** | 문자열 | `"apple"`, `"123"` | 따옴표로 감싼 글자 데이터 |
| **`bool`** | 불리언 | `True`, `False` | 참과 거짓. 조건문 판단의 기준 |
| **`list`** | 리스트 | `["1형식", "2형식", "3형식"]` | 순서가 있는 목록. 대괄호(`[]`), 인덱스 접근(`list[0]`) |
| **`dict`** | 딕셔너리 | `{"question": "문장", "answer": 1}` | Key-Value 쌍. 중괄호(`{}`), 키로 값 찾기(`dict["answer"]`) |

🎯 **한 줄 암기**:  
"숫자는 int, 글자는 str, 목록은 list, 키와 값 짝궁은 dict!"

---

## 2. 사용자 입력과 형변환

```python
user_input = input("정답 번호를 입력하세요 (`1~4`): ").strip()

if user_input in ["1", "2", "3", "4"]:
    user_answer = int(user_input)
```

### 🔍 코드 한 줄씩 뜻 풀기
- `input(...)`: 사용자가 키보드로 입력한 값을 읽어옵니다.  
  👉 **핵심**: 사용자가 숫자 `1`을 입력해도 파이썬에는 무조건 **문자열(`"1"`)**로 들어옵니다.
- `.strip()`: 앞뒤에 실수로 들어간 공백(`" 1 "`)을 잘라내어 깨끗한 `"1"`로 정제합니다.
- `if user_input in ["1", "2", "3", "4"]`: 사용자가 입력한 문자열이 허용된 선택지 목록 안에 있는지 검사합니다.
- `int(user_input)`: 문자열 `"1"`을 진짜 계산 및 비교가 가능한 정수 숫자 `1`로 형태를 바꿉니다(형변환).

### 📝 시험 출제 포인트
- `type(input())`의 반환 타입은 무조건 `str`이다. (O)
- `int("123")`은 숫자 `123`이 되지만, `int("abc")`는 변환할 수 없어 `ValueError`가 발생한다.

---

## 3. 조건문과 반복문

### (1) `if` / `elif` / `else` (조건문)
```python
if choice == "1":
    self.play_quiz()
elif choice == "2":
    self.add_quiz()
else:
    print("잘못된 입력입니다.")
```
- **`if`**: 맨 처음 조건을 검사합니다.
- **`elif`**: 앞선 조건이 `False`(거짓)일 때만 다음 조건을 검사합니다.
- **`else`**: 위의 모든 조건이 전부 `False`일 때 마지막으로 실행됩니다.

### (2) `while`문 vs `for`문 (반복문 비교)

```python
# [while문] 사용자가 5번(종료)을 누를 때까지 끝없이 메뉴를 보여줌
while True:
    choice = input("메뉴 선택: ")
    if choice == "5":
        print("종료합니다.")
        break  # 반복문을 즉시 깨고 탈출!

# [for문] 준비된 퀴즈 5문제를 처음부터 끝까지 하나씩 꺼내 출제
for quiz in self.quizzes:
    print(quiz.question)  # 5문제가 끝나면 자동으로 반복 종료
```

| 구분 | `while`문 | `for`문 |
| :---: | :--- | :--- |
| **반복 기준** | **조건**이 참인 동안 계속 반복 | 정해진 **범위/리스트의 개수**만큼 반복 |
| **사용 상황** | 언제 끝날지 모를 때 (메뉴 반복, 올바른 입력 재요청) | 반복할 횟수나 대상이 명확할 때 (퀴즈 목록 순회) |
| **탈출 키워드** | `break` (반복문 즉시 종료) | `break` 또는 목록 순회 완료 시 자동 종료 |

🎯 **한 줄 암기**:  
"끝나는 시점을 모를 땐 while True, 정해진 리스트 돌릴 땐 for in!"

---

## 4. 클래스와 객체

클래스는 서로 연관된 **데이터(속성)**와 **기능(메서드)**을 하나로 묶어 관리하는 설계도입니다.

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 속성
        self.choices = choices    # 보기 속성
        self.answer = answer      # 정답 속성

# 실제 객체(인스턴스) 찍어내기
q1 = Quiz("The birds sing sweetly.", ["1형식", "2형식", "3형식", "4형식"], 1)
```

### 🔍 코드 한 줄씩 뜻 풀기
- `class Quiz:`: `Quiz`라는 이름의 새로운 클래스(설계도)를 정의합니다.
- `def __init__(self, ...):`: 객체가 처음 생성될 때 파이썬이 자동으로 실행해 주는 **생성자(초기화 함수)**입니다.
- `self`: "방금 막 만들어진 **이 객체 자기 자신**"을 가리키는 대명사입니다.
- `self.question = question`: 전달받은 문제 문장을 객체 자신의 속성(`self.question`)에 보관합니다.
- `q1 = Quiz(...)`: 설계도를 바탕으로 메모리에 실제 퀴즈 객체 `q1`을 만듭니다.  
  👉 `q1.question`을 호출하면 저장해 둔 `"The birds sing sweetly."`가 출력됩니다.

### 📝 시험 출제 포인트
- **속성(Attribute)**: 객체가 가지고 있는 데이터/변수 (`self.score`, `self.quizzes`)
- **메서드(Method)**: 객체가 수행하는 행동/함수 (`def play_quiz(self):`)
- 클래스 내부 메서드의 첫 번째 매개변수는 반드시 `self`여야 한다.

---

## 5. 파일 입출력과 영속성

프로그램이 종료되어도 데이터가 사라지지 않고 하드디스크에 보존되는 것을 **데이터 영속성(Persistence)**이라고 합니다.

```python
import json

data = {
    "best_score": 100,
    "quizzes": [
        {"question": "문장", "answer": 1}
    ]
}

# 파일 저장 (쓰기 모드 'w')
with open("state.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 파일 읽기 (읽기 모드 'r')
with open("state.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
```

### 🔍 코드 한 줄씩 뜻 풀기
- `open("state.json", "w", encoding="utf-8")`: `state.json` 파일을 쓰기(`"w"`) 모드로 엽니다. 한글 깨짐을 방지하기 위해 `utf-8` 인코딩을 지정합니다.
- `with ... as file:`: `with` 블록이 끝나면 파이썬이 알아서 `file.close()`를 실행해 안전하게 파일을 닫습니다.
- `json.dump(data, file)`: 파이썬의 딕셔너리 데이터를 JSON 형태의 텍스트로 파일에 씁니다.
- `json.load(file)`: 파일 속 JSON 텍스트를 파이썬의 딕셔너리/리스트로 변환해 읽어옵니다.

---

## 6. 예외 처리

에러가 발생했을 때 프로그램이 비정상 종료(강제 튕김)되지 않고 안전하게 복구되도록 만드는 기법입니다.

```python
try:
    number = int("abc")  # 숫자로 바꿀 수 없어 ValueError 발생!
    print("성공")
except ValueError:
    print("숫자가 아닙니다. 다시 입력하세요.")
```

### 🔍 실행 순서
1. `try:` 블록의 코드를 실행합니다.
2. `int("abc")`에서 에러(`ValueError`)가 발생하는 즉시 실행을 멈추고 `except ValueError:` 블록으로 점프합니다.
3. `"숫자가 아닙니다. 다시 입력하세요."`를 출력하고 프로그램이 멈추지 않고 정상 진행됩니다.

### 📝 코디세이 시험 필수 예외 3대장
- **`ValueError`**: 자료형 변환 실패 (`int("abc")`, 범위 밖 값)
- **`FileNotFoundError`**: 열려고 하는 파일이 디렉터리에 존재하지 않을 때 (`open("none.json")`)
- **`ZeroDivisionError`**: 숫자를 `0`으로 나누려고 할 때 (`10 / 0`)

---

## 7. ★시험 최다 오답 함정★ `print()` vs `return` 차이

초보자 시험에서 가장 많은 오답이 발생하는 핵심 함정 문제입니다.

```python
# [경우 A] print만 작성한 함수
def add_print(a, b):
    print(a + b)

# [경우 B] return을 작성한 함수
def add_return(a, b):
    return a + b
```

### 💥 실행 결과 비교
```python
# A 실행: 화면에 5는 출력되지만 변수에는 아무것도 담기지 않음
result_a = add_print(2, 3)
print(result_a)         # 출력: None (비어 있음)
print(result_a + 10)    # 💥 TypeError 발생! (None과 10은 더할 수 없음)

# B 실행: 화면엔 바로 안 뜨지만 변수에 결과값 5가 쏙 담김
result_b = add_return(2, 3)
print(result_b)         # 출력: 5
print(result_b + 10)    # ✅ 출력: 15 (정상 계산)
```

| 구분 | `print()` | `return` |
| :---: | :--- | :--- |
| **목적** | 사람 눈에 보이게 모니터 화면에 출력 | 함수를 호출한 곳으로 결과값을 전달 |
| **반환값** | 없음 (`None`) | 지정한 결과값 |
| **이후 연산** | 반환값이 없으므로 다음 계산에 사용 불가 | 변수에 저장하여 다음 계산/로직에 활용 가능 |

### 📝 시험 문제 예시
**Q. 다음 코드 실행 후 변수 `x`의 값은?**
```python
def calc():
    print(100)

x = calc()
```
- 정답: **`None`**  
  (화면에 `100`이 찍히는 것과 관계없이, `return`이 명시되지 않은 파이썬 함수의 기본 반환값은 항상 `None`입니다.)

🎯 **한 줄 암기**:  
"모니터에 띄우고 끝내려면 print, 다음 코드가 쓰게 값을 넘겨주려면 return!"

---

## 8. Git 핵심 7대 명령어와 협업 흐름

Git은 코드 변경 이력을 시간 순서대로 기록하고 협업을 지원하는 분산 버전 관리 시스템입니다.

### (1) 핵심 7대 명령어 요약

| 명령어 | 역할 및 동작 | 시험 핵심 포인트 |
| :--- | :--- | :--- |
| **`git init`** | 현재 디렉터리를 Git 로컬 저장소로 초기화 | 프로젝트 시작 시 딱 1번 실행 |
| **`git add .`** | 작업한 파일들을 스테이징 영역(Staging Area)에 올림 | 커밋할 대상을 준비하는 단계 |
| **`git commit -m "메시지"`** | 스테이징된 파일들을 하나의 영구 버전(스냅샷)으로 확정 | 의미 있는 작업 단위로 분리 |
| **`git push origin main`** | 로컬의 커밋 내역을 원격 GitHub 저장소로 전송 | 내 PC ➔ GitHub 원격 저장소 |
| **`git pull origin main`** | GitHub 원격의 최신 변경사항을 가져와 현재 로컬에 병합 | **이미 있는 로컬 폴더**에서 최신화 |
| **`git clone [URL]`** | 원격 저장소를 내 PC에 **통째로 새로 복제** | **처음 시작할 때** 폴더 생성 |
| **`git checkout -b [이름]`** | 새로운 브랜치를 생성함과 동시에 해당 브랜치로 이동 | 독립된 기능 개발을 위한 가지 분기 |

### (2) ★시험 킬러 문항★ `clone` vs `pull` 차이

- **`git clone`**:
  - 내 컴퓨터에 프로젝트 폴더가 **없을 때** 사용합니다.
  - 원격 저장소의 전체 커밋 히스토리와 브랜치를 **통째로 내려받아 새 디렉터리를 생성**합니다.
- **`git pull`**:
  - 내 컴퓨터에 **이미 프로젝트 폴더가 존재할 때** 사용합니다.
  - 원격 저장소에 새로 추가된 커밋들만 가져와서(`fetch`) 현재 내 로컬 브랜치에 합칩니다(`merge`).

### (3) 브랜치 생성 및 병합 4단계
```bash
# 1. 새로운 기능 브랜치 생성 및 이동
git checkout -b feature/quiz-play

# 2. 코드 작업 후 커밋
git add main.py
git commit -m "Feat: 퀴즈 풀기 기능 구현"

# 3. 메인(main) 브랜치로 복귀
git checkout main

# 4. 기능 브랜치의 작업 내용을 main 브랜치로 병합
git merge feature/quiz-play
```

---

## 9. 실전 알짜 내장 함수 3선

### (1) `enumerate(목록, start=1)`: 순서 번호와 요소를 동시에 꺼내기
```python
choices = ["1형식", "2형식", "3형식", "4형식"]

# start=1을 주면 1번부터 번호가 시작됨
for number, choice in enumerate(choices, start=1):
    print(f"{number}. {choice}")
```

### (2) `isinstance(변수, 타입)`: 데이터 타입이 올바른지 검사하기
```python
score = 80

if isinstance(score, int):
    print("유효한 정수 점수입니다.")
```

### (3) `random.sample(리스트, 뽑을개수)`: 중복 없이 무작위로 추출하기
```python
import random

quizzes = ["Q1", "Q2", "Q3", "Q4", "Q5"]

# 리스트 전체 개수만큼 무작위 순서로 섞어서 추출 (랜덤 출제)
shuffled = random.sample(quizzes, len(quizzes))
```

---
💡 **최종 점검 안내**: 위 9가지 핵심 항목을 머릿속으로 그려보며 설명할 수 있다면, E1-2 주간 시험 및 CBT 문항은 100점 만점으로 통과할 수 있습니다!
