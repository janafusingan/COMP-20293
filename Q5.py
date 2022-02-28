def scores(qz, exam):
    stats = 0
    error = 0
    for i in qz:
        if i >= 50 and i <= 100:
            stats += 1
        elif i < 0 or i > 100:
            error += 1
    if exam < 0 or exam > 100:
        error += 1
    if error == 0:
        if exam >= 50 and stats >= 3:
            print("You've Passed")
        else:
            print("You've Failed")
    else:
        print("One of the scores is not valid")


ans = True
while ans:
    quizzes = []
    for i in range(6):
        if i < 5:
            print("Enter quiz", i + 1, "Score : ", end="")
            quiz = int(input())
            quizzes.append(quiz)
        else:
            exam = int(input("Enter Final Exam Score : "))
    print()
    scores(quizzes, exam)
    print()
    a = input("Enter for another scores (Y/N) ? ")
    if a == 'Y' or a == 'y':
        ans = True
    else:
        ans = False