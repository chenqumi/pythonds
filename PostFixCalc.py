from LinearStruc import Stack


def doMath(expression):
    tokenlist = expression.split()
    opStack = Stack()
    for token in tokenlist:
        try:
            token = int(token)
        except:
            pass
        if isinstance(token, int):
            opStack.push(token)
        else:
            num2 = opStack.pop()
            num1 = opStack.pop()
            tmp = Calc(num1, num2, token)
            opStack.push(tmp)
    return opStack.pop()

  
def Calc(num1, num2, op):
    if op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '+':
        return num1 + num2
    else:
        return num1 - num2


print(doMath('7 8 + 3 2 + /'))
