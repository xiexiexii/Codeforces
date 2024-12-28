cases = input()

for i in range(int(cases)):

    num = list(map(int, input()))
    num.insert(0, 1)
    sum = 4

    for j in range(4):
        if num[j] == num[j+1]:
            sum = sum
        elif num[j] == 0:
            sum += abs(10 - num[j + 1])
        elif num[j + 1] == 0:
            sum += abs(10 - num[j])
        else:
            sum += abs(num[j + 1] - num[j])
    print(sum)
