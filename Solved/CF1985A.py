cases =  input()
cases = int(cases)

for i in range(cases):
    string = input()
    string = list(string)

    temp = string[0]
    string[0] = string[4]
    string[4] = temp

    print(''.join(string))
