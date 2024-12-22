cases =  input()
cases = int(cases)

def ifZ(pwd):
    if pwd[i] == "z":
        pwd.insert(i+1, "a")
    else:
        pwd.insert(i+1, chr(ord(pwd[i])+1))

for i in range(cases):
    string = input()
    pwd = list(string)

    for i in range(int(len(pwd))):
        if len(pwd) == 1 or i == len(pwd) - 1:

            if pwd[i] == "z":
                pwd.append("a")
            else:
                pwd.append(chr(ord(pwd[i])+1))
            
            res = ''.join(pwd)
            print(res)
            break
        elif pwd[i] == pwd[i+1]:
            ifZ(pwd)
            res = ''.join(pwd)
            print(res)
            break
