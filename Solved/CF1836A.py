cases = input()

for i in range(int(cases)):

    count = int(input())
    vals = list(map(int, input().split()))
    dist = []
    flag = False
    
    vals.sort()
    
    for j in range(vals[len(vals) - 1] + 1):
        dist.append(vals.count(j))

    # print(dist)

    for k in range(len(dist) - 1):
        if dist[k] < dist[k + 1]:
            print("NO")
            flag = True
            break

    if flag != True:
        print("YES")
        