cases = input()

for i in range(int(cases)):

    keys = list(map(int, input().split()))

    start = 1
 
    while(True):
        if start % keys[0] == start % keys[1]:
            break
        else:
            start += 1
    
    while(True):
        if start > keys[0] or start > keys[1]:
            print(start)
            break
        else:
            start += keys[0] * keys[1]
    