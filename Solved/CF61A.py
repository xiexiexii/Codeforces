num1 = list(input())
num2 = list(input())
num3 = []

for j in range(len(num1)):
    if num1[j] == num2[j]:
        num3.append("0")
    else:
        num3.append("1")

print("".join(num3))
