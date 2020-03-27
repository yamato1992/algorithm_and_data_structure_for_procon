n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

result = []
for i in range(n):
    nums = result[::]
    result.append(a[i])
    for n in nums:
        result.append(n + a[i])

for mi in m:
    ans = 'yes' if mi in result else 'no'
    print(ans)
