tests = input()
tests = int(tests)

for x in range(tests):
    length = input()
    length = int(length)
    password = input()
    chars = []
    isFalse = False
    for x in password:
        chars.append(int(ord(x)))
    for x in range(length - 1):
        if chars[x] > chars[x+1]:
            isFalse = True
            print("NO")
            break
    if isFalse != True:
        print("YES")
