cases = input()
cases = int(cases)

for i in range(cases):

    keys = input().split()

    keys[0] = int(keys[0])
    keys[1] = int(keys[1])

    if keys[0] < keys[1]:
        start = keys[0]
    else:
        start = keys[1]

    while(True):
        if start % keys[0] == start % keys[1]:
            print(start)
            break
        else:
            start += 1
