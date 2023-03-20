print("Welcome to the best multiple choice football questionnaire around!")
print("You will be presented with 10 questions and they will progressively start to get harder")
print('Goodluck!')

questions = [
    {
        "question": "Who currently has the most ballon d'ors in history?",
        "options": ["A) Cristiano Ronaldo", "B) Lionel Messi", "C) Zinedine Zidane"],
        "answer": "B"
    },
    {
        "question": "How many goals has Erling Haaland scored this season in the premier league?",
        "options": ["A) 26", "B) 27", "C) 28"],
        "answer": "C"
    },
    {
        "question": "Which player has the most minutes played in premier league history?",
        "options": ["A) James Milner", "B) David De Gea", "C) Ben Foster"],
        "answer": "B"
    },
    {
        "question": "?",
        "options": ["A) ", "B) ", "C) "],
        "answer": "A"
    },
    {
        "question": "?",
        "options": ["A) ", "B) ", "C) "],
        "answer": "C"
    },
    {
        "question": "?",
        "options": ["A) ", "B) ", "C) "],
        "answer": "A"
    },
    {
        "question": "Which player has the most red cards in history?",
        "options": ["A) Paolo Montero ", "B) Gerardo Bedoya", "C) Sergio Ramos"],
        "answer": "B"
    },
    {
        "question": "?",
        "options": ["A) ", "B) ", "C) "],
        "answer": "A"
    },
    {
        "question": "?",
        "options": ["A) ", "B) ", "C) "],
        "answer": "C"
    },
    {
        "question": "Which player has scored the most own goals in premier league history? ",
        "options": ["A) Richard Dunne", "B) Jamie Carragher", "C) Phil Jagielka"],
        "answer": "A"
    }
]

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, or C): ")
    if user_answer.upper() == q["answer"]:
        print("Correct!")
    else:
        print("Incorrect!")


