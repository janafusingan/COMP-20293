# 18

from typing import overload


over_limit = int(input("Enter Over Limit : "))

if over_limit > 0:
    print("Your FINE is", end=" ")

    if over_limit >= 1 and over_limit <= 10:
        print("10 Pesos")
    elif over_limit >= 11 and over_limit <= 20:
        print("20 Pesos")
    elif over_limit >= 21 and over_limit <= 30:
        print("30 Pesos")
    elif over_limit >= 31 and over_limit <= 40:
        print("40 Pesos")
    else:
        print("50 Pesos")
else:
    print("Invalid Input")
