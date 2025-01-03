import operator

cases = input()

for i in range(int(cases)):
    
    num = input()
    num = int(num)
    
    resp = []
    qual = []

    for j in range(num):
        temp = list(map(int, input().split()))
        resp.append(temp[0])
        qual.append(temp[1])

    zipped = zip(resp, qual)
    zipped1 = zip(resp, qual)
    
    res = sorted(zipped, key = operator.itemgetter(1)) [::-1]

    res1 = list(res)
    zip1 = list(zipped1)

    # print(res1)
    # print(zip1)

    resp1, qual1 = zip(*res)

    for k in range(int(num)):
        if resp1[k] <= 10:
            print(zip1.index(res1[k]) + 1)
            break


