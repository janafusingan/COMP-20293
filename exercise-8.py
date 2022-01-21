# 8

score = int(input("Enter your Examination Score : "))

if score >= 0 and score <= 100:
    print("Your Letter Grade is", end=" ")

    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    elif score >= 0 and score <= 59:
        print("E")

else:
    print("Invalid Examination Score")
