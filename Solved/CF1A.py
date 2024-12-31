import math

keys = list(map(int, input().split()))

print(int(math.ceil(keys[0] / keys[2]) * math.ceil(keys[1] / keys[2])))