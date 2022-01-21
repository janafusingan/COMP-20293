# 10

num = int(input("Enter Purchased Balls : "))

if num > 0:
    print("Cost is", end=" ")

    if num < 3:
        print(num * 300)
    elif num >= 3 and num < 10:
        print(num * 250)
    elif num >= 10:
        print(num * 200)

else:
    print("Invalid Input")