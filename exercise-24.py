# 24 

hours = int(input("Number of Hours : "))
weekly_sales = float(input("Weekly Sales    : "))

print("")

a, b, c = 0, 0, 0

if hours >= 30 and hours < 50:
    a = 200 + (weekly_sales * 0.1)
elif hours >= 50:
    a = 300 + (weekly_sales * 0.1)
else:
    a = weekly_sales * 0.1

print("Plan A          :", a)

if hours <= 40:
    b = (7.50 * hours) + (weekly_sales * 0.07)
else:
    b = 300 + (10 * (hours - 40)) + (weekly_sales * 0.07)

print("Plan B          :", b)

c = weekly_sales * 0.15
print("Plan C          :", c)

print("")

if a > b and a > c:
    print("Plan A is the best wage plan")
elif b > a and b > c:
    print("Plan B is the best wage plan")
else:
    print("Plan C is the best wage plan")