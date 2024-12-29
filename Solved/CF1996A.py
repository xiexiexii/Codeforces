cases = input()

for i in range(int(cases)):

    legs = input()
    print(int(int(legs) / 4 + (int(legs) % 4) / 2))