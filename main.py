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
        self.has_played = False

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

        self.has_played = True

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

        if not self.has_played:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"현재 최고 점수: {self.best_score}점")

    def save_state(self):
        data = {
        "best_score": self.best_score,
        "has_played": self.has_played,
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
            has_played = data.get("has_played", False)
            saved_quizzes = data["quizzes"]

            if not isinstance(best_score, int) or best_score < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            if not isinstance(has_played, bool):
                raise ValueError("퀴즈 진행 기록이 올바르지 않습니다.")

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
            self.has_played = has_played
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