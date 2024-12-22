cases = input()
cases = int(cases)

people = 0

def p(ppl):
    global people
    people += ppl

def b(ppl):
    global people
    if (people - ppl) < 0:
        people = 0
        print("YES")
    else:
        people -= ppl
        print("NO")
    

for i in range(cases):

    event = input().split()
    
    if event[0] == "P":
        p(int(event[1]))
    else:
        b(int(event[1]))
