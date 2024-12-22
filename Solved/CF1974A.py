cases = input()

for i in range(int(cases)):

    screens = input().split()
    total = 0

    screens[0] = int(screens[0])
    screens[1] = int(screens[1])

    if (screens[1] % 2) == 0:
        total = int(screens[1] / 2)
        screens[0] = screens[0] -  7 * total
        if screens[0] > 0:
            total += int(screens[0] / 15)
            if screens[0] % 15 > 0:
                total += 1
            print(total)
        else:
            print(total)
    else:
        total = int(screens[1] / 2) + 1
        screens[0] = screens[0] -  (7 * total + 4)
        if screens[0] > 0:
            total += int(screens[0] / 15)
            if screens[0] % 15 > 0:
                total += 1
            print(total)
        else:
            print(total)