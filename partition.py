def partition(arr, p: int, r: int):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

n = int(input())
a = list(map(int, input().split()))
index = partition(a, 0, n - 1)
ans = []
for i in range(n):
    ans.append('[' + str(a[i]) + ']' if i == index else str(a[i]))
print(*ans)
