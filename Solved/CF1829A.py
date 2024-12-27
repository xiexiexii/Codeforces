cases = input()

for i in range(int(cases)):

    word = list(input())
    code = list("codeforces")
    count = 0

    for i in range(10):
        if word[i] != code[i]:
            count += 1
    print(count)