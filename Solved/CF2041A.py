list = input().split()

for j in range(5):
    if str(j + 1) not in list:
        print(j + 1)
        break
