cases = input()

for i in range(int(cases)):

    num = list(map(int, list(input())))

    if (num[0] + num[1] + num[2] == num[3] + num[4] + num[5]):
        print("YES")
    else:
        print("NO")