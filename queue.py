n, q = map(int, input().split())
process = [input().split() for _ in range(n)]
task = process[:]
cnt = 0
last = 0
while task:
    t = task.pop(0)
    name, time = t[0], int(t[1])
    if time <= q:
        cnt += time
        print(name, cnt)
    else:
        task.append([name, str(time - q)])
        cnt += q
