
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.score = 0

    def play_quiz(self):
        self.score = 0

        for quiz_number, quiz in enumerate(self.quizzes, start=1):
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
            elif choice in ["2", "3", "4"]:
                print("이 기능은 다음 단계에서 구현합니다.")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")
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
game.show_menu()
        