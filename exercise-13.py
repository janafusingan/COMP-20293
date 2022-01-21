# 13

amount = float(input("Enter PURCHASE AMOUNT : "))
discount = 0

if amount >= 1000:
    discount = amount * 0.1

print("Your DISCOUNT is      :", discount)
print("Your NET BILL is      :", amount - discount)