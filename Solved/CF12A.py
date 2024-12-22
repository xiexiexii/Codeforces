r1 = list(input())
r2 = list(input())
r3 = list(input())

triggerNext = True

for i in range(len(r1)):
    if r1[i] != r3[2-i]:
        print("NO")
        triggerNext = False
        break

if triggerNext == True:
    if r2[0] == r2[2]:
        print("YES")
    else:
        print("NO")

