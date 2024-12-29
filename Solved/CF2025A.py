cases = input()

for i in range(int(cases)):
    word1 = list(input())
    word2 = list(input())
    count = 0

    if len(word1) > len(word2):
        for j in range(len(word2)):
            if word2[j] == word1[j]:
                count += 1
            else:
                break
        
        count += (len(word1) - count) + (len(word2) - count)
        if word1[0] == word2[0]:
            count += 1
        print(count)

    else:
        for j in range(len(word1)):
            if word2[j] == word1[j]:
                count += 1
            else:
                break
        count += (len(word1) - count) + (len(word2) - count)
        if word1[0] == word2[0]:
            count += 1
        print(count)