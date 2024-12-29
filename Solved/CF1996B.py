cases = input()

for i in range(int(cases)):

    array = []
    info = list(map(int, input().split()))

    for j in range(info[0]):
        array.append(input())
    
    # if info[1] == 1:
    #    for j in range(info[0]):
    #        print(array[j])
    # else:
        
    for j in range(info[0]):
        line = list(array[j])
        for k in range(info[0]):
            if k % info[1] != 0:
                line[k] = ""
        array[j] = "".join(line)
    
    for l in range(len(array)):
        if l % info[1] == 0:
            print(array[l])
            