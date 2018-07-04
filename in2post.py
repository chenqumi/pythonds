import re
from LinearStruc import Stack


prec = {
    '**': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}


def InFix2PostFix(expression):
    tokenlist = expression.split()
    opStack = Stack()
    postfix = []
    for token in tokenlist:
        pattern = r'[0-9a-zA-Z]+'
        if re.match(pattern, token):
            postfix.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfix.append(top)
                top = opStack.pop()
        else:
            if opStack.isEmpty():
                opStack.push(token)
            elif prec[token] <= prec[opStack.peek()]:
                postfix.append(opStack.pop())
                opStack.push(token)
            else:
                opStack.push(token)
        # print(postfix)
        # print(opStack)

    while not opStack.isEmpty():
        postfix.append(opStack.pop())

    print(' '.join(postfix))



test1 = '( A * ( B + C ) + D ) / E'
stack = ''
num = 'ABC+*D+'
test2 = 'A + B - C'
test3 = '( A + B ) * C - ( D - E ) * ( F + G )'
test4 = '5 * 3 ** ( 4 - 2 )'

InFix2PostFix(test1)
InFix2PostFix(test2)
InFix2PostFix(test3)
InFix2PostFix(test4)