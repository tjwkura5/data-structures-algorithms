def eval_RPN(token):
    stack = []
    for token in token:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            smaller = stack.pop()
            bigger = stack.pop()
            stack.append(bigger - smaller)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            smaller = stack.pop()
            bigger = stack.pop()
            stack.append(int(float(bigger/smaller)))
        else:
            stack.append(int(token))
    return stack[0]

print(eval_RPN(["2","1","+","3","*"]))

print(eval_RPN(["4","13","5","/","+"]))

print(eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))