# 20

income = float(input("Enter NTI Amount : "))

print("Your TAX Due is", end=" ")
if income < 2500:
    print("0")
elif income >= 2500 and income < 5000:
    print(100 + (0.03 * income))
elif income >= 5000 and income < 10000:
    print(175 + (0.03 * income))
elif income >= 10000 and income < 25000:
    print(425 + (0.08 * income))
elif income >= 25000 and income < 50000:
    print(1625 + (0.13 * income))
else:
    print(4875 + (0.13 * income))