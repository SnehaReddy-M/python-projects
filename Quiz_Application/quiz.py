def ask_question(question_num, question_data):
    print(f"\nQuestion {question_num}")
    print("-" * 40)

    print(question_data["question"])

    for option in question_data["options"]:
        print(option)

    while True:
        user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break

        print("Invalid input! Please enter A, B, C, or D.")

    if user_answer == question_data["answer"]:
        print("✅ Correct!")
        return 1
    else:
        print("❌ Incorrect!")
        print(f"Correct Answer: {question_data['answer']}")
        return 0


def show_result(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 40)
    print("🎉 QUIZ COMPLETED")
    print("=" * 40)

    print(f"Score      : {score}/{total_questions}")
    print(f"Percentage : {percentage:.2f}%")

    if percentage >= 80:
        print("🏆 Excellent Performance!")
    elif percentage >= 60:
        print("👍 Good Job!")
    else:
        print("📚 Keep Practicing!")


questions = [
    {
        "question": "What is the capital of India?",
        "options": [
            "A. Mumbai",
            "B. New Delhi",
            "C. Chennai",
            "D. Kolkata"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": [
            "A. function",
            "B. fun",
            "C. def",
            "D. define"
        ],
        "answer": "C"
    },
    {
        "question": "Which data type stores multiple values?",
        "options": [
            "A. int",
            "B. float",
            "C. string",
            "D. list"
        ],
        "answer": "D"
    },
    {
        "question": "How many days are there in a week?",
        "options": [
            "A. 5",
            "B. 6",
            "C. 7",
            "D. 8"
        ],
        "answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "A. Hyper Text Markup Language",
            "B. High Text Machine Language",
            "C. Hyper Tool Markup Language",
            "D. Home Text Markup Language"
        ],
        "answer": "A"
    }
]


def run_quiz():
    score = 0

    print("=" * 40)
    print("🎯 WELCOME TO THE PYTHON QUIZ")
    print("=" * 40)

    total_questions = len(questions)

    for index, question in enumerate(questions, start=1):
        score += ask_question(index, question)

    show_result(score, total_questions)


run_quiz()
