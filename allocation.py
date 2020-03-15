def check(n, k, W, P):
    i = 0
    for _ in range(k):
        capacity = 0
        while capacity + W[i] <= P:
            capacity += W[i]
            i += 1
            if i == n:
                return n
    return i

def solve(n, k, W):
    left = 0
    right = (10 ** 5) * (10 ** 5)
    mid = 0
    while (right - left) > 1:
        mid = (right + left) // 2
        v = check(n, k, W, mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right

n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]
print(solve(n, k, W))
