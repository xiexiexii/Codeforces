cases = input()

for i in range(int(cases)):
    length = input()
    numbers = list(map(int, input().split()))
    numbers.append(1440)
    count = 0

    for j in range(len(numbers) - 1):
        if count >= 2:
            print("YES")
            break
        if numbers[j + 1] - numbers[j] >= 120:
            count += int((numbers[j + 1] - numbers[j]) / 120)
            if count >= 2:
                print("YES")
                break
    if count < 2:
        print("NO")
        
