# 23

hours = int(input("Total Number of hours : "))
print("Parking Fee           :", end=" ")

if hours > 3:
    print(30 + (hours - 3) * 12)
else:
    print(30)