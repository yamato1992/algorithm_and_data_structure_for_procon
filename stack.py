formula = input().split()
operand = ['+', '-', '*', '/']
stack = []

for c in formula:
    if c in operand:
        b = str(stack.pop())
        a = str(stack.pop())
        stack.append(eval(''.join([a, c, b])))
    else:
        stack.append(c)

print(stack.pop())
