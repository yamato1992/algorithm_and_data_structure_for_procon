S = list(input())
areas = 0
cnt = 0
stack_1 = []
stack_2 = []

for i in range(len(S)):
    if S[i] == '\\':
        stack_1.append(i)
    elif S[i] == '/' and len(stack_1) > 0:
        j = stack_1.pop()
        area = i - j
        areas += area
        while len(stack_2) > 0 and stack_2[-1][0] > j:
            area += stack_2.pop()[1]
        stack_2.append([j, area])

print(areas)
if stack_2:
    print(len(stack_2), *list(zip(*stack_2))[1])
else:
    print(0)
    