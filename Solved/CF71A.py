cases = input()

for i in range(int(cases)):

    word = list(input())

    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[len(word) - 1])
    else:
        print(''.join(word))