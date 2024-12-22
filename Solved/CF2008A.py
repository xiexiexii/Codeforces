cases = input()

for i in range(int(cases)):
    numbers = list(input())

    numbers[0] = int(numbers[0])
    numbers[2] = int(numbers[2])

    if numbers[0] % 2 == 1:
        print("NO")
    elif numbers[2] % 2 == 1 and numbers[0] == 0:
        print("NO")
    else:
        print("YES")