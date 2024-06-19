def calculate(tokens):
    stack = []
    num = ''
    operator = '+'
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token.isdigit() or token == '.':
            num += token
        if token == '(':
            num = calculate(tokens)
        if token in '+-*/)' or len(tokens) == 0:
            num = float(num)
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(stack.pop() / num)
            operator = token
            num = ''
        if token == ')':
            break
    return sum(stack)


if __name__ == '__main__':
    expression = input('请输入算数表达式: ')
    print(calculate(list(expression.replace(' ', ''))))
