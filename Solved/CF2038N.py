cases = input()
cases = int(cases)

for i in range(cases):

    expression = input()
    expression = list(expression)

    if expression[0] == expression[2]:
        expression[1] = "="
        print(''.join(expression))

    elif expression[0] > expression[2]:
        expression[1] = ">"
        print(''.join(expression))

    else:
        expression[1] = "<"
        print(''.join(expression))
