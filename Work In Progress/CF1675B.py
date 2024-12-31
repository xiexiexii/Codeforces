cases = input()

for i in range(int(cases)):

    num = input()
    num = int(num) - 1
    nums = list(map(int, input().split()))
    count = 0
    stop = False

    

    '''
    for j in range(num):
        if stop == True:
            break
        while nums[num - j - 1] >= nums[num - j]:
            if nums[num - j - 1] == 0 and nums[num - j] == 0:
                count = -1
                stop = True
                break
            else:
                nums[num - j - 1] = int(nums[num - j - 1] / 2)
                count += 1
                # print(nums)
    print(count)
    # print(nums)
    '''