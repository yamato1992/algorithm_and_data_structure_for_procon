n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

cnt = 0
for t in T:
    head = 0
    tail = n - 1
    while head <= tail:
        i = (head + tail) // 2
        if S[i] == t:
            cnt += 1
            break
        elif S[i] < t:
            head = i + 1
        else:
            tail = i - 1

print(cnt)