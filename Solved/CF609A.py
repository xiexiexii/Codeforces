driveCount = int(input())
size = int(input())
sum = 0
drives = []

for i in range(driveCount):
    drives.append(int(input()))

drives.sort(reverse=True)

for i in range(driveCount):
    sum += drives[i]
    if sum >= size:
        print(i + 1)
        break