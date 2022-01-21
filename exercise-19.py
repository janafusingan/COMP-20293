# 19

quiz1 = int(input("Enter Quiz 1 Score     : "))
quiz2 = int(input("Enter Quiz 2 Score     : "))
quiz3 = int(input("Enter Quiz 3 Score     : "))
quiz4 = int(input("Enter Quiz 4 Score     : "))
quiz5 = int(input("Enter Quiz 5 Score     : "))
quiz6 = int(input("Enter Quiz 6 Score     : "))
exam = int(input("Enter Final Exam Score : "))

x = 0
ctr = 0;

print("")
quiz = []
quiz.append(quiz1)
quiz.append(quiz2) 
quiz.append(quiz3)
quiz.append(quiz4)
quiz.append(quiz5)
quiz.append(quiz6)

# check if the exam score is equal or greather than 50 (passing score)
if exam >= 50:
    # check if quiz score is equal or greather than 50 (passing score)
    # if true, then add 1 to ctr (counter) which counts the quizzes passed
    for x in quiz:
        if x >= 50:
            ctr += 1

    # checks if the student passed 3 or more quiz
    if ctr >= 3:
        print("You've Passed")
    else:
        print("You've Failed")
else:
    print("You've Failed")

