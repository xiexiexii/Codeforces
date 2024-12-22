cases = input()
cases = int(cases)

for i in range(cases):

    num = list(input())

    for j in range(len(num)):
        num[j] = int(num[j])

    add = 0

    for i in num:
        add += i

    print(add)
