import math
import decimal

num = decimal.Decimal(input())

# print(num - math.floor(num))

if math.floor(num) % 10 == 9:
    print("GOTO Vasilisa.")
else:
    dec = num - math.floor(num)
    if dec < 0.5:
        print(math.floor(num))
    else:
        print(math.ceil(num))

'''
elif num - math.floor(num) >= 0.5:
    print(math.ceil(num))
else:
    print("Floor")
    print(math.floor(num))
'''