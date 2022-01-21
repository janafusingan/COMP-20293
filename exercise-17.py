# 17

hours = int(input("Enter Parking Hours : "))

if hours > 0 and hours <= 24:
    print("Parking Charge is   :", end=" ")

    # print the minimum charge for 1 hour of parking
    if hours == 1:
        print(30)

    # print the min charge plus the added charge (20 for every extra hours)
    # this is for the charge below the max charge
    elif hours < 10:
        print(30 + ((hours - 1) * 20))
    
    # print the maximum charge of 200
    else:
        print(200)
        
else:
    print("Invalid Entry")