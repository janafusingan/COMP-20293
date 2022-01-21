# 6

num = []

for i in range(0, 5):
    print("Entry no.", i+1, ": ", end=" ")
    n = int(input())
    num.append(n)

print()
# sort the list in ascending order then print the last item in the list
num.sort()
print("Largest Number is", num[-1])
