cases = input()

for i in range(int(cases)):
    
    word = list(input())
    isTrue = False

    if len(word) == 1:
        print("NO")
    else:
        for j in range(len(word) - 1):
            if word[j] != word[j + 1]:
                temp = word[j]
                word[j] = word[j + 1]
                word[j + 1] = temp
                print("YES")
                print("".join(word))
                isTrue = True
                break

        if not isTrue:
            print("NO")