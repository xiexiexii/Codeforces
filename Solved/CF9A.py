num = input().split()

for i in range(len(num)):
    num[i] = int(num[i])

if num[0] > num[1]:
    max = num[0]
else:
    max = num[1]

max = 7 - max

if max == 1 or max == 5:
    print(str(int(max)) + "/6")
elif max == 2 or max == 4:
    print(str(int(max / 2)) + "/3")
elif max == 3:
    print("1/2")
else:
    print("1/1")