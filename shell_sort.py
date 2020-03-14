def insertion_sort(A, g, n):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
        A[j + g] = v
    return A

def shell_sort(A, n):
    G = list()
    h = 1
    while h < n:
        G.append(h)
        h = 3 * h + 1
    G.reverse()
    for i in range(len(G)):
        insertion_sort(A, G[i], n)
    return A

n = int(input())
a = [int(input()) for _ in range(n)]
print(shell_sort(a, n))
