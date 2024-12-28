cases = input()

for i in range(int(cases)):
    length = input()
    array = list(map(int, input().split()))
    count = 0
    maxCount = 0
    num1 = 0
    num2 = 0

    for j in range(int(length)):
        if array[j] == "0" and j == int(length) - 1:
            count += 1
            if count > maxCount:
                maxCount = count
                count = 0
        elif array[j] == "0":
            count += 1
        else:
            if count > maxCount:
                maxCount = count
                count = 0
        
    print(maxCount)
        