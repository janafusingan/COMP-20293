# 3

vowels = ["a", "e", "i", "o", "u"]

str1 = input(str("Enter an Alphabet: "))

# check if the input is a digit or an alphabet
#if str1.isdigit:
#     print("Invalid Input")
# else:
if str1.lower() in vowels:
    print(str1, "is a vowel")
else:
    print(str1, "is a consonant")