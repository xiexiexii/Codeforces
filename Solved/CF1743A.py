cases = input()

for i in range(int(cases)):

    num = input()
    num = int(num)
    keys = list(map(int, input().split()))

    print((10 - num) * (9 - num) * 3)