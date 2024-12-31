cases = input()

for i in range(int(cases)):

    numcards = input()
    cards = list(map(int, input().split()))
    shuffles = input()
    cardsmoved = list(map(int, input().split()))

    print(cards[sum(cardsmoved) % int(numcards)])