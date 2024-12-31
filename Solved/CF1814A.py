cases = input()

for i in range(int(cases)):

    keys = list(map(int, input().split()))

    if (keys[0] % 2 == 1 and keys[1] % 2 == 0) or (keys[1] % 2 == 0 and keys[0] % 2 == 1 and 2 * keys[1] > keys[0]):
        print("NO")
    else:
        print("YES")
