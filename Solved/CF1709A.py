cases = input()

for i in range(int(cases)):

    key = input()
    key = int(key)

    keys  = list(map(int, input().split()))

    if keys[key - 1] != 0 and keys[keys[key - 1] - 1] != 0:
        print("YES")
    else:
        print("NO")