class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


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


for quiz_number, quiz in enumerate(quizzes, start=1):
    print(f"문제 {quiz_number}. {quiz.question}")

    for number, choice in enumerate(quiz.choices, start=1):
        print(f"{number}. {choice}")

    print()