n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

c = 0

for t in T:
    for s in S:
        if t == s:
            c += 1
            break

print(c)
