num = list(map(int, list(input())))
count = 0

while(1):
    if len(num) == 1:
        print(count)
        break
    else:
        num = list(map(int, list(str(sum(num)))))
        count += 1
