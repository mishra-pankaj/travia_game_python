import random

questions = {
    "What is the capital of France?":"paris",
    "How many continents are there in the world?":"7",
    "What planet is known as the Red Planet?":"Mars",
    "Which animal is known as the King of the Jungle?":"Lion",
    "How many days are there in a leap year":"366"
}

def python_trivai_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answere = input("your answere: ").lower().strip()

        correct_answere = questions[question]

        if user_answere == correct_answere.lower():
            print("correct!\n")
            score +=1

        else:
            print(f"wrong. The correct answere is :{correct_answere}.\n")

    print(f"YOUR TOTAL SCORE IS: {score}/{total_questions}")

python_trivai_game()