f = open("input.txt", "r")
f.read()

info = list(map(int, input().split()))
levels = list(map(int, input().split()))
level = []

unsorted = levels.copy()
levels.sort(reverse = True)

# print(levels[info[1] - 1]) 
file = open("output.txt", "w")
file.write(levels[info[1] - 1])

for i in range(info[1]):
    level.append(str(unsorted.index(levels[i]) + 1))

level.sort()

# print(" ".join(level))
file.write(levels[info[1] - 1])
file.close()

