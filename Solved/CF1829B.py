cases = input()

for i in range(int(cases)):

    length = input()
    array = list(map(int, input().split()))
    count = 0
    maxCount = 0

    for j in range(int(length)):
        if array[j] == 0:
            count += 1
            # print("j: " + str(j))
            # print("count: " + str(count))
        else:
            if count > maxCount:
                maxCount = count
            count = 0

    if count > maxCount:
        maxCount = count
        count = 0 
    print(maxCount)
        