cases = input()

for i in range(int(cases)):

    times = []
    isTrue = False
    
    info = list(map(int, input().split()))
    
    for k in range(info[0]):
        times += list(map(int, input().split()))

    if int(times[0]) >= int(info[1]):
        isTrue = True
        print("YES")
    else:
        times.append(info[2])
    
        for k in range(info[0]):

            # print(int(times[2 * (k + 1)]) - int(times[2 * (k + 1) - 1]))

            # if k == info[0] - 1:
            #    if times[len(times) - 1] - times[len(times) - 2] >= info[1]:
            #        isTrue = True
            #        print("YES")
            #        break
            if int(times[2 * (k + 1)]) - int(times[2 * (k + 1) - 1]) >= info[1]:
                isTrue = True
                print("YES")
                break
    
    if not isTrue:
        print("NO")
