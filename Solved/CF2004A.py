cases = input()

for i in range(int(cases)):

    unique = []

    count = input()

    info = input().split()

    for j in range(len(info)):
        info[j] = int(info[j])
        if info[j] not in unique:
            unique.append(info[j])

    if len(unique) > 2 or unique[1] == unique[0] + 1:
        print ("NO")
    else:
        print("YES")
