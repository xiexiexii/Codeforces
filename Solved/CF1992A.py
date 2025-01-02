cases = input()

for i in range(int(cases)):

    nums = list(map(int, input().split()))

    for j in range(5):
        nums.sort()
        nums[0] += 1
    
    print(nums[0] * nums[1] * nums[2])