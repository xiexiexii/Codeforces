cases = input()

for i in range(int(cases)):
    coins, req = map(int, input().split())

    if coins >= req:
        print(coins)
    elif 2 * coins - req > 0:
        print(2 * coins - req)
    else:
        print(0)
