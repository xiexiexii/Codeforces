cases = input()

for i in range(int(cases)):

    strip = 0
    count = 0
    length = []
    isTrue = False

    info = input().split()

    info[0] = int(info[0])
    info[1] = int(info[1])

    for j in range(info[0]):
        length.append(len(input()))

    for k in range(info[0]):
        if strip + length[k] > info[1]:
            print(count)
            isTrue = True
            break
        elif strip + length[k] == info[1]:
            print(count + 1)
            isTrue = True
            break
        else:
            strip += length[k]
            count += 1
    
    if not isTrue:
        print(count)
    