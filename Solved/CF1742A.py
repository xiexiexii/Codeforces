cases = input()

for i in range(int(cases)):

    keys = list(map(int, input().split()))
    keys.sort()

    if keys[0] + keys[1] == keys[2]:
        print("YES")
    else:
        print("NO")

