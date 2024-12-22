cases = input()
cases = int(cases)

for i in range(cases):

    reqs = input().split()

    for j in range(2):
        reqs[j] = int(reqs[j])

    print(reqs[1] * (reqs[0] - 1) + 1)
        
