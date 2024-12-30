cases = input()

for i in range(int(cases)):
    
    num = list(map(int, input().split()))

    if num[1] < num[0]:
        print(str(num[1]) + " " + str(num[0]))
    else:
        print(str(num[0]) + " " + str(num[1]))