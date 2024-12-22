cases = input()
cases = int(cases)

for i in range(cases):

    string = list(input())

    for j in range(len(string)):

        if string[j] == "q":
            string[j] = "p"
        elif string[j] == "p":
            string[j] = "q"
    
    string = string[::-1]
    print(''.join(string))
    
