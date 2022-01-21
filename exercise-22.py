# 22

# temp for temperature
temp = float(input("Enter the temperature to be converted : ")) 
unit = str(input("Enter Unit of Temperature (C or F)    : "))

print("")

if unit.lower() == 'c' or unit.lower() == 'f':
    print("The equivalent", end=" ")
    if unit.lower() == 'f':
        print("Celsius is", (5.0/9.0) * (temp-32.0))
    else:
        print("Fahrenheit is", (9.0/5.0) * temp + 32)

else:
    print("Invalid Input of Unit")
