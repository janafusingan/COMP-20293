# 11

speed = int(input("Enter SPEED in kph : "))

if speed > 0:
    print("FINE in Pesos      :", end=" ")

    if speed <= 80:
        print(0)
    elif speed > 80 and speed <= 100:
        print(500)
    elif speed > 100:
        print(800)

else:
    print("Invalid Input")