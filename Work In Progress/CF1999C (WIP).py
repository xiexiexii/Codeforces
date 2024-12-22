cases = input()

for i in range(int(cases)):

    times = []
    isTrue = False
    
    info = input().split()

    for j in range(len(info)):
        info[j] = int(info[j])
    
    for k in range(info[0]):
        times += input().split()
    
    for l in range(len(times)):
        times[l] = int(times[l])

    if int(times[0]) == int(info[1]):
        isTrue = True
        print("YES")
    
    times.append(info[2])
    
    for k in range(info[0]):

        # print(int(times[2 * (k + 1)]) - int(times[2 * (k + 1) - 1]) + 1)

        if k == info[0] - 1:
            if not int(times[2 * (k + 1)]) - int(times[2 * (k + 1) - 1]) >= info[1]:
                break

        if int(times[2 * (k + 1)]) - int(times[2 * (k + 1) - 1]) + 1 >= info[1]:
            isTrue = True
            print("YES")
            break
    
    if not isTrue:
        print("NO")
