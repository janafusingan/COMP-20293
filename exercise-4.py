# 4


print()
print("\t\tSubject Pass or Failed Program")
print()
subject = str(input("Enter your subject : "))
grade = int(input("Enter your grade    : "))
print()

if grade >= 75 and grade <= 100:
    print("You Pass your subject", subject, "with the grade of", grade)
else:
    print("You Failed your subject", subject, "with the grade of", grade)

print()