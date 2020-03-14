formula = input().split()
operand = ['+', '-', '*', '/']
stuck = []

for c in formula:
    if c in operand:
        b = str(stuck.pop())
        a = str(stuck.pop())
        stuck.append(eval(''.join([a, c, b])))
    else:
        stuck.append(c)

print(stuck.pop())
