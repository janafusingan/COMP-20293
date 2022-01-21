# 16

unit_price = float(input("Enter Unit Price : "))
quantity = int(input("Enter Quantity   : "))
discount = 0
total = unit_price * quantity

print("")

if unit_price > 0:
    if quantity > 0:
        print("Your Bill")
        print("----------")

        if quantity >= 10 and quantity <= 19:
            discount = total * 0.2
            print("You are entitled to 20% discount")
        elif quantity >= 20 and quantity <= 49:
            discount = total * 0.3
            print("You are entitled to 30% discount")
        elif quantity >= 50 and quantity <= 99:
            discount = total * 0.4
            print("You are entitled to 40% discount")
        elif quantity >= 100:
            discount = total * 0.5
            print("You are entitled to 50% discount")

        print("")
        print("Total Purchase Cost :", total )
        print("Discount Amount     :", discount)
        print("Net Cost Amount     :", total - discount)

    else:
        print("Invalid Quantity, Enter value greater than 0")
else:
    print("Invalid Unit Price, Enter value greater than 0")