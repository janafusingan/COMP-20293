purchase = float(input("Enter your purchase amount:₱"))
payment = float(input("Enter your payment amount:₱"))
vat = purchase * .12
vat = round(vat,2)
total = purchase + vat  # or total = purchase * 1.12
total = round(total,2)
change = payment - total
print()
if payment < total:
    print("Sorry your payment is not enough")
else:
    print("VAT Amount (12%) :₱",vat)
    print("Total Amount to be paid  :₱",total)
    print("Your change is ₱",change)
