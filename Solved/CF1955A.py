cases = input()
cases = int(cases)

for case in range(cases):
    
    string = input()
    array = string.split()

    for i in range(len(array)):
        array[i] = int(array[i])

    if 2 * array[1] < array[2]:
        print(int(array[0] * array[1]))
    else:
        print(int(array[2] * int((array[0] / 2)) + array[1] * (array[0] % 2)))
