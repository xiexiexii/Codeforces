cases = input()

for i in range(int(cases)):
    length = input()
    array = input().split()
    count = 0
    maxCount = 0

    for j in range(int(length)):
        if array[j] == "0" and j == int(length) - 1:
            count += 1
            if count > maxCount:
                maxCount = count
        if array[j] == "0":
            count += 1
        else:
            if count > maxCount:
                maxCount = count
                count = 0
    print(maxCount)
        