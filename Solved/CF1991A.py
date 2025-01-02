cases = input()

for i in range(int(cases)):

    length = input()
    array = list(map(int, input().split()))
    short = []

    for j in range(int(length)):
        if j % 2 == 0:
            short.append(array[j])
    
    short.sort()
    print(short[len(short) - 1])